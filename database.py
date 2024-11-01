# database.py
"""
Tutorial: This file contains the Database class for managing database interactions 
in our Tkinter Treeview app. The Database class encapsulates all database-related 
operations, keeping them modular and separate from the main application logic.

Sections covered:
- Class Initialization: Connect to SQLite database.
- Table Creation: Create the employees table if it doesn't exist.
- Data Fetching: Retrieve records from the database.
- Inserting, Updating, Deleting: Modify the database based on user actions.
- Connection Management: Properly close the database connection.
"""

import sqlite3

class Database:
    def __init__(self, db_name="treeview_data.db"):
        """Initialize database connection and create the employees table if it doesn't exist."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """Create the employees table in the database."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                occupation TEXT
            )
        ''')
        self.connection.commit()

    def fetch_all(self):
        """Fetch all employee records from the database."""
        self.cursor.execute("SELECT id, name, age, occupation FROM employees")
        return self.cursor.fetchall()

    def insert(self, name, age, occupation):
        """Insert a new employee record into the database."""
        self.cursor.execute("INSERT INTO employees (name, age, occupation) VALUES (?, ?, ?)", (name, age, occupation))
        self.connection.commit()

    def update(self, emp_id, name, age, occupation):
        """Update an employee record in the database."""
        self.cursor.execute("UPDATE employees SET name = ?, age = ?, occupation = ? WHERE id = ?", (name, age, occupation, emp_id))
        self.connection.commit()

    def delete(self, emp_id):
        """Delete an employee record from the database."""
        self.cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
        self.connection.commit()

    def close(self):
        """Close the database connection."""
        self.connection.close()