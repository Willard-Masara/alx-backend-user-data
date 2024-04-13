#!/usr/bin/env python3

"""
This module provides functions for connecting to a secure database and retrieving user data.
"""

import os
import mysql.connector
from typing import List
from filter_datum import filter_datum

def get_db():
    """
    Connect to a secure database and return the connection object.

    Returns:
        A MySQLConnection object for interacting with the database.
    """
    # Get database credentials from environment variables
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    dbname = os.getenv("PERSONAL_DATA_DB_NAME")

    # Connect to the database
    connection = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=dbname
    )

    return connection

def main():
    """
    Retrieve user data from the database and display it under a filtered format.
    """
    # Fields to be filtered
    fields_to_filter = ['name', 'email', 'phone', 'ssn', 'password']

    # Connect to the database
    db_connection = get_db()

    # Create a cursor to execute SQL queries
    cursor = db_connection.cursor()

    # Retrieve all rows from the users table
    cursor.execute("SELECT * FROM users")

    # Fetch all rows
    rows = cursor.fetchall()

    # Display each row under a filtered format
    for row in rows:
        # Construct log message
        log_message = "; ".join([f"{field}={value}" for field, value in zip(cursor.column_names, row)])

        # Filter sensitive fields
        filtered_message = filter_datum(fields_to_filter, "***", log_message, "; ")

        # Log filtered message
        print(f"[HOLBERTON] user_data INFO {filtered_message}")

    # Close cursor and connection
    cursor.close()
    db_connection.close()

if __name__ == "__main__":
    main()

