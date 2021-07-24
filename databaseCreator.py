import sqlite3
import os.path
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def getDatabasePath():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    database = ".\Databases\pokedex.db"
    db_path = os.path.join(BASE_DIR, database )
    return db_path

def main():
    conn = create_connection(getDatabasePath())
    sql='''    CREATE TABLE IF NOT EXISTS pokemons (
        Id integer PRIMARY KEY AUTOINCREMENT,
        pokemonName text,
        baseExperience INTEGER,
        height INTEGER,
        type text,
        ability text,
        health INTEGER
    );'''
    create_table(conn,sql)


if __name__ == "__main__":
    main()