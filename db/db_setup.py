import psycopg2
from psycopg2 import Error


def setup():
    try:
        connection = psycopg2.connect(user="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="tradebull")
        cursor = connection.cursor()
        return cursor, connection
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)


def create_tables(cursor, connection):
    create_table_query = '''create table if not exists trade_history(
                            id serial primary key,
                            strategy_id int,
                            type varchar(4) not null,
                            asset_type varchar(10) not null,
                            asset_price decimal(19,6) not null,
                            trade_date date not null,
                            opening_price decimal(19,6) not null,
                            opening_timestamp timestamp without time zone not null,
                            closing_price decimal(19,6),
                            closing_timestamp timestamp without time zone,
                            pl_value decimal(19,6),
                            pl_percent decimal(5,3)); '''

    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")


def insert(cursor, connection, table_name, data):
    insert_query = "INSERT INTO " + table_name + "VALUES " + data + ";"
    cursor.execute(insert_query)
    connection.commit()
    print("1 Record inserted successfully")
    # Fetch result
    cursor.execute("SELECT * from " + table_name)
    record = cursor.fetchall()
    print("Result ", record)


def update(cursor, connection, update_query):
    cursor.execute(update_query)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record updated successfully ")
    # Fetch result
    cursor.execute("SELECT * from mobile")
    print("Result ", cursor.fetchall())


def delete(cursor, connection):
    # Executing a SQL query to delete table
    delete_query = """Delete from mobile where id = 1"""
    cursor.execute(delete_query)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record deleted successfully ")
    # Fetch result
    cursor.execute("SELECT * from mobile")
    print("Result ", cursor.fetchall())
