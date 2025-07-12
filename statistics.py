import tkinter as tk
import random
from statistical_def import definitions

term, definition = random.choice(list(definitions.items()))

# Create window
root = tk.Tk()
root.attributes('-topmost', True) 
root.title("definition of the Day")
root.geometry("400x200")
root.resizable(False, False)

# Display definition
definition_label = tk.Label(root, text=f'"{definition}"', wraplength=380, justify="center", font=("Segoe UI", 12))
root.geometry("")  
definition_label.pack(pady=20)

# Display term
term_label = tk.Label(root, text=f"- {term}", font=("Arial", 10, "italic"))
term_label.pack()

# Run the app
root.mainloop()