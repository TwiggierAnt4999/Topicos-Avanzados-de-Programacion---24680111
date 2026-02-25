import flet as ft


def main(page: ft.Page):
    page.title = "Formulario"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#1e1e1e"
    page.padding = 50
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

    def campo(label):
        return ft.TextField(
            hint_text=label,
            border=ft.InputBorder.OUTLINE,
            border_width=2,
            border_color="#bbbbbb",
            bgcolor="#2b2b2b",
            color="white",
            hint_style=ft.TextStyle(color="#aaaaaa"),
            height=70,
            text_size=18,
            expand=True,
        )

    # Campos
    nombre = campo("Nombre")

    numero_control = ft.TextField(
        hint_text="Numero de control",
        keyboard_type=ft.KeyboardType.NUMBER,
        border=ft.InputBorder.OUTLINE,
        border_width=2,
        border_color="#bbbbbb",
        bgcolor="#2b2b2b",
        color="white",
        hint_style=ft.TextStyle(color="#aaaaaa"),
        height=70,
        text_size=18,
        expand=True,
    )

    email = campo("Email")

    carreras_lista = [
        "Contador Público",
        "Ingeniería Civil",
        "Ingeniería Electrónica",
        "Ingeniería en Gestión Empresarial",
        "Ingeniería en Sistemas",
        "Ingeniería Industrial",
        "Maestría en Ingeniería Administrativa",
    ]

    carrera = ft.Dropdown(
        hint_text="Carrera",
        options=[ft.dropdown.Option(c) for c in carreras_lista],
        border_color="#bbbbbb",
        border_width=2,
        bgcolor="#2b2b2b",
        color="white",
        height=70,
        text_size=18,
        expand=True,
    )

    semestre = ft.TextField(
        hint_text="Semestre",
        keyboard_type=ft.KeyboardType.NUMBER,
        border=ft.InputBorder.OUTLINE,
        border_width=2,
        border_color="#bbbbbb",
        bgcolor="#2b2b2b",
        color="white",
        hint_style=ft.TextStyle(color="#aaaaaa"),
        height=70,
        text_size=18,
        expand=True,
    )

    genero = ft.RadioGroup(
        content=ft.Row(
            [
                ft.Text("Género:", size=18, color="white"),
                ft.Radio(value="Masculino", label="Masculino"),
                ft.Radio(value="Femenino", label="Femenino"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=40,
        )
    )

    # Diálogo
    dialogo = ft.AlertDialog(
        modal=True,
        bgcolor="#2b2b2b",
        title=ft.Text("", color="white"),
        content=ft.Text("", color="white"),
        actions=[
            ft.TextButton(
                "Cerrar",
                style=ft.ButtonStyle(color="white"),
                on_click=lambda e: cerrar_dialogo()
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.overlay.append(dialogo)

    def cerrar_dialogo():
        dialogo.open = False
        page.update()

    def mostrar_dialogo(titulo, mensaje):
        dialogo.title.value = titulo
        dialogo.content.value = mensaje
        dialogo.open = True
        page.update()

    # Validación
    def limpiar_errores():
        for campo in [nombre, numero_control, email, semestre]:
            campo.error_text = None
            campo.border_color = "#bbbbbb"
        carrera.border_color = "#bbbbbb"

    def marcar_error(control, mensaje):
        control.error_text = mensaje
        control.border_color = "red"

    def validar(e):
        limpiar_errores()

        if not nombre.value:
            marcar_error(nombre, "Campo obligatorio")
            mostrar_dialogo("Error", "Todos los campos son obligatorios.")
            return

        if not numero_control.value:
            marcar_error(numero_control, "Campo obligatorio")
            mostrar_dialogo("Error", "Todos los campos son obligatorios.")
            return

        if not email.value:
            marcar_error(email, "Campo obligatorio")
            mostrar_dialogo("Error", "Todos los campos son obligatorios.")
            return

        if not carrera.value:
            carrera.border_color = "red"
            mostrar_dialogo("Error", "Todos los campos son obligatorios.")
            return

        if not semestre.value:
            marcar_error(semestre, "Campo obligatorio")
            mostrar_dialogo("Error", "Todos los campos son obligatorios.")
            return

        if not genero.value:
            mostrar_dialogo("Error", "Todos los campos son obligatorios.")
            return

        if numero_control.value and not numero_control.value.isdigit():
            marcar_error(numero_control, "Solo números")
            mostrar_dialogo("Error", "El Número de Control solo debe contener números.")
            return

        if semestre.value and not semestre.value.isdigit():
            marcar_error(semestre, "Solo números")
            mostrar_dialogo("Error", "El Semestre solo debe contener números.")
            return

        mensaje = (
            f"Nombre: {nombre.value}\n"
            f"Número de control: {numero_control.value}\n"
            f"Email: {email.value}\n"
            f"Carrera: {carrera.value}\n"
            f"Semestre: {semestre.value}\n"
            f"Género: {genero.value}"
        )

        mostrar_dialogo("Datos registrados correctamente", mensaje)

    enviar = ft.ElevatedButton(
        "Enviar",
        height=70,
        width=float("inf"),
        on_click=validar,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=0),
            bgcolor="#3a3a3a",
            color="white",
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