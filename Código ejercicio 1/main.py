import flet as ft
import math


def main(page: ft.Page):
    page.title = "Calculadora TAP"
    page.window_width = 300
    page.window_height = 500
    page.window_resizable = False
    page.padding = 20

    # Usamos lista para poder modificar el valor sin nonlocal
    expression = [""]

    display = ft.Text(
        value="0",
        size=32,
        text_align=ft.TextAlign.RIGHT,
        width=260
    )

    def update_display():
        display.value = expression[0] if expression[0] else "0"
        page.update()

    def button_click(e):
        value = e.control.data

        if value == "C":
            expression[0] = ""

        elif value == "=":
            try:
                exp = expression[0].replace("^", "**")
                result = str(eval(exp))
                expression[0] = result
            except:
                expression[0] = "Error"

        elif value == "√":
            try:
                result = str(math.sqrt(float(expression[0])))
                expression[0] = result
            except:
                expression[0] = "Error"

        elif value == "+/-":
            if expression[0]:
                if expression[0].startswith("-"):
                    expression[0] = expression[0][1:]
                else:
                    expression[0] = "-" + expression[0]

        else:
            if expression[0] == "Error":
                expression[0] = ""
            expression[0] += value

        update_display()

    buttons = [
        ["C", "√", "^", "/"],
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["+/-", "0", ".", "="],
    ]

    grid = ft.Column(spacing=10)

    for row in buttons:
        button_row = ft.Row(spacing=10)
        for text in row:
            button_row.controls.append(
                ft.Button(
                    text,
                    data=text,   # ← usamos data (mejor práctica)
                    expand=1,
                    height=50,
                    on_click=button_click
                )
            )
        grid.controls.append(button_row)

    page.add(
        ft.Column(
            controls=[
                ft.Container(
                    content=display,
                    bgcolor=ft.Colors.BLACK12,
                    padding=10,
                    border_radius=8,
                ),
                grid
            ],
            spacing=20
        )
    )


ft.run(main)
