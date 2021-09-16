import os
import sqlite3
import pymysql
from data.config import MySQL_db_host, MySQL_db_login, MySQL_db_password, MySQL_db_name


def execute_query_mysql(query):
    conn = pymysql.connect(host=MySQL_db_host,
                           port = 3306,
                           user=MySQL_db_login,
                           password=MySQL_db_password,
                           database=MySQL_db_name,
                           charset='utf8mb4')
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    conn.commit()
    conn.close()
    return result


def execute_query(query):
    db_path = os.path.join(os.getcwd(), 'db.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    conn.commit()
    conn.close()
    return result
