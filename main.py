import flet as ft
import random
from quotes import quotes  # quotes = {author: quote}

def main(page: ft.Page):
    # Window settings
    page.title = "Quote of the Day"
    page.window_width = 400
    page.window_height = 600
    page.window_maximized = False
    page.window_resizable = False
    page.window_always_on_top = True
    page.window_center = True

    # UI Elements
    quote_text = ft.Text("", size=16, text_align=ft.TextAlign.CENTER, selectable=True)
    author_text = ft.Text("", italic=True, size=12, text_align=ft.TextAlign.CENTER)

    # Function to load a new quote
    def get_new_quote(e=None):
        author, quote = random.choice(list(quotes.items()))
        quote_text.value = f'"{quote}"'
        author_text.value = f"- {author}"
        page.update()

    # Button
    next_button = ft.ElevatedButton("Next Quote", on_click=get_new_quote)

    # Layout
    page.add(
        ft.Column(
            [quote_text, author_text, next_button],
            spacing=20,
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    # First quote
    get_new_quote()

# Launch in native desktop window mode
ft.app(target=main, view=ft.FLET_APP)
