import tkinter as tk
from tkinter import messagebox

# 1. APPLICATION WINDOW SETUP

root = tk.Tk()
root.title("CodSoft Todo list")
root.geometry("400x450")

# ---- INPUT BOX ----
# Entry widget for user to input new tasks
task_entry = tk.Entry(root, font=("Arial", 14), width=25)
task_entry.pack(pady=15)

# ---- LISTBOX CONTAINER ----
# Display container to hold and manage the task nodes
task_listbox = tk.Listbox(root, font=("Arial", 12), width=32, height=12)
task_listbox.pack(pady=10)


# 2. BACKEND LOGIC FUNCTIONS


# Function to extract text from entry field and append to listbox
def add_task_gui():
    task = task_entry.get()
    if task.strip() == '':
        messagebox.showwarning("Warning", "Task cannot be empty!")
    else:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Function to permanently remove the selected task node
def delete_task_gui():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task before deleting it!")

# Function to append completion checkmark to the selected task
def mark_task_done_gui():
    try:
        selected_index = task_listbox.curselection()[0]
        task_text = task_listbox.get(selected_index)
        if "✔️" not in task_text:
            new_text = f"{task_text} ✔️"
            task_listbox.delete(selected_index)
            task_listbox.insert(selected_index, new_text)
            task_listbox.itemconfig(selected_index, fg="gray")
        else:
            messagebox.showinfo("Info", "This task has already been completed!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task before marking it completed!")


# 3. UI ACTION BUTTON INTERFACE


# Button configuration to trigger task insertion
add_button = tk.Button(root, text="Add Task", font=("Arial", 12), bg="#4CAF50", fg="white", width=22, command=add_task_gui)
add_button.pack(pady=5)

# Button configuration to trigger status modification
mark_button = tk.Button(root, text="Mark task as Done", font=("Arial", 12), bg="purple", fg="white", width=22, command=mark_task_done_gui)
mark_button.pack(pady=5)

# Button configuration to trigger task termination
delete_button = tk.Button(root, text="Delete Selected Task", font=("Arial", 12), bg="#f44336", fg="white", width=22, command=delete_task_gui)
delete_button.pack(pady=5)

# Start application event orchestration loop
root.mainloop()