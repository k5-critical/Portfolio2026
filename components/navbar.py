import flet as ft


def navbar(page):
    return ft.Row(
        controls=[
            ft.ElevatedButton("Home", on_click=lambda e: page.go("/")),
            ft.ElevatedButton("Timeline", on_click=lambda e: page.go("/timeline")),
            ft.ElevatedButton("MATLAB", on_click=lambda e: page.go("/matlab")),
            ft.ElevatedButton("Blog", on_click=lambda e: page.go("/blog")),
            ft.ElevatedButton("GitHub", on_click=lambda e: page.go("/github")),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )