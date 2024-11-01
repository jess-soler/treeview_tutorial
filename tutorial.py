# tutorial.py

import tkinter as tk
from tkinter import scrolledtext

class Tutorial:
    def __init__(self, root):
        """Initialize the tutorial window and its content."""
        self.tutorial_window = tk.Toplevel(root)
        self.tutorial_window.title("Tutorial")
        self.tutorial_window.attributes('-fullscreen', True)  # Set full screen
        self.tutorial_window.resizable(False, False)  # Make it non-resizable

        # Create a custom title bar for the tutorial window
        title_bar = tk.Frame(self.tutorial_window, bg='lightgray', relief='raised', bd=2)
        title_bar.pack(fill=tk.X)

        close_button = tk.Button(title_bar, text='X', command=self.tutorial_window.destroy, bg='red', fg='white')
        close_button.pack(side=tk.RIGHT)

        minimize_button = tk.Button(title_bar, text='–', command=self.tutorial_window.iconify, bg='orange', fg='white')
        minimize_button.pack(side=tk.RIGHT)

        # Create a ScrolledText widget for displaying the tutorial
        self.tutorial_text = scrolledtext.ScrolledText(self.tutorial_window, wrap=tk.WORD)
        self.tutorial_text.pack(expand=True, fill=tk.BOTH)

        # Add tutorial content
        self.add_tutorial_content()

    def add_tutorial_content(self):
        """Add tutorial steps to the text widget."""
        self.tutorial_text.insert(tk.END, "Tutorial: Creating a Tkinter Treeview with Database Integration\n\n", 'title')
        
        self.tutorial_text.insert(tk.END, "Step 1: **Setting Up the Database**\n", 'step')
        self.tutorial_text.insert(tk.END, "- Create a file named `database.py`.\n")
        self.tutorial_text.insert(tk.END, "- Import the sqlite3 library and create a `Database` class.\n")
        self.tutorial_text.insert(tk.END, "- In the constructor, establish a connection to the SQLite database and create the employees table if it doesn't exist.\n\n")
        
        self.insert_code_snippet("""import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('employees.db')  # Connect to the database
        self.cursor = self.conn.cursor()  # Create a cursor object
        self.create_table()  # Call the method to create the table

    def create_table(self):
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,  # Employee ID
                name TEXT,              # Employee name
                age INTEGER,            # Employee age
                occupation TEXT         # Employee occupation
            )'''
        )
        self.conn.commit()  # Commit the changes to the database
""")

        self.tutorial_text.insert(tk.END, "Step 2: **Creating the Main Application**\n", 'step')
        self.tutorial_text.insert(tk.END, "- Create a file named `app.py`.\n")
        self.tutorial_text.insert(tk.END, "- Import tkinter and ttk, and create a `App` class.\n")
        self.tutorial_text.insert(tk.END, "- Initialize the Tkinter root window and set up the Treeview to display employee records.\n\n")
        
        self.insert_code_snippet("""import tkinter as tk
from tkinter import ttk
from database import Database

class App:
    def __init__(self, root):
        self.root = root  # Store the root window
        self.root.title("Treeview with Database")  # Set window title
        self.root.geometry("600x400")  # Set the window size

        self.db = Database()  # Create an instance of the Database class
        self.setup_treeview()  # Call the method to set up the Treeview
        self.setup_widgets()  # Call the method to set up input widgets
        self.load_data()  # Load data from the database into the Treeview
""")

        self.tutorial_text.insert(tk.END, "Step 3: **Setting Up the Treeview**\n", 'step')
        self.tutorial_text.insert(tk.END, "- Create a method `setup_treeview` inside the `App` class.\n")
        self.tutorial_text.insert(tk.END, "- Define the Treeview with columns for ID, Name, Age, and Occupation.\n")
        self.tutorial_text.insert(tk.END, "- Add a scrollbar to the Treeview for better navigation.\n\n")
        
        self.insert_code_snippet("""def setup_treeview(self):
    self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Age", "Occupation"), show='headings')  # Create Treeview
    self.tree.heading("ID", text="ID")  # Set column headings
    self.tree.heading("Name", text="Name")
    self.tree.heading("Age", text="Age")
    self.tree.heading("Occupation", text="Occupation")

    self.tree.pack(expand=True, fill=tk.BOTH)  # Add the Treeview to the window
    self.tree.bind("<ButtonRelease-1>", self.select_item)  # Bind item selection event

    # Create a vertical scrollbar
    scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.tree.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    self.tree.configure(yscroll=scrollbar.set)  # Link scrollbar to the Treeview
""")

        self.tutorial_text.insert(tk.END, "Step 4: **Setting Up Input Widgets**\n", 'step')
        self.tutorial_text.insert(tk.END, "- Create input fields for Name, Age, and Occupation.\n")
        self.tutorial_text.insert(tk.END, "- Add buttons for Add, Update, Delete, and Clear functionalities.\n\n")
        
        self.insert_code_snippet("""def setup_widgets(self):
    # Entry fields for input
    self.entry_name = tk.Entry(self.root)
    self.entry_age = tk.Entry(self.root)
    self.entry_occupation = tk.Entry(self.root)

    # Buttons for CRUD operations
    btn_add = tk.Button(self.root, text="Add", command=self.add_entry)
    btn_update = tk.Button(self.root, text="Update", command=self.update_entry)
    btn_delete = tk.Button(self.root, text="Delete", command=self.delete_entry)
    btn_clear = tk.Button(self.root, text="Clear", command=self.clear_entries)

    # Pack the widgets
    self.entry_name.pack()
    self.entry_age.pack()
    self.entry_occupation.pack()
    btn_add.pack()
    btn_update.pack()
    btn_delete.pack()
    btn_clear.pack()
""")

        self.tutorial_text.insert(tk.END, "Step 5: **Implementing CRUD Operations**\n", 'step')
        self.tutorial_text.insert(tk.END, "- Define methods for Add, Update, Delete, and Clear operations.\n")
        self.tutorial_text.insert(tk.END, "- Each method interacts with the database to manage employee records.\n\n")

        self.insert_code_snippet("""def add_entry(self):
    name = self.entry_name.get()  # Get name from entry
    age = self.entry_age.get()  # Get age from entry
    occupation = self.entry_occupation.get()  # Get occupation from entry

    self.db.insert(name, age, occupation)  # Insert data into database
    self.load_data()  # Refresh Treeview data
    self.clear_entries()  # Clear input fields

def update_entry(self):
    selected_item = self.tree.selection()[0]  # Get selected item
    selected_id = self.tree.item(selected_item, "values")[0]  # Get ID from selected item
    name = self.entry_name.get()  # Get updated name
    age = self.entry_age.get()  # Get updated age
    occupation = self.entry_occupation.get()  # Get updated occupation

    self.db.update(selected_id, name, age, occupation)  # Update database record
    self.load_data()  # Refresh Treeview data
    self.clear_entries()  # Clear input fields

def delete_entry(self):
    selected_item = self.tree.selection()[0]  # Get selected item
    selected_id = self.tree.item(selected_item, "values")[0]  # Get ID from selected item

    self.db.delete(selected_id)  # Delete record from database
    self.load_data()  # Refresh Treeview data
    self.clear_entries()  # Clear input fields

def clear_entries(self):
    self.entry_name.delete(0, tk.END)  # Clear name entry
    self.entry_age.delete(0, tk.END)  # Clear age entry
    self.entry_occupation.delete(0, tk.END)  # Clear occupation entry
""")

        self.tutorial_text.insert(tk.END, "Step 6: **Loading Data into the Treeview**\n", 'step')
        self.tutorial_text.insert(tk.END, "- Create a method `load_data` that fetches records from the database and displays them in the Treeview.\n\n")
        
        self.insert_code_snippet("""def load_data(self):
    for row in self.tree.get_children():  # Clear existing Treeview data
        self.tree.delete(row)

    for row in self.db.fetch_all():  # Fetch all records from the database
        self.tree.insert("", tk.END, values=row)  # Insert records into the Treeview
""")

        self.tutorial_text.insert(tk.END, "Step 7: **Running the Application**\n", 'step')
        self.tutorial_text.insert(tk.END, "- Finally, create an instance of the `App` class in the main block to run the application.\n")
        self.tutorial_text.insert(tk.END, "- Run the `app.py` file to see the application in action!\n\n")
        
        self.insert_code_snippet("""if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)  # Create an instance of App
    root.mainloop()  # Start the Tkinter main loop
""")

        self.tutorial_text.tag_config('title', font=('Arial', 16, 'bold'))
        self.tutorial_text.tag_config('step', font=('Arial', 14, 'underline'))

        self.tutorial_text.config(state=tk.DISABLED)  # Disable editing in the ScrolledText widget

    def insert_code_snippet(self, code):
        """Insert a code snippet into the tutorial text."""
        self.tutorial_text.insert(tk.END, f"```python\n{code}\n```\n\n")  # Format code as a code block

# Main application to launch the tutorial
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    tutorial = Tutorial(root)  # Create the tutorial
    root.mainloop()  # Start the Tkinter main loop