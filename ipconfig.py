import subprocess
import tkinter as tk
from tkinter import scrolledtext

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output_text.delete(1.0, tk.END)  # Clear previous output
        output_text.insert(tk.END, result.stdout)
    except Exception as e:
        output_text.insert(tk.END, f"Error: {e}")

def create_button(frame, text, command):
    return tk.Button(frame, text=text, bg="lime", fg="black", command=command, font=("Arial", 12), relief="raised", borderwidth=3)

# Initialize the Tkinter window
root = tk.Tk()
root.title("IPConfig GUI")
root.configure(bg="black")
root.geometry("800x600")

# Create a frame for buttons
button_frame = tk.Frame(root, bg="black")
button_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

# Create a scrolled text widget for output
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="black", fg="lime", font=("Arial", 10))
output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Create buttons for various ipconfig commands
create_button(button_frame, "Display All IP Configuration", lambda: run_command("ipconfig")).pack(side=tk.LEFT, padx=10)
create_button(button_frame, "Detailed IP Configuration", lambda: run_command("ipconfig /all")).pack(side=tk.LEFT, padx=10)
create_button(button_frame, "Release IP Address", lambda: run_command("ipconfig /release")).pack(side=tk.LEFT, padx=10)
create_button(button_frame, "Renew IP Address", lambda: run_command("ipconfig /renew")).pack(side=tk.LEFT, padx=10)
create_button(button_frame, "Flush DNS Cache", lambda: run_command("ipconfig /flushdns")).pack(side=tk.LEFT, padx=10)
create_button(button_frame, "Display DNS Cache", lambda: run_command("ipconfig /displaydns")).pack(side=tk.LEFT, padx=10)
create_button(button_frame, "Register DNS", lambda: run_command("ipconfig /registerdns")).pack(side=tk.LEFT, padx=10)
create_button(button_frame, "Show Network Adapters", lambda: run_command("ipconfig /allcompartments /all")).pack(side=tk.LEFT, padx=10)

# Start the main loop
root.mainloop()
