# pip install mysql-connector-python

import mysql.connector

def connect_to_mysql(host, username, password, database):
    try:
        # Establish a connection to MySQL
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )

        if connection.is_connected():
            print("Connected to MySQL database!")
            return connection
        else:
            print("Failed to connect to MySQL database.")
            return None
        
    except Exception as e:
        print("Error:", e)
        return None