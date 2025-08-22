# -*- coding: utf-8 -*-
from . import __version__ as app_version

app_name = "abchotels"
app_title = "ABC Hotels"
app_publisher = "Your Name"
app_description = "Custom app for hotel management"
app_icon = "octicon octicon-home"
app_color = "blue"
app_email = "your.email@example.com"
app_license = "MIT"

app_include_css = "/assets/abchotels/css/abchotels.css"
app_include_js = "/assets/abchotels/js/abchotels.js"

desk_page = {"ABC Hotels": "abchotels/workspace/abc_hotels"}

website_include_js = ["/assets/abchotels/js/website.js"]

website_route_rules = [
    {"from_route": "/abchotels/<path:app_path>", "to_route": "abchotels"}
]
# Install / migrate hooks
after_install = "abchotels.setup.installer.after_install"
after_migrate = "abchotels.setup.installer.after_migrate"


fixtures = [
	{
		"doctype": "Room Type"
	},
	{
		"doctype": "Cancelation Policy"
	},
	{
		"doctype": "Rate Code"
	},
	{
		"doctype": "Room Type Inventory"
	},
	{
		"doctype": "Property"
	},
	{
		"doctype": "Room Type Room"
	},
	{
		"doctype": "Amenity"
	},
	{
		"doctype": "Room Category"
	},
	{
		"doctype": "Bed Type"
	},
	{
        "doctype": "Role",
        "filters": [
            ["role_name", "in", [
                "Reservation Agent",
                "Reservation Manager",
                "Front Desk",
                "Accountant",
                "Inventory Engine",
                "Night Auditor",
                "Revenue Manager",
                "Housekeeping",
                "Housekeeping Supervisor",
                "Maintenance",
                "POS Cashier",
                "POS Supervisor",
                "Restaurant Manager",
                "Property Manager (GM)",
                "Device Service",
                "API Integration",
            ]]
        ],
    },

    # Custom DocPerm for core doctypes you touched
    {"doctype": "Custom DocPerm", "filters": [["parent", "in", [
                "Reservation Agent",
                "Reservation Manager",
                "Front Desk",
                "Accountant",
                "Inventory Engine",
                "Night Auditor",
                "Revenue Manager",
                "Housekeeping",
                "Housekeeping Supervisor",
                "Maintenance",
                "POS Cashier",
                "POS Supervisor",
                "Restaurant Manager",
                "Property Manager (GM)",
                "Device Service",
                "API Integration",
    ]]]},

    # Optional: grant page/report access as fixtures
    {"doctype": "Role Permission for Page and Report", "filters": [["role", "in", [
                "Reservation Agent",
                "Reservation Manager",
                "Front Desk",
                "Accountant",
                "Inventory Engine",
                "Night Auditor",
                "Revenue Manager",
                "Housekeeping",
                "Housekeeping Supervisor",
                "Maintenance",
                "POS Cashier",
                "POS Supervisor",
                "Restaurant Manager",
                "Property Manager (GM)",
                "Device Service",
                "API Integration",
    ]]]},
	{
		"doctype": "Workspace",
		"filters": [
			[
				"module",
				"=",
				"ABC Hotels"
			]
		]
	}
]
