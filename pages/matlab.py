import flet as ft
import random, threading, time
import subprocess, sys, os

# ── Shared baby blue palette ──────────────────────────────────────────────────
BG       = "#E0F4FF"
SURFACE  = "#F0F8FF"
SURFACE2 = "#E8F4FF"
BORDER   = "#B0E0E6"
TEXT_PRI = "#000000"
TEXT_SEC = "#4A4A4A"
ACCENT   = "#0066CC"
ACCENT_B = "#003D99"

CONFETTI_COLORS = ["#FF6B6B","#FFD93D","#6BCB77","#4D96FF","#FF922B","#CC5DE8","#F06595"]


def _load_cert(index: int) -> str:
    return f"certificates/{index}.pdf"


def _hoverable(container: ft.Container, accent_color: str) -> ft.Container:
    container.animate = 200

    def on_hover(e, c=container, col=accent_color):
        if e.data == "true":
            c.bgcolor = SURFACE2
            c.border  = ft.Border.all(1, col)
            c.shadow  = ft.BoxShadow(spread_radius=0, blur_radius=18,
                                     color=col + "33", offset=ft.Offset(0, 4))
        else:
            c.bgcolor = SURFACE
            c.border  = ft.Border.all(1, BORDER)
            c.shadow  = None
        c.update()

    container.on_hover = on_hover
    return container


