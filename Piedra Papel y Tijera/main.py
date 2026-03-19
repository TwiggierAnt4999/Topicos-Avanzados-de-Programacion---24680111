import flet as ft
import random


def main(page: ft.Page):
    page.title = "Piedra, Papel o Tijera"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#1e1e1e"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.spacing = 30

    opciones = ["Piedra", "Papel", "Tijera"]

    eleccion_programa = ft.Container(
        content=ft.Text("", size=18, text_align=ft.TextAlign.CENTER),
        width=300,
        height=70,
        alignment=ft.Alignment.CENTER,
        border=ft.border.all(3, "white"),
    )

    resultado = ft.Container(
        width=350,
        height=70,
        alignment=ft.Alignment.CENTER,
        visible=False,
    )

    def determinar_ganador(usuario, pc):
        if usuario == pc:
            return "Empate"
        if (
            (usuario == "Piedra" and pc == "Tijera")
            or (usuario == "Papel" and pc == "Piedra")
            or (usuario == "Tijera" and pc == "Papel")
        ):
            return "Ganaste"
        return "Perdiste"

    def jugar(e):
        usuario = e.control.data
        pc = random.choice(opciones)

        eleccion_programa.content.value = f"La computadora eligió: {pc}"

        r = determinar_ganador(usuario, pc)

        resultado.visible = True
        resultado.content = ft.Text(r, size=20, weight=ft.FontWeight.BOLD)

        if r == "Ganaste":
            resultado.bgcolor = "green"
        elif r == "Perdiste":
            resultado.bgcolor = "red"
        else:
            resultado.bgcolor = "gray"

        page.update()

    def reiniciar(e):
        eleccion_programa.content.value = ""
        resultado.visible = False
        page.update()

    menu = ft.PopupMenuButton(
        content=ft.Container(
            content=ft.Text("Elije una opción", size=18),
            width=250,
            height=70,
            alignment=ft.Alignment.CENTER,
            border=ft.border.all(3, "white"),
        ),
        items=[
            ft.PopupMenuItem(
                content=ft.Text("Piedra"),
                on_click=jugar,
                data="Piedra",
            ),
            ft.PopupMenuItem(
                content=ft.Text("Papel"),
                on_click=jugar,
                data="Papel",
            ),
            ft.PopupMenuItem(
                content=ft.Text("Tijera"),
                on_click=jugar,
                data="Tijera",
            ),
        ],
    )

    dialogo = ft.AlertDialog(
        modal=True,
        title=ft.Text("Reiniciar juego"),
        content=ft.Text("¿Quieres volver a jugar?"),
        actions=[
            ft.TextButton("Sí", on_click=lambda e: (reiniciar(e), setattr(dialogo, "open", False), page.update())),
            ft.TextButton("No", on_click=lambda e: (setattr(dialogo, "open", False), page.update())),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    boton_reiniciar = ft.Button(
        "Reiniciar",
        on_click=lambda e: (setattr(dialogo, "open", True), page.overlay.append(dialogo), page.update()),
        width=250,
        height=60,
    )

    page.add(
        ft.Text("Piedra, Papel o Tijera", size=28, weight=ft.FontWeight.BOLD),
        menu,
        eleccion_programa,
        resultado,
        boton_reiniciar,
    )


ft.run(main)