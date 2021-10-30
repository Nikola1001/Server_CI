import datetime

import psycopg2
# from .config import *

host = '18.223.114.75'
user = 'test_user'
password = '1234'
db_name = 'db_name'


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port=5432
    )
    connection.autocommit = True
    # print("Информация о сервере PostgreSQL")
    # print(connection.get_dsn_parameters(), "\n")

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version {cursor.fetchone()}")

    with connection.cursor() as cursor:
        # cursor.execute("DROP TABLE Denis_pidor")
        create_table_query = '''CREATE TABLE IF NOT EXISTS Denis_pidor (
        	    item_id serial NOT NULL PRIMARY KEY,
        	    item_name VARCHAR (100) NOT NULL,
        	    price INTEGER NOT NULL
            );'''
        cursor.execute(create_table_query)
        # connection.commit()

    with connection.cursor() as cursor:
        insert_query = """ INSERT INTO Denis_pidor (item_Id, item_name, price)
                                      VALUES (%s, %s, %s)"""
        item_tuple = (2, "Keyboard",  150)
        cursor.execute(insert_query, item_tuple)
        print("1 элемент успешно добавлен")

        # cursor.execute("SELECT purchase_time from Denis_pidor where item_id = 12")
        # purchase_datetime = cursor.fetchone()
        # print("Дата покупки товара", purchase_datetime[0].date())
        # print("Время покупки товара", purchase_datetime[0].time())

except Exception as ex:
    print("Не удалось подключиться")
    print(ex)
finally:
    if connection:
        connection.close()
        print("connection close OK")
