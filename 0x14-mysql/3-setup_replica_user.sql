-- create a user to replicate the database and grant the permission to do so

  CREATE USER
IF NOT EXISTS 'replica_user'@'%'
IDENTIFIED BY 'replica_pass';

GRANT REPLICATION SLAVE
   ON *.*
   TO 'replica_user'@'%';

GRANT SELECT
   ON mysql.user
   TO 'holberton_user'@'localhost';
