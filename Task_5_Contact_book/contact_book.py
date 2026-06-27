import tkinter as tk
from tkinter import messagebox

# ==========================================
# 1. CORE DATA LOGIC (DATABASE & CRUD)
# ==========================================

# Active list array to temporarily store contact objects
contact_database = [
    {"name": "Anjali Parashar", "phone": "9100000000", "email": "anjali@example.com", "address": "Bhopal"}
]

def add_contact():
    """Validates input fields and saves a new contact record."""
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    # Form field validation check
    if not name or not phone:
        messagebox.showwarning("Missing Information", "Name and Phone Number fields are strictly required!")
        return

    # Duplicate check using the phone number as a unique key
    for contact in contact_database:
        if contact['phone'] == phone:
            messagebox.showwarning("Data Conflict", "A contact record with this phone number already exists.")
            return

    # Append to local data array
    new_node = {"name": name, "phone": phone, "email": email, "address": address}
    contact_database.append(new_node)
    
    messagebox.showinfo("Success", f"Contact record for '{name}' has been successfully saved.")
    clear_input_fields()
    refresh_contact_listview()

def refresh_contact_listview(filter_query=""):
    """Wipes listbox structure and renders live contacts based on search query."""
    contact_listbox.delete(0, tk.END)
    query = filter_query.lower().strip()
    
    for item in contact_database:
        # Check if query matches name or phone
        if query in item['name'].lower() or query in item['phone']:
            display_string = f" 👤  {item['name']}   │   📞  {item['phone']}"
            contact_listbox.insert(tk.END, display_string)

def search_contacts(event=None):
    """Filters directory records live while typing."""
    query = search_entry.get()
    refresh_contact_listview(query)

def load_selected_contact(event=None):
    """Loads selected item details from listbox back into input fields."""
    try:
        selected_index = contact_listbox.curselection()[0]
        selected_text = contact_listbox.get(selected_index)
        
        # Isolate phone number from the string layout
        extracted_phone = selected_text.split("│")[1].replace("📞", "").strip()
        
        for item in contact_database:
            if item['phone'] == extracted_phone:
                clear_input_fields()
                name_entry.insert(0, item['name'])
                phone_entry.insert(0, item['phone'])
                email_entry.insert(0, item['email'])
                address_entry.insert(0, item['address'])
                
                # Lock phone field modifications to preserve unique key
                phone_entry.configure(state="disabled")
                break
    except IndexError:
        pass # Handle blank spaces gracefully

def update_contact():
    """Overrides existing details for the loaded unique record."""
    phone_entry.configure(state="normal")
    target_phone = phone_entry.get().strip()
    
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if not name:
        messagebox.showwarning("Validation Alert", "Name field cannot be left blank during an update!")
        return

    for item in contact_database:
        if item['phone'] == target_phone:
            item['name'] = name
            item['email'] = email
            item['address'] = address
            messagebox.showinfo("Success", "Contact details updated successfully.")
            clear_input_fields()
            refresh_contact_listview()
            return
            
    messagebox.showerror("Error", "Failed to update contact. Target key not found.")

def delete_contact():
    """Permanently flushes targeted record out of database list array."""
    phone_entry.configure(state="normal")
    target_phone = phone_entry.get().strip()

    if not target_phone:
        messagebox.showwarning("Selection Alert", "Please select a profile from the directory list first!")
        return

    for idx, item in enumerate(contact_database):
        if item['phone'] == target_phone:
            confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to permanently delete '{item['name']}' from directory storage?")
            if confirm:
                contact_database.pop(idx)
                messagebox.showinfo("Deleted", "Contact record deleted from storage archives.")
                clear_input_fields()
                refresh_contact_listview()
            return

def clear_input_fields():
    """Clears inputs out of the entry sheet and resets field states."""
    phone_entry.configure(state="normal")
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# ==========================================
# 2. DESIGN STUDIO WORKSPACE CANVAS VIEW
# ==========================================
root = tk.Tk()
root.title("Professional Contact Directory")
root.geometry("840x540")

# Premium High-End Palette System
CLR_CANVAS = "#f8fafc"       # Soft off-white linen background
CLR_CARD = "#ffffff"         # Pure solid white containers
CLR_TEXT_DARK = "#0f172a"    # Deep slate gray font
CLR_MUTED = "#64748b"        # Elegant taupe gray subtitles

# Premium Action Shades
COLOR_SAVE = "#10b981"       # Professional Mint Green
COLOR_UPDATE = "#4f46e5"     # Premium Deep Indigo Blue
COLOR_DELETE = "#ef4444"     # Sharp Crimson Red

root.configure(bg=CLR_CANVAS)

# --- HEADER TITLE BLOCK ---
title_lbl = tk.Label(root, text="CONTACT DIRECTORY MANAGER", font=("Segoe UI", 15, "bold"), bg=CLR_CANVAS, fg=CLR_TEXT_DARK)
title_lbl.pack(pady=(25, 5), padx=35, anchor="w")

