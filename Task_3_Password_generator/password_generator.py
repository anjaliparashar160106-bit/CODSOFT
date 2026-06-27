import tkinter as tk
from tkinter import messagebox
import random
import string

# 1. CORE PASSWORD GENERATION LOGIC

def generate_password():
    """Assembles character pools based on complexity checkboxes and generates a randomized secure token."""
    try:
        length_str = length_entry.get().strip()
        if not length_str:
            messagebox.showwarning("Input Error", "Please specify the password length!")
            return
            
        length = int(length_str)
        if length < 4 or length > 32:
            messagebox.showwarning("Range Error", "Password length must be between 4 and 32 characters!")
            return
            
        char_pool = ""
        if uppercase_var.get():
            char_pool += string.ascii_uppercase
        if lowercase_var.get():
            char_pool += string.ascii_lowercase
        if digits_var.get():
            char_pool += string.digits
        if symbols_var.get():
            char_pool += string.punctuation

        if not char_pool:
            messagebox.showwarning("Complexity Error", "Select at least one complexity criteria!")
            return

        generated_token = "".join(random.choice(char_pool) for _ in range(length))
        password_display_var.set(generated_token)
        
    except ValueError:
        messagebox.showwarning("Type Error", "Password length must be a valid integer number!")


# 2. UI CONTAINER AND LAYOUT SETUP 

root = tk.Tk()
root.title("Secure Key Generator")
root.geometry("380x500")

# Uniform Theme Palette Constants
BG_MAIN = "#0f172a"      # Sleek deep slate blue (matches modern IDEs)
TEXT_LIGHT = "#f8fafc"   # Clean off-white
ACCENT_CYAN = "#38bdf8"  # Neon Cyan accent
ACCENT_MINT = "#34d399"  # Mint Green for generated key

root.configure(bg=BG_MAIN)

password_display_var = tk.StringVar()

# --- HEADER TITLE SECTION ---
title_label = tk.Label(root, text="PASSWORD GENERATOR", font=("Segoe UI", 15, "bold"), bg=BG_MAIN, fg=ACCENT_CYAN)
title_label.pack(pady=(25, 15))

# --- CONFIGURATION LAYER ---
# Removed the second background box color to blend completely with the main canvas
config_frame = tk.Frame(root, bg=BG_MAIN)
config_frame.pack(padx=25, pady=5, fill="both", expand=True)

# 1. Length Input Channel Configuration
length_label = tk.Label(config_frame, text="Password Length (4-32)", font=("Segoe UI", 11, "bold"), bg=BG_MAIN, fg=TEXT_LIGHT)
length_label.pack(anchor="w", pady=(10, 5))

length_entry = tk.Entry(
    config_frame, font=("Consolas", 12, "bold"), justify="center", bd=0, 
    bg="#1e293b", fg=TEXT_LIGHT, width=12, insertbackground=TEXT_LIGHT,
    highlightthickness=1, highlightbackground="#334155"
)
length_entry.insert(0, "12")
length_entry.pack(anchor="w", pady=(0, 15), ipady=6)

# 2. Dynamic Variable Mappings
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

# 3. Clean Flat Checkbuttons Layout
chk_style = {
    "font": ("Segoe UI", 10), "bg": BG_MAIN, "fg": "#cbd5e1", 
    "activebackground": BG_MAIN, "activeforeground": ACCENT_CYAN, 
    "selectcolor": "#1e293b", "bd": 0, "highlightthickness": 0
}

tk.Checkbutton(config_frame, text="Include Uppercase Letters (A-Z)", variable=uppercase_var, **chk_style).pack(anchor="w", pady=6)
tk.Checkbutton(config_frame, text="Include Lowercase Letters (a-z)", variable=lowercase_var, **chk_style).pack(anchor="w", pady=6)
tk.Checkbutton(config_frame, text="Include Numerical Digits (0-9)", variable=digits_var, **chk_style).pack(anchor="w", pady=6)
tk.Checkbutton(config_frame, text="Include Special Symbols (@,#,$)", variable=symbols_var, **chk_style).pack(anchor="w", pady=6)

# --- OUTPUT AND ACTION SEGMENT ---
generate_btn = tk.Button(
    root, text="GENERATE SECURE KEY", font=("Segoe UI", 11, "bold"), 
    bg="#0284c7", fg=TEXT_LIGHT, bd=0, cursor="hand2", activebackground="#0369a1", activeforeground=TEXT_LIGHT
)
# Dynamic assignment mapping
generate_btn.configure(command=generate_password)
generate_btn.pack(pady=15, padx=25, fill="x", ipady=10)

output_entry = tk.Entry(
    root, textvariable=password_display_var, font=("Consolas", 14, "bold"), 
    justify="center", bd=0, bg="#1e293b", fg=ACCENT_MINT, 
    highlightthickness=1, highlightbackground="#334155"
)
output_entry.pack(pady=(0, 30), padx=25, fill="x", ipady=12)

root.mainloop()