# MySQLServer.py
import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL (change user & password if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1123581321*MySQL"  # Change to your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