# Split Panel Container Frame
workspace_box = tk.Frame(root, bg=CLR_CANVAS)
workspace_box.pack(padx=35, pady=10, fill="both", expand=True)
workspace_box.columnconfigure(0, weight=4) # Left side Form panel
workspace_box.columnconfigure(1, weight=5) # Right side List viewing screen

# ==========================================
# LEFT SIDE PANEL: PROFILE ENTRY SHEET
# ==========================================
form_card = tk.Frame(workspace_box, bg=CLR_CARD, highlightthickness=1, highlightbackground="#e2e8f0")
form_card.grid(row=0, column=0, sticky="nsew", padx=(0, 15), pady=10)

form_title = tk.Label(form_card, text="Contact Specifications Form", font=("Segoe UI", 11, "bold"), bg=CLR_CARD, fg=CLR_TEXT_DARK)
form_title.pack(anchor="w", padx=20, pady=(15, 10))

def create_form_entry(label_text):
    """Layout formatting standard automation sequence for inputs"""
    lbl = tk.Label(form_card, text=label_text, font=("Segoe UI", 9, "bold"), bg=CLR_CARD, fg=CLR_MUTED)
    lbl.pack(anchor="w", padx=20, pady=(6, 2))
    entry = tk.Entry(form_card, font=("Segoe UI", 10), bd=0, bg="#f1f5f9", fg=CLR_TEXT_DARK, highlightthickness=1, highlightbackground="#e2e8f0", insertbackground=CLR_TEXT_DARK)
    entry.pack(fill="x", padx=20, ipady=6)
    return entry

name_entry = create_form_entry("Full Name *")
phone_entry = create_form_entry("Phone Number *")
email_entry = create_form_entry("Email Address")
address_entry = create_form_entry("Address(Optional)")

# --- GRID ACTION INTERACTION LAYOUT ---
actions_box = tk.Frame(form_card, bg=CLR_CARD)
actions_box.pack(fill="x", padx=20, pady=20)
actions_box.columnconfigure(0, weight=1)
actions_box.columnconfigure(1, weight=1)

btn_style = {"font": ("Segoe UI", 9, "bold"), "fg": "#ffffff", "bd": 0, "cursor": "hand2"}

add_btn = tk.Button(actions_box, text="SAVE CONTACT", bg=COLOR_SAVE, activebackground="#059669", activeforeground="#ffffff", command=add_contact, **btn_style)
add_btn.grid(row=0, column=0, sticky="nsew", padx=(0, 4), ipady=11)

update_btn = tk.Button(actions_box, text="UPDATE CHANGES", bg=COLOR_UPDATE, activebackground="#3730a3", activeforeground="#ffffff", command=update_contact, **btn_style)
update_btn.grid(row=0, column=1, sticky="nsew", padx=(4, 0), ipady=11)

delete_btn = tk.Button(form_card, text="DELETE CONTACT PROFILE", bg=COLOR_DELETE, activebackground="#b91c1c", activeforeground="#ffffff", command=delete_contact, **btn_style)
delete_btn.pack(fill="x", padx=20, pady=(0, 15), ipady=11)

# ==========================================
# RIGHT SIDE PANEL: LIVE SYSTEM REGISTER
# ==========================================
directory_card = tk.Frame(workspace_box, bg=CLR_CARD, highlightthickness=1, highlightbackground="#e2e8f0")
directory_card.grid(row=0, column=1, sticky="nsew", padx=(15, 0), pady=10)

# Real-Time Search Stream Bar
search_lbl = tk.Label(directory_card, text="Search Saved Directory 🔍", font=("Segoe UI", 9, "bold"), bg=CLR_CARD, fg=CLR_MUTED)
search_lbl.pack(anchor="w", padx=20, pady=(15, 2))

search_entry = tk.Entry(directory_card, font=("Segoe UI", 10), bd=0, bg="#f1f5f9", fg=CLR_TEXT_DARK, highlightthickness=1, highlightbackground="#e2e8f0")
search_entry.pack(fill="x", padx=20, ipady=6)
search_entry.bind("<KeyRelease>", search_contacts)

# Main Viewing Area Node
list_lbl = tk.Label(directory_card, text="Live Active Registry", font=("Segoe UI", 9, "bold"), bg=CLR_CARD, fg=CLR_MUTED)
list_lbl.pack(anchor="w", padx=20, pady=(12, 4))

contact_listbox = tk.Listbox(
    directory_card, font=("Segoe UI", 10), bd=0, bg="#ffffff", fg=CLR_TEXT_DARK,
    highlightthickness=1, highlightbackground="#e2e8f0", selectbackground="#e0f2fe", selectforeground=COLOR_UPDATE
)
contact_listbox.pack(fill="both", expand=True, padx=20, pady=(0, 15))
contact_listbox.bind("<<ListboxSelect>>", load_selected_contact)

# Synchronize database view on launch
refresh_contact_listview()

root.mainloop()