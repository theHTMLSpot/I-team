import sqlite3
import logging
from database import get_db_connection

def initialize_db():
    """Initialize the database by creating the users table if it does not exist."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            logging.info("Creating users table if not exists...")
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                id_ TEXT,
                cv BLOB
            )
            ''')
            conn.commit()
            logging.info("Database initialized successfully.")
    except sqlite3.Error as e:
        logging.error(f"An error occurred while initializing the database: {e}")