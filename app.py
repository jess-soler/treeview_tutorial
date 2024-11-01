# app.py

import tkinter as tk
from tkinter import ttk
from database import Database
from tutorial import Tutorial

class App:
    def __init__(self, root):
        """Initialize the main application and tutorial help window button."""
        self.root = root
        self.root.title("Treeview with Database")
        self.root.attributes('-fullscreen', True)  # Start in fullscreen mode

        # Initialize the database
        self.db = Database()

        # Create a custom title bar
        self.create_title_bar()

        # Set up the main components
        self.setup_treeview()
        self.setup_widgets()
        self.load_data()

        # Exit button at the bottom
        exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)  # Default button color
        exit_button.pack(side=tk.BOTTOM, pady=10)  # Add padding for spacing

    def create_title_bar(self):
        """Create a custom title bar with minimize and close buttons."""
        title_bar = tk.Frame(self.root, bg='lightgray', relief='raised', bd=2)
        title_bar.pack(fill=tk.X)

        close_button = tk.Button(title_bar, text='X', command=self.root.quit, bg='red', fg='white')
        close_button.pack(side=tk.RIGHT)

        minimize_button = tk.Button(title_bar, text='–', command=self.minimize_window, bg='orange', fg='white')
        minimize_button.pack(side=tk.RIGHT)

        # Fullscreen toggle button
        fullscreen_button = tk.Button(title_bar, text='[ ]', command=self.toggle_fullscreen, bg='green', fg='white')
        fullscreen_button.pack(side=tk.RIGHT)

    def minimize_window(self):
        """Minimize the main application window."""
        self.root.iconify()

    def toggle_fullscreen(self):
        """Toggle fullscreen mode for the application."""
        self.root.attributes('-fullscreen', not self.root.attributes('-fullscreen'))

    def setup_treeview(self):
        """Create and configure the Treeview widget."""
        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Age", "Occupation"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Occupation", text="Occupation")

        # Add a scrollbar for the Treeview
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Bind select event
        self.tree.bind("<<TreeviewSelect>>", self.select_item)

    def setup_widgets(self):
        """Create entry fields and action buttons."""
        tk.Label(self.root, text="Name").pack()
        self.entry_name = tk.Entry(self.root)
        self.entry_name.pack()

        tk.Label(self.root, text="Age").pack()
        self.entry_age = tk.Entry(self.root)
        self.entry_age.pack()

        tk.Label(self.root, text="Occupation").pack()
        self.entry_occupation = tk.Entry(self.root)
        self.entry_occupation.pack()

        # Action buttons
        tk.Button(self.root, text="Add Employee", command=self.add_entry).pack()
        tk.Button(self.root, text="Update Employee", command=self.update_entry).pack()
        tk.Button(self.root, text="Delete Employee", command=self.delete_entry).pack()

        # Help button to open tutorial window
        tutorial_button = tk.Button(self.root, text="Tutorial", command=self.show_tutorial, bg='green', fg='white')  # Green button
        tutorial_button.pack()

    def load_data(self):
        """Load data from the database into the Treeview widget."""
        for item in self.tree.get_children():
            self.tree.delete(item)

        for row in self.db.fetch_all():
            self.tree.insert('', 'end', values=row)

    def add_entry(self):
        """Add a new employee record to the database and reload the data."""
        name = self.entry_name.get()
        age = int(self.entry_age.get())
        occupation = self.entry_occupation.get()

        self.db.insert(name, age, occupation)
        self.load_data()
        self.clear_entries()

    def update_entry(self):
        """Update the selected employee record in the database and reload the data."""
        selected_item = self.tree.selection()[0]
        selected_id = self.tree.item(selected_item, "values")[0]

        name = self.entry_name.get()
        age = int(self.entry_age.get())
        occupation = self.entry_occupation.get()

        self.db.update(selected_id, name, age, occupation)
        self.load_data()
        self.clear_entries()

    def delete_entry(self):
        """Delete the selected employee record from the database and reload the data."""
        selected_item = self.tree.selection()[0]
        selected_id = self.tree.item(selected_item, "values")[0]

        self.db.delete(selected_id)
        self.load_data()
        self.clear_entries()

    def clear_entries(self):
        """Clear the input entry fields."""
        self.entry_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_occupation.delete(0, tk.END)

    def select_item(self, event):
        """Populate the entry fields with the selected item's data."""
        selected_item = self.tree.selection()[0]
        selected_data = self.tree.item(selected_item, "values")
        self.entry_name.delete(0, tk.END)
        self.entry_name.insert(0, selected_data[1])
        self.entry_age.delete(0, tk.END)
        self.entry_age.insert(0, selected_data[2])
        self.entry_occupation.delete(0, tk.END)
        self.entry_occupation.insert(0, selected_data[3])

    def show_tutorial(self):
        """Show the tutorial window."""
        Tutorial(self.root)  # Create a tutorial instance

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()