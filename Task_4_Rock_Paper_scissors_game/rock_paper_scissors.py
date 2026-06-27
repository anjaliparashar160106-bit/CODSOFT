import tkinter as tk
import random
import time

# 1. CORE ARCHITECTURE & COMPUTATIONAL LOGIC

def play_round(user_choice):
    """Processes user vs computer game matrix and triggers dynamic visual feedback loops."""
    global user_score, computer_score
    
    # Simple list configuration for automation tracking
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    # 1. Visual Matrix Animation Effect (Simulating computer computing data)
    choices_label.configure(fg="#ffb703", text="SYSTEM INTERCEPTING INBOUND CHOICE...")
    root.update()
    time.sleep(0.15) # Subtle micro-delay for arcade processing sensation
    
    choices_var.set(f"PLAYER WEAPON: [ {user_choice.upper()} ]  ⚡  CPU SYSTEM: [ {computer_choice.upper()} ]")

    # 2. Evaluation Logic Tree Setup
    if user_choice == computer_choice:
        result_var.set("ROUND TIE! 🤝 PARALLEL SEQUENCES MATCHED")
        result_frame.configure(bg="#ffb703") # Cyber Yellow flash boundary
        result_label.configure(bg="#ffb703", fg="#090d16")
        
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        
        user_score += 1
        result_var.set("VICTORY! 🔥 CPU MEMORY MATRIX CORE BREACHED")
        result_frame.configure(bg="#39ff14") # Neon Ghost Green flash boundary
        result_label.configure(bg="#39ff14", fg="#090d16")
    else:
        computer_score += 1
        result_var.set("DEFEAT! 💀 SYSTEM ARCHITECTURE INTERCEPTED YOU")
        result_frame.configure(bg="#ff0055") # Crimson Cyber Pink flash boundary
        result_label.configure(bg="#ff0055", fg="#f8fafc")

    # Update active scoreboards instantly
    score_var.set(f"PLAYER: {user_score}  ◈  CPU: {computer_score}")


def reset_game():
    """Flushes active integer scores and restores base game interface parameters."""
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_var.set("PLAYER: 0  ◈  CPU: 0")
    choices_var.set("READY FOR COMBAT: LAUNCH ROUND 1")
    result_var.set("CHOOSE YOUR WEAPON DISPATCH ENTRY")
    
    # Restore original neon dark frame states
    result_frame.configure(bg="#1a233a")
    result_label.configure(bg="#1a233a", fg="#00f0ff")

# 2. CYBERPUNK ARCADE UI FRAMEWORK

root = tk.Tk()
root.title("NEON ARCADE // CORE_RPS")
root.geometry("480x560")

# Retro High-Visibility Style Guide Constants
COLOR_BG = "#090d16"         # Clean Void Obsidian Black
COLOR_SURROUND = "#1a233a"   # Deep Tech Cobalt Frame Box
NEON_CYAN = "#00f0ff"        # Electric Cyan Print Stream
NEON_PINK = "#ff007f"        # Cyber Hot Pink Accent Title
TEXT_WHITE = "#f8fafc"       # Bright Core Off-White

root.configure(bg=COLOR_BG)

user_score = 0
computer_score = 0

score_var = tk.StringVar(value="PLAYER: 0  ◈  CPU: 0")
choices_var = tk.StringVar(value="READY FOR COMBAT: LAUNCH ROUND 1")
result_var = tk.StringVar(value="CHOOSE YOUR WEAPON DISPATCH ENTRY")


# 3. INTERACTIVE LAYOUT GENERATION STREAMS


# --- TOP NEON HEADER TITLE ---
main_header = tk.Label(root, text="▲ ARCADE MATRIX ENGINE ▲", font=("Courier New", 16, "bold"), bg=COLOR_BG, fg=NEON_PINK)
main_header.pack(pady=(25, 10))

# --- FLOATING SCOREBOARD CORE ---
scoreboard_panel = tk.Frame(root, bg=COLOR_SURROUND, bd=0, highlightthickness=2, highlightbackground=NEON_CYAN)
scoreboard_panel.pack(pady=15, padx=30, fill="x")

score_label = tk.Label(scoreboard_panel, textvariable=score_var, font=("Consolas", 18, "bold"), bg=COLOR_SURROUND, fg=NEON_CYAN)
score_label.pack(pady=14)

# --- DYNAMIC ACTION STATUS PANEL ---
choices_label = tk.Label(root, textvariable=choices_var, font=("Courier New", 10, "bold"), bg=COLOR_BG, fg="#8a99ad")
choices_label.pack(pady=(20, 5))

# Dynamic status bounding box container
result_frame = tk.Frame(root, bg=COLOR_SURROUND, bd=0, highlightthickness=1, highlightbackground="#2d3d5a")
result_frame.pack(pady=5, padx=30, fill="x")

result_label = tk.Label(result_frame, textvariable=result_var, font=("Segoe UI", 12, "bold"), bg=COLOR_SURROUND, fg=NEON_CYAN, justify="center", wraplength=400)
result_label.pack(pady=15, padx=10)

# --- INTERACTIVE WEAPON CONTROLS GRID ---
weapons_box = tk.Frame(root, bg=COLOR_BG)
weapons_box.pack(pady=30, padx=30, fill="x")

for col_position in range(3):
    weapons_box.columnconfigure(col_position, weight=1)

# Schema Matrix configuration details: (Text, Data Input Token, Normal Color, Hover Flash Color)
button_blueprints = [
    ("ROCK 🪨", "Rock", "#34495e", "#5d6d7e"),
    ("PAPER 📄", "Paper", "#16a085", "#1abc9c"),
    ("SCISSORS ✂️", "Scissors", "#8e44ad", "#9b59b6")
]

# Spawn engine dynamically with inline callback mappings
for index, (text_label, command_token, base_hex, hover_hex) in enumerate(button_blueprints):
    action_btn = tk.Button(
        weapons_box, text=text_label, font=("Segoe UI", 12, "bold"),
        bg=base_hex, fg=TEXT_WHITE, bd=0, cursor="hand2",
        activebackground=hover_hex, activeforeground=TEXT_WHITE,
        command=lambda t=command_token: play_round(t)
    )
    action_btn.grid(row=0, column=index, sticky="nsew", padx=6, ipady=18)
    
    # Native animation hooks to capture mouse tracking
    action_btn.bind("<Enter>", lambda e, h=hover_hex, b=action_btn: b.configure(bg=h))
    action_btn.bind("<Leave>", lambda e, o=base_hex, b=action_btn: b.configure(bg=o))

# --- SYSTEM RESET SYSTEM UTILITY ---
system_reset_btn = tk.Button(
    root, text="⚡ REBOOT MAIN INTERFACE MATCH ⚡", font=("Courier New", 10, "bold"),
    bg="#2c3e50", fg="#bdc3c7", bd=0, cursor="hand2",
    activebackground="#e74c3c", activeforeground=TEXT_WHITE,
    command=reset_game
)
system_reset_btn.pack(side="bottom", fill="x", padx=30, pady=35, ipady=12)

root.mainloop()

