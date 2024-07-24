import sqlite3
import logging

def get_db_connection() -> sqlite3.Connection:
    """Establish a connection to the SQLite database and return the connection object."""
    try:
        conn = sqlite3.connect('database.db')
        return conn
    except sqlite3.Error as e:
        logging.error(f"Database connection error: {e}")
        raise

