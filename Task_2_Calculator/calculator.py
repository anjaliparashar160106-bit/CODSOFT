import tkinter as tk
from tkinter import messagebox

# Global variable to track the mathematical operations sequence
expression = ""

# Initializing the main application workspace root node
root = tk.Tk()
root.title("CodSoft Calculator Pro")
root.geometry("360x480")
root.configure(bg="#0f172a")

# Dynamic string variable mapped to track and broadcast inputs to the display widget
equation_var = tk.StringVar()

# --- HIGH-CONTRAST DIGITAL UI SCREEN ---
display_screen = tk.Entry(
    root, 
    textvariable=equation_var, 
    font=("Segoe UI", 24, "bold"), 
    bd=0, 
    bg="#1e293b", 
    fg="#f8fafc", 
    justify="right",
    highlightthickness=1,
    highlightbackground="#334155"
)
display_screen.pack(pady=25, padx=20, ipady=15, fill="both")


# CORE BACKEND CALCULATION ENGINES

def press_button(num):
    """Appends numerical digits or operations characters to the global expression evaluation string."""
    global expression
    expression = expression + str(num)
    equation_var.set(expression)  # Push current string to dynamic UI display element

def clear_screen():
    """Resets the dynamic display variable stream and flushes calculation history from volatile storage."""
    global expression
    expression = ""
    equation_var.set("")

def equal_press():
    """Parses structural text inputs via logical string evaluation and manages unexpected mathematical operations."""
    global expression
    try:
        # Utilizing Python's built-in evaluation parser to process mathematical sequences
        total = str(eval(expression))
        equation_var.set(total)
        expression = total  # Preserve final evaluation block for continuous computation runs
    except ZeroDivisionError:
        messagebox.showwarning("Math Error", "Division by zero is mathematically undefined!")
        clear_screen()
    except Exception:
        messagebox.showwarning("Execution Error", "Syntax structure error in mathematical sequence!")
        clear_screen()


# 3. INTERACTIVE TOUCHPAD COMPONENT GRID

# Component frame to isolate control grid metrics neatly
button_frame = tk.Frame(root, bg="#0f172a")
button_frame.pack(padx=20, pady=5, fill="both", expand=True)

# Grid coordinate scaling rule configuration sets
for i in range(4):
    button_frame.rowconfigure(i, weight=1)
    button_frame.columnconfigure(i, weight=1)

# Flat matrix UI blueprint sequence: (Text Token, Row Coordinate, Column Index, Accent Color Block)
buttons_matrix = [
    ('7', 0, 0, '#334155'), ('8', 0, 1, '#334155'), ('9', 0, 2, '#334155'), ('/', 0, 3, '#0284c7'),
    ('4', 1, 0, '#334155'), ('5', 1, 1, '#334155'), ('6', 1, 2, '#334155'), ('*', 1, 3, '#0284c7'),
    ('1', 2, 0, '#334155'), ('2', 2, 1, '#334155'), ('3', 2, 2, '#334155'), ('-', 2, 3, '#0284c7'),
    ('C', 3, 0, '#ef4444'), ('0', 3, 1, '#334155'), ('=', 3, 2, '#10b981'), ('+', 3, 3, '#0284c7'),
]

# Structural iteration to spawn uniform interactive button interfaces dynamically
for (text, row, col, bg_color) in buttons_matrix:
    # Evaluating component execution mapping parameters
    if text == '=':
        action_command = equal_press
    elif text == 'C':
        action_command = clear_screen
    else:
        # Isolated runtime tracking mapping setup to prevent immediate initialization crashes
        action_command = lambda t=text: press_button(t)

    btn = tk.Button(
        button_frame, 
        text=text, 
        font=("Segoe UI", 16, "bold"), 
        bg=bg_color, 
        fg="#f8fafc", 
        bd=0, 
        activebackground="#475569", 
        activeforeground="#f8fafc",
        cursor="hand2",
        command=action_command
    )
    btn.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)

# Execute continuous window thread application processes loop
root.mainloop()