class MatlabPage:
    COURSES = [
        {"title": "MATLAB Onramp", "description": "Introduction to MATLAB syntax, variables, and basic operations.",
         "date": "10 Jan 2026", "hours": "~2 hrs", "cert_image": _load_cert(1)},
        {"title": "Machine Learning Onramp", "description": "Supervised learning fundamentals using MATLAB's ML toolbox.",
         "date": "17 Jan 2026", "hours": "~2 hrs", "cert_image": _load_cert(6)},
        {"title": "Deep Learning Onramp", "description": "Neural network concepts and training workflows in MATLAB.",
         "date": "24 Jan 2026", "hours": "~2 hrs", "cert_image": _load_cert(3)},
        {"title": "Signal Processing Onramp", "description": "Filtering, FFT, and frequency-domain analysis in MATLAB.",
         "date": "31 Jan 2026", "hours": "~2 hrs", "cert_image": _load_cert(4)},
        {"title": "Simulink Onramp", "description": "Block diagram modelling and simulation of dynamic systems.",
         "date": "7 Feb 2026", "hours": "~2 hrs", "cert_image": _load_cert(2)},
        {"title": "Explore Data with MATLAB Plots", "description": "Data visualisation techniques and best practices in MATLAB.",
         "date": "14 Feb 2026", "hours": "~2 hrs", "cert_image": _load_cert(3)},
        {"title": "Programming Constructs", "description": "Loops, conditionals, and functions for structured MATLAB programs.",
         "date": "21 Feb 2026", "hours": "~2 hrs", "cert_image": _load_cert(7)},
        {"title": "MATLAB Desktop Tools and Troubleshooting Scripts",
         "description": "Using the MATLAB environment, debugging tools, and best practices.",
         "date": "28 Feb 2026", "hours": "~2 hrs", "cert_image": _load_cert(8)},
    ]

    def __init__(self):
        self._overlay_ref  = ft.Ref[ft.Container]()
        self._confetti_ref = ft.Ref[ft.Stack]()
        self._card_refs    = []
        self._badge_refs   = []

    def _close_preview(self, e):
        self._overlay_ref.current.visible = False
        self._overlay_ref.current.update()

    def _open_preview(self, e, src):
        self._overlay_ref.current.content = ft.Stack(controls=[
            ft.Container(expand=True, bgcolor="#000000", opacity=0.9, on_click=self._close_preview),
            ft.Container(
                content=ft.Column(controls=[
                    ft.Row(controls=[ft.Container(expand=True),
                                     ft.IconButton(icon=ft.Icons.CLOSE, icon_color=TEXT_PRI,
                                                   on_click=self._close_preview)]),
                    ft.Image(src=src, fit="contain", expand=True),
                ], spacing=4, expand=True),
                padding=ft.Padding(left=24, right=24, top=24, bottom=24), expand=True,
            ),
        ], expand=True)
        self._overlay_ref.current.visible = True
        self._overlay_ref.current.update()

    def _build_badge(self, ref):
        return ft.Container(
            ref=ref,
            content=ft.Text("Completed", size=11, weight=ft.FontWeight.W_600, color=ACCENT),
            bgcolor=ACCENT_B + "33",
            padding=ft.Padding(left=10, right=10, top=4, bottom=4),
            border_radius=20,
            border=ft.Border.all(1, ACCENT_B),
            animate=800,
        )

    def _open_certificate_url(self, cert_filename):
        async def _handler(e):
            try:
                # Get the directory of the current file
                current_dir = os.path.dirname(os.path.abspath(__file__))
                portfolio_dir = os.path.dirname(current_dir)
                cert_path = os.path.join(portfolio_dir, "assets", cert_filename)
                
                # Open PDF with system default application
                if sys.platform == "win32":
                    os.startfile(cert_path)
                elif sys.platform == "darwin":  # macOS
                    subprocess.run(["open", cert_path])
                else:  # Linux
                    subprocess.run(["xdg-open", cert_path])
            except Exception as ex:
                print(f"Error opening certificate: {ex}")
        return _handler

    def _build_card(self, course, index, card_ref, badge_ref):
        return _hoverable(
            ft.Container(
                ref=card_ref,
                opacity=0,
                animate_opacity=600,
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Container(
                            content=ft.Text(str(index), size=13, weight=ft.FontWeight.W_700, color=ACCENT),
                            width=32, height=32, border_radius=16,
                            bgcolor=ACCENT_B + "33",
                            border=ft.Border.all(1, ACCENT_B),
                            alignment=ft.Alignment(0, 0),
                        ),
                        ft.Text(course["title"], size=14, weight=ft.FontWeight.W_600, color=TEXT_PRI, expand=True),
                        ft.Icon(ft.Icons.CHECK_CIRCLE, color=ACCENT, size=20),
                    ], spacing=10),
                    ft.Text(course["description"], size=13, color=TEXT_SEC),
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.CALENDAR_TODAY, size=12, color=TEXT_SEC),
                        ft.Text(course["date"], size=11, color=TEXT_SEC),
                        ft.Text("·", size=11, color=BORDER),
                        ft.Icon(ft.Icons.TIMER, size=12, color=TEXT_SEC),
                        ft.Text(course["hours"], size=11, color=TEXT_SEC, italic=True),
                        ft.Container(expand=True),
                        self._build_badge(badge_ref),
                    ], spacing=4),
                    ft.Container(
                        content=ft.Row(controls=[
                            ft.Icon(ft.Icons.PICTURE_AS_PDF, color=ACCENT_B, size=28),
                            ft.Column(controls=[
                                ft.Text(f"Certificate {index}", size=13, weight=ft.FontWeight.W_600, color=TEXT_PRI),
                                ft.Text("Open certificate PDF", size=11, color=TEXT_SEC),
                            ], spacing=4, expand=True),
                        ], spacing=12, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                        bgcolor=SURFACE2, border_radius=8, height=120,
                        padding=ft.Padding(left=14, right=14, top=14, bottom=14),
                        border=ft.Border.all(1, BORDER),
                        margin=ft.Margin(left=0, right=0, top=4, bottom=0),
                        clip_behavior=ft.ClipBehavior.HARD_EDGE,
                        on_click=self._open_certificate_url(course["cert_image"]),
                        ink=True, tooltip="Open certificate PDF",
                    ),
                ], spacing=8),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=16, right=16, top=16, bottom=16),
                border=ft.Border.all(1, BORDER),
            ),
            ACCENT,
        )

    def _make_confetti_piece(self):
        return ft.Container(
            width=random.randint(10, 18), height=random.randint(10, 18),
            bgcolor=random.choice(CONFETTI_COLORS),
            border_radius=random.choice([0, 10]),
            left=random.randint(0, 1200), top=random.randint(-50, 0),
            opacity=1, animate_opacity=1500, animate_position=1500,
        )

    def _run_animations(self, page=None):
        for ref in self._card_refs:
            time.sleep(0.12)
            try:
                ref.current.opacity = 1
                ref.current.update()
            except Exception:
                pass

        def pulse_badges():
            for _ in range(4):
                for c in [ACCENT_B + "33", ACCENT_B + "77"]:
                    for ref in self._badge_refs:
                        try:
                            ref.current.bgcolor = c
                            ref.current.update()
                        except Exception:
                            pass
                    time.sleep(0.5)
            for ref in self._badge_refs:
                try:
                    ref.current.bgcolor = ACCENT_B + "33"
                    ref.current.update()
                except Exception:
                    pass

        threading.Thread(target=pulse_badges, daemon=True).start()

        try:
            pieces = self._confetti_ref.current.controls
            for p in pieces:
                p.top = random.randint(400, 800)
                p.opacity = 0
                p.left = random.randint(0, 1200)
            self._confetti_ref.current.update()
            time.sleep(2.5)
            self._confetti_ref.current.visible = False
            self._confetti_ref.current.update()
        except Exception as ex:
            print("Confetti error:", ex)

    def build(self):
        self._card_refs  = [ft.Ref[ft.Container]() for _ in self.COURSES]
        self._badge_refs = [ft.Ref[ft.Container]() for _ in self.COURSES]

        cards = [self._build_card(c, i + 1, self._card_refs[i], self._badge_refs[i])
                 for i, c in enumerate(self.COURSES)]

        progress_section = _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Text("Overall Progress", size=14, weight=ft.FontWeight.W_600, color=TEXT_PRI),
                        ft.Container(expand=True),
                        ft.Text("8 / 8 courses", size=14, weight=ft.FontWeight.W_700, color=ACCENT),
                    ]),
                    ft.ProgressBar(value=1.0, bgcolor=BORDER, color=ACCENT, height=10, border_radius=5),
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.CHECK_BOX, color=ACCENT, size=14),
                        ft.Text("All 8 courses completed — requirement met!", size=12,
                                color=ACCENT, weight=ft.FontWeight.W_600),
                    ], spacing=6),
                ], spacing=10),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=20, right=20, top=20, bottom=20),
                border=ft.Border.all(1, ACCENT_B),
                margin=ft.Margin(left=0, right=0, top=0, bottom=16),
            ),
            ACCENT,
        )

        left_col  = ft.Column(controls=cards[::2],  spacing=14, expand=True)
        right_col = ft.Column(controls=cards[1::2], spacing=14, expand=True)

        confetti_layer = ft.Stack(ref=self._confetti_ref,
                                  controls=[self._make_confetti_piece() for _ in range(40)],
                                  expand=True)
        overlay = ft.Container(ref=self._overlay_ref, visible=False, expand=True, bgcolor="transparent")

        def on_mount(e=None):
            threading.Thread(target=self._run_animations, args=(None,), daemon=True).start()

        main_column = ft.Column(controls=[
            ft.Text("MATLAB Achievement Hub", size=22, weight=ft.FontWeight.W_700, color=TEXT_PRI),
            ft.Text("Proof of completion for 8 MathWorks Learning Center self-paced courses.", size=14, color=TEXT_SEC),
            ft.Divider(height=12, color="transparent"),
            progress_section,
            ft.Row(controls=[left_col, right_col], spacing=14, vertical_alignment=ft.CrossAxisAlignment.START),
        ], spacing=4, scroll=ft.ScrollMode.AUTO, expand=True)

        wrapper = ft.Stack(controls=[main_column, confetti_layer, overlay], expand=True)
        outer   = ft.Container(content=wrapper, expand=True)
        outer.did_mount = on_mount
        return outer