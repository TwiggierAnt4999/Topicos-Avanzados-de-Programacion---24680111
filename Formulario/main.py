import flet as ft


def main(page: ft.Page):
    page.title = "Formulario"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#e6e1cc"
    page.padding = 50
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

    def campo(label):
        return ft.TextField(
            hint_text=label,
            border=ft.InputBorder.OUTLINE,
            border_width=2,
            border_color="black",
            bgcolor="white",
            color="black",
            hint_style=ft.TextStyle(color="black"),
            height=70,
            text_size=18,
            expand=True,
        )

    nombre = campo("Nombre")
    numero_control = ft.TextField(
        hint_text="Numero de control",
        keyboard_type=ft.KeyboardType.NUMBER,
        border=ft.InputBorder.OUTLINE,
        border_width=2,
        border_color="black",
        bgcolor="white",
        color="black",
        height=70,
        text_size=18,
        expand=True,
        )
    email = campo("Email")
    carrera = campo("Carrera")
    semestre = ft.TextField(
        hint_text="Semestre",
        keyboard_type=ft.KeyboardType.NUMBER,
        border=ft.InputBorder.OUTLINE,
        border_width=2,
        border_color="black",
        bgcolor="white",
        color="black",
        height=70,
        text_size=18,
        expand=True,
        )

    genero = ft.RadioGroup(
        content=ft.Row(
            [
                ft.Text("Genero:", size=18),
                ft.Radio(value="Masculino", label="Masculino"),
                ft.Radio(value="Femenino", label="Femenino"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=40,
        )
    )

    enviar = ft.ElevatedButton(
        "Enviar",
        height=70,
        width=float("inf"),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=0),
            bgcolor="#9e9e9e",
            color="black",
        ),
    )

    page.add(
        ft.Column(
            [
                nombre,
                numero_control,
                email,
                ft.Row(
                    [carrera, semestre],
                    spacing=30,
                ),
                genero,
                enviar,
            ],
            spacing=35,
            expand=True,
        )
    )


ft.run(main)