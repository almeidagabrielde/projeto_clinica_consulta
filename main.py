from db_credentials import mysql_db_config
from etl import etl_process
from sql_queries import mysql_queries


def main(postgresql):
    print('starting etl')

    # establish connection for target database
    target_cnx = postgresql.connect('dw_clinica')

    # loop through credentials

    # mysql
    for config in mysql_db_config:
        try:
            print("loa.ing db: " + config['database'])
            etl_process(mysql_queries, target_cnx, config, 'mysql')
        except Exception as error:
            print("etl for {} has error".format(config['database']))
            print('error message: {}'.format(error))
            continue


    target_cnx.close()