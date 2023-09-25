import mysql.connector
import sys


def Connect():
    conn = None
    try:
        conn = mysql.connector.Connect(
            host='localhost',
            user='root',
            password='',
            database='travel_ticket'
        )
        print("Connected to MySQL Database")

    except:
        print("Error connecting to MySQL server.", sys.exc_info())

    finally:
        return conn
