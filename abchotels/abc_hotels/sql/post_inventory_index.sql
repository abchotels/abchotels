-- add unique index if missing
SET @idx_name := 'uniq_rti';
SELECT COUNT(*)
INTO @exists
FROM information_schema.statistics
WHERE table_schema = DATABASE()
  AND table_name = 'tabRoom Type Inventory'
  AND index_name = @idx_name;

SET @sql := IF(@exists = 0,
    'ALTER TABLE `tabRoom Type Inventory` ADD UNIQUE KEY uniq_rti (room_type, rate_code, for_date)',
    'SELECT "Index uniq_rti already exists"');

PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- add lookup index if missing
SET @idx_name := 'idx_rti_lookup';
SELECT COUNT(*)
INTO @exists
FROM information_schema.statistics
WHERE table_schema = DATABASE()
  AND table_name = 'tabRoom Type Inventory'
  AND index_name = @idx_name;

SET @sql := IF(@exists = 0,
    'ALTER TABLE `tabRoom Type Inventory` ADD KEY idx_rti_lookup (room_type, rate_code, for_date)',
    'SELECT "Index idx_rti_lookup already exists"');

PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
