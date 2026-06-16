import flet as ft

# ── Shared baby blue palette ──────────────────────────────────────────────────
BG       = "#E0F4FF"
SURFACE  = "#F0F8FF"
SURFACE2 = "#E8F4FF"
BORDER   = "#B0E0E6"
TEXT_PRI = "#000000"
TEXT_SEC = "#4A4A4A"
ACCENT   = "#0066CC"
ACCENT_B = "#003D99"
AMBER    = "#FF8C00"
BLUE     = "#0066CC"


def _hoverable(container: ft.Container, accent_color: str) -> ft.Container:
    container.animate = 200

    def on_hover(e, c=container, col=accent_color):
        if e.data == "true":
            c.bgcolor = SURFACE2
            c.border  = ft.Border.all(1, col)
            c.shadow  = ft.BoxShadow(
                spread_radius=0,
                blur_radius=18,
                color=col + "33",
                offset=ft.Offset(0, 4),
            )
        else:
            c.bgcolor = SURFACE
            c.border  = ft.Border.all(1, BORDER)
            c.shadow  = None
        c.update()

    container.on_hover = on_hover
    return container


class TimelinePage:
    ENTRIES = [
        {
            "week": "Week 1", "dates": "20 Jan – 26 Jan",
            "task": "Project setup & repo initialisation",
            "contribution": "Initialised the GitHub repository, set up branching strategy, and created the base Flet app structure shared with the team.",
            "status": "Done", "icon": ft.icons.ROCKET_LAUNCH, "tags": ["Git", "Setup"],
        },
        {
            "week": "Week 2", "dates": "27 Jan – 2 Feb",
            "task": "Civil engineering module — input form",
            "contribution": "Built the material input form for the Civil module using ft.TextField and ft.Dropdown. Added client-side validation.",
            "status": "Done", "icon": ft.icons.BUILD, "tags": ["Python", "UI"],
        },
        {
            "week": "Week 3", "dates": "3 Feb – 9 Feb",
            "task": "Cost calculation logic",
            "contribution": "Implemented the Total Cost formula (Σ Qᵢ × Pᵢ + Overheads) in Python and wired it to the UI. Wrote unit tests.",
            "status": "Done", "icon": ft.icons.CALCULATE, "tags": ["Python", "Maths"],
        },
        {
            "week": "Week 4", "dates": "10 Feb – 16 Feb",
            "task": "Results display & data table",
            "contribution": "Created the ft.DataTable component showing itemised cost breakdown. Added CSV export functionality.",
            "status": "Done", "icon": ft.icons.TABLE_CHART, "tags": ["Python", "UI"],
        },
        {
            "week": "Week 5", "dates": "17 Feb – 23 Feb",
            "task": "Code review & pull request",
            "contribution": "Reviewed 3 teammates' PRs, flagged a critical off-by-one error in the Mining module loop. Merged approved changes.",
            "status": "Done", "icon": ft.icons.RATE_REVIEW, "tags": ["Git", "Collaboration"],
        },
        {
            "week": "Week 6", "dates": "24 Feb – 2 Mar",
            "task": "Portfolio — this web app",
            "contribution": "Started building the individual Flet web portfolio. Completed Timeline and MATLAB hub pages.",
            "status": "In Progress", "icon": ft.icons.WEB, "tags": ["Python", "UI"],
        },
    ]

    STATUS_STYLES = {
        "Done":        (ACCENT_B + "33", ACCENT, ACCENT),
        "In Progress": (AMBER + "33",    AMBER,  AMBER),
        "Pending":     ("#6E40C933",     "#A371F7", "#A371F7"),
    }

    def _tag_chip(self, label):
        return ft.Container(
            content=ft.Text(label, size=10, color=BLUE),
            bgcolor=BLUE + "22",
            padding=ft.Padding(left=8, right=8, top=3, bottom=3),
            border_radius=20,
            border=ft.Border.all(1, BLUE + "44"),
        )

    def _build_entry(self, entry, index, is_last):
        bg, fg, dot_color = self.STATUS_STYLES.get(entry["status"], (SURFACE2, TEXT_SEC, TEXT_SEC))
        is_done     = entry["status"] == "Done"
        is_progress = entry["status"] == "In Progress"

        dot = ft.Container(
            width=44, height=44, border_radius=22,
            bgcolor=SURFACE2,
            content=ft.Icon(entry["icon"], color=dot_color, size=20),
            alignment=ft.Alignment(0, 0),
            border=ft.Border.all(2, dot_color),
        )

        week_badge = ft.Container(
            content=ft.Text(entry["week"], size=11, weight=ft.FontWeight.W_700, color=dot_color),
            bgcolor=bg,
            padding=ft.Padding(left=10, right=10, top=3, bottom=3),
            border_radius=20,
            border=ft.Border.all(1, dot_color + "55"),
        )

        status_icon = (ft.icons.CHECK_CIRCLE if is_done else ft.icons.PENDING if is_progress else ft.icons.CIRCLE)
        status_badge = ft.Container(
            content=ft.Row(controls=[
                ft.Icon(status_icon, size=12, color=fg),
                ft.Text(entry["status"], size=11, weight=ft.FontWeight.W_600, color=fg),
            ], spacing=4),
            bgcolor=bg,
            padding=ft.Padding(left=10, right=10, top=4, bottom=4),
            border_radius=20,
        )

        card = _hoverable(
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row(controls=[
                            week_badge,
                            ft.Text(entry["dates"], size=11, color=TEXT_SEC),
                            ft.Container(expand=True),
                            status_badge,
                        ], spacing=8),
                        ft.Text(entry["task"], size=14, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                        ft.Text(entry["contribution"], size=13, color=TEXT_SEC, no_wrap=False),
                        ft.Row(controls=[self._tag_chip(t) for t in entry.get("tags", [])], spacing=6, wrap=True),
                    ],
                    spacing=8,
                ),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=16, right=16, top=16, bottom=16),
                border=ft.Border.all(1, BORDER),
                expand=True,
            ),
            dot_color,
        )

        connector = ft.Container(
            width=2, height=20,
            bgcolor=dot_color if is_done else BORDER,
            margin=ft.Margin(left=21, right=21, top=0, bottom=0),
        )

        left_col = ft.Column(
            controls=[dot] + ([] if is_last else [connector]),
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            width=44,
        )

        return ft.Container(
            content=ft.Row(controls=[left_col, card], spacing=16,
                           vertical_alignment=ft.CrossAxisAlignment.START),
            margin=ft.Margin(left=0, right=0, top=0, bottom=12),
        )

    def build(self):
        done_count = sum(1 for e in self.ENTRIES if e["status"] == "Done")
        total      = len(self.ENTRIES)
        progress   = done_count / total

        hero = _hoverable(
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row(controls=[
                            ft.Icon(ft.icons.TODAY, color=TEXT_PRI, size=28),
                            ft.Text("Project Timeline", size=24, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                        ], spacing=10),
                        ft.Text("Weekly log of my individual contributions to the group project.", size=13, color=TEXT_SEC),
                        ft.Divider(height=8, color="transparent"),
                        ft.Row(controls=[
                            ft.Text(f"{done_count} of {total} weeks completed", size=12, color=TEXT_SEC),
                            ft.Container(expand=True),
                            ft.Text(f"{int(progress * 100)}%", size=12, weight=ft.FontWeight.W_700, color=ACCENT),
                        ]),
                        ft.ProgressBar(value=progress, bgcolor=BORDER, color=ACCENT, height=6, border_radius=4),
                    ],
                    spacing=6,
                ),
                bgcolor=SURFACE, border_radius=16,
                padding=ft.Padding(left=24, right=24, top=24, bottom=24),
                margin=ft.Margin(left=0, right=0, top=0, bottom=24),
                border=ft.Border.all(1, BORDER),
            ),
            ACCENT,
        )

        def stat_card(value, label, color):
            return _hoverable(
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(value, size=22, weight=ft.FontWeight.W_700, color=color),
                            ft.Text(label, size=11, color=TEXT_SEC),
                        ],
                        spacing=2,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=SURFACE, border_radius=12,
                    padding=ft.Padding(left=20, right=20, top=14, bottom=14),
                    border=ft.Border.all(1, BORDER),
                    expand=True,
                    alignment=ft.Alignment(0, 0),
                ),
                color,
            )

        stats = ft.Row(controls=[
            stat_card(str(total), "Total Weeks", TEXT_PRI),
            stat_card(str(done_count), "Completed", ACCENT),
            stat_card(str(sum(1 for e in self.ENTRIES if e["status"] == "In Progress")), "In Progress", AMBER),
        ], spacing=12)

        entries = [self._build_entry(e, i, i == len(self.ENTRIES) - 1) for i, e in enumerate(self.ENTRIES)]

        return ft.Column(
            controls=[
                hero, stats,
                ft.Divider(height=24, color="transparent"),
                ft.Text("Weekly Contributions", size=16, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                ft.Divider(height=8, color="transparent"),
                *entries,
            ],
            spacing=4,
            scroll=ft.ScrollMode.AUTO,
        )
