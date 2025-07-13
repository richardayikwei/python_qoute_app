import tkinter as tk
import random
from statistical_def import definitions

# Function to update quote
def get_new_definition():
    term, definition = random.choice(list(definitions.items()))
    definition_label.config(text=f'"{definition}"')
    term_label.config(text=f"- {term}")

# Create window
root = tk.Tk()
root.attributes('-topmost', True) 
root.title("Definition of the Day")
root.geometry("400x200")
root.resizable(False, False)


# Display definition
definition_label = tk.Label(root, text="", wraplength=380, justify="center", font=("Segoe UI", 12))
root.geometry("")  
definition_label.pack(pady=20)

#button
next_button = tk.Button(root, text="Next Quote", command=get_new_definition)
next_button.pack()


# Display term
term_label = tk.Label(root, text="", font=("Arial", 10, "italic"))
term_label.pack()

# Show the first quote
get_new_definition()

# Run the app
root.mainloop()