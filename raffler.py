import tkinter as tk
from tkinter import messagebox, scrolledtext
import random

def pick_winners():
    # Retrieve and clean the input names
    names = names_input.get("1.0", tk.END).strip()
    students = [name.strip() for name in names.replace(',', '\n').splitlines() if name.strip()]
    
    # Get the number of winners and validate the input
    try:
        number_of_winners = int(winners_input.get())
        if number_of_winners <= 0 or number_of_winners > len(students):
            raise ValueError
    except ValueError:
        messagebox.showwarning("Invalid Input", f"Please enter a valid number of winners (1-{len(students)}).")
        return

    # Randomly select the winners
    winners = random.sample(students, number_of_winners)
    result = "\n".join(f"{i + 1}. {winner}" for i, winner in enumerate(winners))
    
    # Display the winners in the output text area
    output_text.config(state='normal')  # Enable text area for editing
    output_text.delete('1.0', tk.END)   # Clear previous results
    output_text.insert(tk.END, f"Winning Names:\n{result}")
    output_text.config(state='disabled') # Disable text area for editing to prevent user modification

# Set up the main application window
root = tk.Tk()
root.title("Raffle Program")
root.geometry("500x500")
root.resizable(False, False)  # Disable window resizing

# Input section for names
tk.Label(root, text="Enter names (separated by lines or commas):").pack(pady=5)
names_input = scrolledtext.ScrolledText(root, height=10, width=60)
names_input.pack(pady=5)

# Input section for the number of winners
tk.Label(root, text="Number of winners:").pack(pady=5)
winners_input = tk.Entry(root, width=10)
winners_input.pack(pady=5)

# Button to trigger picking winners
tk.Button(root, text="Pick Winners", command=pick_winners).pack(pady=10)

# Output section for displaying the winners
output_text = scrolledtext.ScrolledText(root, height=10, width=60, state='disabled')
output_text.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
