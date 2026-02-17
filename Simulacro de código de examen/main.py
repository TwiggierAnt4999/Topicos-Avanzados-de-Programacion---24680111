import flet as ft


def main(page: ft.Page):
    page.title = "Calculadora Estática - TAP"
    page.window_width = 280
    page.window_height = 450
    page.window_resizable = False
    page.padding = 15

    expression = [""]

    # ---------------- DISPLAY ----------------

    display_text = ft.Text("0", size=20)

    def update_display():
        display_text.value = expression[0] if expression[0] else "0"
        page.update()

    seccion_display = ft.Container(
        content=display_text,
        bgcolor=ft.Colors.BLACK12,
        height=70,
        alignment=ft.alignment.Alignment(1, 0),
        border=ft.border.all(1, ft.Colors.RED),
        padding=10
    )

    # ---------------- LÓGICA ----------------

    def agregar_valor(valor):
        if expression[0] == "Error":
            expression[0] = ""
        expression[0] += valor
        update_display()

    def calcular():
        try:
            resultado = str(eval(expression[0]))
            expression[0] = resultado
        except:
            expression[0] = "Error"
        update_display()

    def limpiar():
        expression[0] = ""
        update_display()

    # ---------------- BOTONES NUMÉRICOS ----------------

    def boton_numero(valor):
        return ft.Container(
            expand=1,
            height=50,
            bgcolor="blue",
            border=ft.border.all(1, "white"),
            alignment=ft.alignment.Alignment(0, 0),
            content=ft.Text(valor, color="white"),
            on_click=lambda e: agregar_valor(valor)
        )

    seccion_numeros = ft.Column(
        controls=[
            ft.Row(controls=[boton_numero("7"), boton_numero("8"), boton_numero("9")]),
            ft.Row(controls=[boton_numero("4"), boton_numero("5"), boton_numero("6")]),
            ft.Row(controls=[boton_numero("1"), boton_numero("2"), boton_numero("3")]),
            ft.Row(controls=[boton_numero("0"), boton_numero("."), 
                             ft.Container(
                                 expand=1,
                                 height=50,
                                 bgcolor="blue",
                                 border=ft.border.all(1, "white"),
                                 alignment=ft.alignment.Alignment(0, 0),
                                 content=ft.Text("C", color="white"),
                                 on_click=lambda e: limpiar()
                             )]),
        ],
        spacing=10
    )

    # ---------------- OPERACIONES ----------------

    def boton_operacion(valor):
        return ft.Container(
            expand=1,
            height=60,
            bgcolor="green",
            border=ft.border.all(1, "white"),
            alignment=ft.alignment.Alignment(0, 0),
            content=ft.Text(valor, color="white"),
            on_click=lambda e: agregar_valor(valor)
        )

    seccion_operaciones = ft.Row(
        controls=[
            boton_operacion("+"),
            boton_operacion("-"),
            boton_operacion("*"),
            boton_operacion("/"),
            ft.Container(
                expand=1,
                height=60,
                bgcolor="green",
                border=ft.border.all(1, "white"),
                alignment=ft.alignment.Alignment(0, 0),
                content=ft.Text("=", color="white"),
                on_click=lambda e: calcular()
            ),
        ]
    )

    # ---------------- CONSTRUCCIÓN FINAL ----------------

    page.add(
        ft.Column(
            controls=[
                seccion_display,
                ft.Text("Números:", size=12),
                seccion_numeros,
                ft.Divider(),
                ft.Text("Operaciones:", size=12),
                seccion_operaciones,
            ],
            spacing=15
        )
    )


if __name__ == "__main__":
    ft.run(main)
