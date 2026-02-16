import mysql.connector
from config import DB_CONFIG

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def run_query(sql):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close()
    conn.close()
    return result
