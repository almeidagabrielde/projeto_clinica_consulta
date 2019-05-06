from variables import datawarehouse_name

# postgresql (target db, datawarehouse)
datawarehouse_db_config = {
  'Trusted_Connection': 'yes',
  'driver': '{POSTGRESQL}',
  'server': 'datawarehouse_postgresql',
  'database': '{}'.format('dw_clinica'),
  'user': 'your_db_username',
  'password': 'your_db_password',
  'autocommit': True,
}

# mysql
mysql_db_config = [
  {
   'user': 'clinica',
   'password': 'clinica_01',
   'host': 'guilhermetecnologia.ddns.net:3307',
   'database': 'clinica_medica'
  }
 ]
