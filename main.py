import tkinter as tk
import random
import json

with open('quotes.json','r',encoding="utf-8") as q:
    quotes = json.load(q)

author, quote = random.choice(list(quotes.items()))

# Create window
root = tk.Tk()
root.attributes('-topmost', True) 
root.title("Quote of the Day")
root.geometry("400x200")
root.resizable(False, False)

# Display quote
quote_label = tk.Label(root, text=f'"{quote}"', wraplength=380, justify="center", font=("Segoe UI", 12))
root.geometry("")  
quote_label.pack(pady=20)

# Display author
author_label = tk.Label(root, text=f"- {author}", font=("Arial", 10, "italic"))
author_label.pack()

# Run the app
root.mainloop()