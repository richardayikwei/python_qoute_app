import flet as ft
import random
from statistical_def import definitions

def main(page: ft.Page):
    page.title = "Definition of the Day"
    page.window_maximized = False     # disables full screen
    page.window_width = 400
    page.window_height = 250
    page.window_resizable = False
    page.window_always_on_top = True
    page.window_center = True

    definition_text = ft.Text("", size=16, text_align=ft.TextAlign.CENTER, selectable=True)
    term_text = ft.Text("", italic=True, size=12, text_align=ft.TextAlign.CENTER)

    def get_new_definition(e=None):
        term, definition = random.choice(list(definitions.items()))
        definition_text.value = f'"{definition}"'
        term_text.value = f"- {term}"
        page.update()

    next_button = ft.ElevatedButton("Next Quote", on_click=get_new_definition)

    page.add(
        ft.Column(
            [definition_text, term_text, next_button],
            spacing=20,
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    get_new_definition()

# Use desktop window mode
ft.app(target=main, view=ft.FLET_APP)
