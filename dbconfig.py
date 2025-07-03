import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost", 
            database="cd_automation",  
            user="root", 
            port="3306",
            password="shankar"  
        )
        if connection.is_connected():
            print("✅ Connection successful!")
            return connection
    except Error as e:
        print("❌ Connection failed:")
        print(e)
        return None
