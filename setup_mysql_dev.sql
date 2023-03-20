-- a script that prepares a MYSQL serer for the project
-- create a database user password privileges and SELECT privilleges
-- if DATABASE already exists the script won't fail
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- if the user already exists the script doesn't fail
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- the user should have all privileges on the databse and only that database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- SELECT privileges to another database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
