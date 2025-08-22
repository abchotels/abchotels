# abchotels/abchotels/setup/installer.py
import os
import frappe
from pathlib import Path
from .seed_roles_perms import seed_roles_and_permissions
from .seed_modules import seed_module_profiles
from .seed_users import seed as seed_users
SQL_DIR = Path(frappe.get_app_path("abchotels", "abc_hotels", "sql"))
DEBUG = os.environ.get("BENCH_DEBUG", "").lower() in {"1", "true", "yes"}

def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _exec_sql_file(filename: str, split: bool = False) -> None:
    sql = _read(SQL_DIR / filename)
    if split:
        # safe split for simple DDL (NOT for procedures)
        statements = [s.strip() for s in sql.split(";") if s.strip()]
        for stmt in statements:
            frappe.db.sql(stmt)
    else:
        # execute as a single statement (use for CREATE PROCEDURE)
        frappe.db.sql(sql)


def _create_inventory_key():
    _exec_sql_file("post_inventory_index.sql", split=True)   # optional

def _create_inventory_seeder():
    _exec_sql_file("seed_room_type_inventory_drop.sql", split=True)   # optional
    _exec_sql_file("seed_room_type_inventory_create.sql", split=False)


def _create_dim_date_objects() -> None:
    # tabl
    _exec_sql_file("dim_date_table.sql", split=True)
    # procedure (drop + create as two separate files so we don't need custom splitting)
    _exec_sql_file("seed_dim_date_drop.sql", split=True)
    _exec_sql_file("seed_dim_date_create.sql", split=False)

def _seed_dim_date_default() -> None:
    # Seed a sensible horizon; adjust as you like
    frappe.db.sql(
        "CALL seed_dim_date(%s, %s, %s, %s)",
        ("2020-01-01", "2035-12-31", "FRI_SAT", "+03:00"),
    )


def _safe(label: str, fn, **kwargs):
    print(f"[abchotels] START {label} kwargs={kwargs}")  # stdout so bench shows it
    try:
        out = fn(**kwargs) if kwargs else fn()
        # Many seeders already commit; doing it again is harmless and ensures we flush
        frappe.db.commit()
        print(f"[abchotels] OK    {label} -> {out}")
        return out
    except Exception:
        # log to file and also rethrow so bench shows the traceback (no silent hang)
        frappe.logger("abchotels").exception(f"[abchotels] {label} failed")
        if DEBUG:
            raise
        else:
            # Still surface an error to bench so it doesn't look stuck
            raise

def after_install():
    _safe("seed_roles_and_permissions", seed_roles_and_permissions)
    _safe("seed_module_profiles",      seed_module_profiles)

    # Optional but recommended if you added it:
    # _safe("lock_workspaces_by_job",     lock_workspaces_by_job)

    # Always seed users; pulls defaults from site_config if present
    domain = frappe.conf.get("abchotels_email_domain", "hotel.local")
    default_property = frappe.conf.get("abchotels_default_property")
    _create_dim_date_objects()
    _seed_dim_date_default()
    _create_inventory_seeder()
    _safe("seed_users", seed_users, domain=domain, property_name=default_property)

def after_migrate():
    # Keep after_migrate short & safe
    _safe("seed_module_profiles",      seed_module_profiles)
    # If you use workspace locking, re-apply here too:
    # _safe("lock_workspaces_by_job",     lock_workspaces_by_job)
    ensure_dim_date()
    return {"ok": True}



def ensure_dim_date():
    # Re-create if missing, then ensure seeded horizon exists (idempotent)
    _create_inventory_key()
    _create_dim_date_objects()
    _seed_dim_date_default()

