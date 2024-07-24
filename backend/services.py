from database import get_db_connection
from uuid import UUID, uuid4
from typing import Optional
import sqlite3
import logging

def insert_user(name: str, email: str, cv: str = None, id: Optional[UUID] = None):
    id = id or uuid4()  # Use provided ID or generate a new one

    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()

            # Check if the email already exists
            cursor.execute('SELECT 1 FROM users WHERE email = ?', (email,))
            if cursor.fetchone() is not None:
                raise ValueError("Email already in use")

            # Proceed with inserting the new user
            cursor.execute('''
                INSERT INTO users (id_, name, email, cv, verified)
                VALUES (?, ?, ?, ?, ?)
            ''', (str(id), name, email, cv, False))
            conn.commit()
            logging.info("User inserted successfully.")

    except sqlite3.Error as e:
        logging.error(f"An error occurred while inserting the user: {e}")
        raise  # Reraise the exception for further handling if needed

    except ValueError as e:
        logging.warning(f"Validation error: {e}")
        raise  # Reraise the exception for further handling if needed

def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    
    conn.close()
    return users

def get_user(name: str, email: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT * FROM users
    WHERE name = ? AND email = ?
    ''', (name, email))
    
    user = cursor.fetchone()
    
    conn.close()
    return user

def verify_user(name: str, email: str):
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            # Update the user's verified status
            cursor.execute('''
            UPDATE users
            SET verified = ?
            WHERE name = ? AND email = ?
            ''', (True, name, email))
            
            conn.commit()
            
            # Retrieve the updated user
            cursor.execute('''
            SELECT * FROM users
            WHERE name = ? AND email = ?
            ''', (name, email))
            
            user = cursor.fetchone()
            
            return user

    except sqlite3.Error as e:
        logging.error(f"An error occurred while verifying the user: {e}")
        raise  # Reraise the exception for further handling if needed