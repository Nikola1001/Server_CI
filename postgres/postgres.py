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
    print("Информация о сервере PostgreSQL")
    print(connection.get_dsn_parameters(), "\n")

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version {cursor.fetchone()}")




except Exception as ex:
    print("Не удалось подключиться")
    print(ex)
finally:
    if connection:
        connection.close()
        print("connection close OK")
