import tkinter as tk
import random
from quotes import quotes

# Function to update quote
def get_new_quote():
    author, quote = random.choice(list(quotes.items()))
    quote_label.config(text=f'"{quote}"')
    author_label.config(text=f"- {author}")

# Create window
root = tk.Tk()
root.attributes('-topmost', True) 
root.title("Quote of the Day")
root.geometry("400x200")
root.resizable(False, False)

# Display quote
quote_label = tk.Label(root, text="", wraplength=380, justify="center", font=("Segoe UI", 12))
root.geometry("")  
quote_label.pack(pady=20)

#button
next_button = tk.Button(root, text="Next Quote", command=get_new_quote)
next_button.pack()

# Display author
author_label = tk.Label(root, text="", font=("Arial", 10, "italic"))
author_label.pack()

# Show the first quote
get_new_quote()

# Run the app
root.mainloop()