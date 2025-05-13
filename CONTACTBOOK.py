import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# --- DATABASE SETUP ---
conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL UNIQUE,
        email TEXT,
        address TEXT
    )
""")
conn.commit()

# --- MAIN APP ---
class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("600x500")
        
        # --- VARIABLES ---
        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()
        self.search_var = tk.StringVar()

        # --- WIDGETS ---
        self.create_widgets()
        self.view_contacts()

    def create_widgets(self):
        # --- FORM ---
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Name").grid(row=0, column=0)
        tk.Entry(frame, textvariable=self.name_var).grid(row=0, column=1)

        tk.Label(frame, text="Phone").grid(row=1, column=0)
        tk.Entry(frame, textvariable=self.phone_var).grid(row=1, column=1)

        tk.Label(frame, text="Email").grid(row=2, column=0)
        tk.Entry(frame, textvariable=self.email_var).grid(row=2, column=1)

        tk.Label(frame, text="Address").grid(row=3, column=0)
        tk.Entry(frame, textvariable=self.address_var).grid(row=3, column=1)

        # --- BUTTONS ---
        tk.Button(frame, text="Add Contact", command=self.add_contact).grid(row=4, column=0, pady=10)
        tk.Button(frame, text="Update Contact", command=self.update_contact).grid(row=4, column=1)
        tk.Button(frame, text="Delete Contact", command=self.delete_contact).grid(row=5, column=0)
        tk.Button(frame, text="Clear Fields", command=self.clear_fields).grid(row=5, column=1)

        # --- SEARCH ---
        tk.Entry(self.root, textvariable=self.search_var, width=30).pack(pady=5)
        tk.Button(self.root, text="Search", command=self.search_contact).pack()

        # --- CONTACT LIST ---
        self.tree = ttk.Treeview(self.root, columns=("Name", "Phone"), show='headings')
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)
        self.tree.bind("<ButtonRelease-1>", self.load_selected)

    def add_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()

        if not name or not phone:
            messagebox.showwarning("Input Error", "Name and Phone are required!")
            return

        try:
            cursor.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
                           (name, phone, email, address))
            conn.commit()
            messagebox.showinfo("Success", "Contact added!")
            self.view_contacts()
            self.clear_fields()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Phone number already exists.")

    def view_contacts(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        cursor.execute("SELECT name, phone FROM contacts")
        for contact in cursor.fetchall():
            self.tree.insert("", tk.END, values=contact)

    def search_contact(self):
        keyword = self.search_var.get()
        if not keyword:
            self.view_contacts()
            return

        for row in self.tree.get_children():
            self.tree.delete(row)

        cursor.execute("SELECT name, phone FROM contacts WHERE name LIKE ? OR phone LIKE ?", 
                       (f"%{keyword}%", f"%{keyword}%"))
        for contact in cursor.fetchall():
            self.tree.insert("", tk.END, values=contact)

    def load_selected(self, event):
        selected = self.tree.focus()
        values = self.tree.item(selected, 'values')
        if not values:
            return

        cursor.execute("SELECT * FROM contacts WHERE name=? AND phone=?", values)
        contact = cursor.fetchone()
        if contact:
            self.name_var.set(contact[1])
            self.phone_var.set(contact[2])
            self.email_var.set(contact[3])
            self.address_var.set(contact[4])

    def update_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()

        cursor.execute("SELECT id FROM contacts WHERE phone = ?", (phone,))
        result = cursor.fetchone()
        if not result:
            messagebox.showerror("Error", "Contact not found!")
            return

        cursor.execute("UPDATE contacts SET name=?, email=?, address=? WHERE phone=?",
                       (name, email, address, phone))
        conn.commit()
        messagebox.showinfo("Updated", "Contact updated successfully.")
        self.view_contacts()

    def delete_contact(self):
        phone = self.phone_var.get()
        cursor.execute("DELETE FROM contacts WHERE phone = ?", (phone,))
        conn.commit()
        messagebox.showinfo("Deleted", "Contact deleted.")
        self.view_contacts()
        self.clear_fields()

    def clear_fields(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.address_var.set("")
        self.search_var.set("")

# --- RUN APP ---
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
