import tkinter as tk
import random

#Place your quote in the bracket sperated by a comma and in quotes
quotes = {
   'Robert Chang' :'Looking back at my own academic and professional career so far, many times in the past I self-censored my questions because I did not want to appear incapable. However, over time I realized that this attitude was rather detrimental — in the long run, most instances of self-censorship are missed opportunities for learning rather than shame.'
}

author, quote = random.choice(list(quotes.items()))

# Create window
root = tk.Tk()
root.attributes('-topmost', True) 
root.title("Quote of the Day")
root.geometry("400x200")
root.resizable(False, False)

# Display quote
quote_label = tk.Label(root, text=f'"{quote}"', wraplength=380, justify="center", font=("Arial", 12))
quote_label.pack(pady=20)

# Display author
author_label = tk.Label(root, text=f"- {author}", font=("Arial", 10, "italic"))
author_label.pack()

# Run the app
root.mainloop()