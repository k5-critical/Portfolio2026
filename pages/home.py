import flet as ft

# ── Shared baby blue palette ──────────────────────────────────────────────────
BG       = "#E0F4FF"
SURFACE  = "#F0F8FF"
BORDER   = "#B0E0E6"
TEXT_PRI = "#000000"
TEXT_SEC = "#4A4A4A"
ACCENT   = "#0066CC"


class HomePage:
    PROFILE_IMAGE = "screenshots/profile.jpeg"
    EMAIL_URL     = "mailto:lamekjunior05@gmail.com"
    GITHUB_URL    = "https://github.com/k5-critical"

    def _link_button(self, label: str, url: str, icon: str):
        async def _open_url(e):
            await e.page.launch_url(url)

        return ft.TextButton(
            content=ft.Row(
                controls=[
                    ft.Icon(icon, color=ACCENT, size=16),
                    ft.Text(label, size=13, color=TEXT_PRI),
                ],
                spacing=8,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            on_click=_open_url,
            style=ft.ButtonStyle(
                padding=ft.Padding(left=14, right=14, top=10, bottom=10),
                shape=ft.RoundedRectangleBorder(radius=12),
            ),
        )

    def _stat_card(self, value: str, label: str):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(value, size=28, weight=ft.FontWeight.W_700, color="#000000"),
                    ft.Text(label, size=13, color="#4A4A4A", weight=ft.FontWeight.W_600),
                ],
                spacing=6,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor="#B0E0E6",
            border_radius=16,
            padding=ft.Padding(left=24, right=24, top=20, bottom=20),
            border=ft.Border.all(2, "#0066CC"),
            expand=True,
        )

    def _info_card(self, icon: str, title: str, value: str):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(icon, size=24, color="#0066CC"),
                            ft.Text(title, size=13, weight=ft.FontWeight.W_600, color="#4A4A4A"),
                        ],
                        spacing=8,
                    ),
                    ft.Text(value, size=20, weight=ft.FontWeight.W_700, color="#000000"),
                ],
                spacing=10,
            ),
            bgcolor="#B0E0E6",
            border_radius=14,
            padding=ft.Padding(left=20, right=20, top=18, bottom=18),
            border=ft.Border.all(2, "#0066CC"),
            expand=True,
        )

    def build(self, page: ft.Page):
        profile_avatar = ft.Container(
            content=ft.Image(
                src=self.PROFILE_IMAGE,
                fit=ft.BoxFit.COVER,
                width=150,
                height=150,
                error_content=ft.Container(
                    content=ft.Icon(ft.Icons.PERSON, color=ACCENT, size=48),
                    alignment=ft.Alignment(0, 0),
                ),
            ),
            width=150,
            height=150,
            border_radius=75,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            border=ft.Border.all(3, ACCENT),
        )

        hero = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Text("Civil Engineer", size=28, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                            ft.Text("Contact and profile details", size=13, color=TEXT_SEC),
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        self._link_button("Email: lamekjunior05@gmail.com", self.EMAIL_URL, ft.Icons.EMAIL),
                                        self._link_button("GitHub: k5-critical", self.GITHUB_URL, ft.Icons.ADD_LINK),
                                    ],
                                    spacing=10,
                                ),
                                padding=ft.Padding(left=0, right=0, top=12, bottom=0),
                            ),
                        ],
                        spacing=14,
                        expand=True,
                    ),
                    ft.Container(width=24),
                    ft.Column(
                        controls=[
                            ft.Text("Profile", size=14, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                            profile_avatar,
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.START,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.START,
                spacing=20,
            ),
            bgcolor=SURFACE,
            border_radius=20,
            padding=ft.Padding(left=24, right=24, top=24, bottom=24),
            border=ft.Border.all(1, BORDER),
            expand=True,
        )

        stats = ft.Row(
            controls=[
                self._stat_card("2nd", "Year of Study"),
                self._stat_card("12+", "Projects Completed"),
                self._stat_card("3.8 / 4.0", "GPA"),
                self._stat_card("2*", "Internship"),
            ],
            spacing=12,
            wrap=True,
            expand=True,
        )

        return ft.Column(
            controls=[
                hero,
            ],
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
        )
