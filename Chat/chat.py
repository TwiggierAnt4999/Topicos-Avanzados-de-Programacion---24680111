from dataclasses import dataclass
import flet as ft

@dataclass
class Message:
    user_name: str
    text: str
    message_type: str 


@ft.control
class ChatMessage(ft.Row):
    def __init__(self, message: Message):
        super().__init__()
        self.vertical_alignment = ft.CrossAxisAlignment.START
        self.message = message

        self.controls = [
            ft.CircleAvatar(
                content=ft.Text(self.get_initials(message.user_name)),
                color=ft.Colors.WHITE,
                bgcolor=self.get_avatar_color(message.user_name),
            ),
            ft.Column(
                tight=True,
                spacing=5,
                controls=[
                    ft.Text(message.user_name, weight=ft.FontWeight.BOLD),
                    ft.Text(message.text, selectable=True),
                ],
            ),
        ]

    def get_initials(self, name):
        return name[:1].upper() if name else "?"

    def get_avatar_color(self, name):
        colors = [
            ft.Colors.BLUE,
            ft.Colors.GREEN,
            ft.Colors.RED,
            ft.Colors.PURPLE,
            ft.Colors.ORANGE,
            ft.Colors.TEAL,
        ]
        return colors[hash(name) % len(colors)]

def main(page: ft.Page):

    page.title = "Flet Chat"
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    new_message = ft.TextField(
        hint_text="Escribe un mensaje...",
        expand=True,
        min_lines=1,
        max_lines=5,
        shift_enter=True,
        filled=True,
    )

    def on_message(message: Message):
        if message.message_type == "chat_message":
            m = ChatMessage(message)
        else:
            m = ft.Text(
                message.text,
                italic=True,
                size=12,
                color=ft.Colors.BLACK_45,
            )

        chat.controls.append(m)
        page.update()

    page.pubsub.subscribe(on_message)

    async def send_message(e):
        if new_message.value:
            page.pubsub.send_all(
                Message(
                    page.session.store.get("user_name"),
                    new_message.value,
                    "chat_message",
                )
            )
            new_message.value = ""
            await new_message.focus()

    new_message.on_submit = send_message

    user_name_input = ft.TextField(
        label="Ingresa tu nombre",
        autofocus=True,
    )

    def join_chat(e):
        if not user_name_input.value:
            user_name_input.error_text = "El nombre no puede estar vacío"
            user_name_input.update()
            return

        page.session.store.set("user_name", user_name_input.value)
        dialog.open = False
        page.update()

        page.pubsub.send_all(
            Message(
                user_name_input.value,
                f"{user_name_input.value} se ha unido al chat",
                "login_message",
            )
        )

    dialog = ft.AlertDialog(
        modal=True,
        open=True,
        title=ft.Text("Bienvenido"),
        content=ft.Column([user_name_input], tight=True),
        actions=[ft.TextButton("Entrar", on_click=join_chat)],
    )

    page.overlay.append(dialog)

    page.add(
        ft.Container(
            content=chat,
            border=ft.border.all(1, ft.Colors.OUTLINE),
            padding=10,
            expand=True,
        ),
        ft.Row(
            [
                new_message,
                ft.IconButton(
                    icon=ft.Icons.SEND,
                    on_click=send_message,
                ),
            ]
        ),
    )


ft.run(main)