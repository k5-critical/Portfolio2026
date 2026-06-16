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
BLUE     = "#0066CC"
AMBER    = "#FF8C00"
PURPLE   = "#9370DB"
RED      = "#DC143C"


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


class GithubPage:
    COMMITS = [
        {"hash": "a3f9c12", "message": "Add Civil module cost input form",       "date": "28 Jan 2026", "branch": "feature/civil-input"},
        {"hash": "b72e4d8", "message": "Implement Total Cost calculation logic",  "date": "5 Feb 2026",  "branch": "feature/civil-input"},
        {"hash": "c1a8f53", "message": "Add unit tests for cost formula",         "date": "6 Feb 2026",  "branch": "feature/civil-input"},
        {"hash": "d90b217", "message": "Create DataTable for cost breakdown",     "date": "12 Feb 2026", "branch": "feature/results-table"},
        {"hash": "e5c3a91", "message": "Add CSV export to results page",          "date": "13 Feb 2026", "branch": "feature/results-table"},
        {"hash": "f84d632", "message": "Fix off-by-one in Mining loop (review)",  "date": "18 Feb 2026", "branch": "dev"},
    ]

    PULL_REQUESTS = [
        {"pr_number": "#12", "title": "Civil module — input form + validation", "status": "Merged",
         "commits": 3, "reviews": "Reviewed by: @teammate1, @teammate2",
         "description": "Added the full Civil engineering material input form with dropdowns, text fields, and client-side validation."},
        {"pr_number": "#19", "title": "Results DataTable + CSV export", "status": "Merged",
         "commits": 2, "reviews": "Reviewed by: @teammate3",
         "description": "Implemented the itemised cost breakdown table using ft.DataTable. Added a CSV export button."},
        {"pr_number": "#23", "title": "Code review — fix Mining module loop", "status": "Closed",
         "commits": 1, "reviews": "Reviewed by: me (@your_github_handle)",
         "description": "Identified and fixed an off-by-one error in the Mining module's material loop."},
    ]

    WEEKLY_COMMITS = [
        {"week": "20 Jan", "count": 1}, {"week": "27 Jan", "count": 3},
        {"week": "3 Feb",  "count": 2}, {"week": "10 Feb", "count": 2},
        {"week": "17 Feb", "count": 1}, {"week": "24 Feb", "count": 0},
    ]

    IMPACT_SUMMARY = """
My primary contribution was building the Civil Engineering module of the group app,
covering the full pipeline from user input to cost output.

I designed and implemented:
- The material input form (dropdowns, text fields, validation)
- The Total Cost calculation engine: Σ (Qᵢ × Pᵢ) + Overheads
- The results DataTable showing an itemised cost breakdown
- A CSV export feature for engineering reporting

Beyond my module, I contributed to code quality across the team by reviewing
3 pull requests and catching a critical logic bug in the Mining module.

**Total: 6 commits · 2 PRs opened · 3 PRs reviewed**
"""

    STATUS_STYLE = {
        "Merged": (ACCENT_B + "33", ACCENT, ACCENT_B),
        "Closed": (RED + "22",      RED,    RED + "55"),
        "Open":   (BLUE + "22",     BLUE,   BLUE + "44"),
    }

    BRANCH_COLORS = {
        "feature/civil-input":   (PURPLE + "22", PURPLE),
        "feature/results-table": (AMBER  + "22", AMBER),
        "dev":                   (ACCENT_B+"22", ACCENT),
    }

    def _stat_card(self, icon, value, label, color):
        return _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Icon(icon, color=color, size=24),
                    ft.Text(value, size=22, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                    ft.Text(label, size=12, color=TEXT_SEC),
                ], spacing=4, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=16, right=16, top=16, bottom=16),
                border=ft.Border.all(1, BORDER),
                expand=True, alignment=ft.Alignment(0, 0),
            ),
            color,
        )

    def _build_contribution_graph(self):
        max_count = max(w["count"] for w in self.WEEKLY_COMMITS) or 1
        bars = []
        for w in self.WEEKLY_COMMITS:
            height = max(4, int((w["count"] / max_count) * 80))
            bars.append(ft.Column(controls=[
                ft.Text(str(w["count"]), size=11, color=TEXT_SEC, text_align=ft.TextAlign.CENTER),
                ft.Container(width=36, height=height,
                             bgcolor=ACCENT if w["count"] > 0 else BORDER,
                             border_radius=ft.BorderRadius(4, 4, 0, 0)),
                ft.Text(w["week"], size=10, color=TEXT_SEC, text_align=ft.TextAlign.CENTER),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4))

        return _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Text("Contribution Activity", size=14, weight=ft.FontWeight.W_600, color=TEXT_PRI),
                    ft.Text("Commits per week", size=12, color=TEXT_SEC),
                    ft.Container(
                        content=ft.Row(controls=bars,
                                       alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                       vertical_alignment=ft.CrossAxisAlignment.END),
                        padding=ft.Padding(left=0, right=0, top=8, bottom=4),
                    ),
                ], spacing=6),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=16, right=16, top=16, bottom=16),
                border=ft.Border.all(1, BORDER),
            ),
            ACCENT,
        )

    def _commit_row(self, c):
        bg, fg = self.BRANCH_COLORS.get(c["branch"], (SURFACE2, TEXT_SEC))
        return ft.Container(
            content=ft.Row(controls=[
                ft.Icon(ft.Icons.COMMIT, size=14, color=BLUE),
                ft.Text(c["hash"], size=12, color=BLUE, font_family="monospace", width=70),
                ft.Text(c["message"], size=13, color=TEXT_PRI, expand=True),
                ft.Text(c["date"], size=11, color=TEXT_SEC, width=90),
                ft.Container(
                    content=ft.Text(c["branch"], size=10, color=fg),
                    bgcolor=bg,
                    padding=ft.Padding(left=8, right=8, top=3, bottom=3),
                    border_radius=20,
                    border=ft.Border.all(1, fg + "55"),
                ),
            ], spacing=10),
            padding=ft.Padding(left=12, right=12, top=10, bottom=10),
            border=ft.Border(bottom=ft.BorderSide(1, BORDER)),
        )

    def _pr_card(self, pr):
        bg, fg, border_c = self.STATUS_STYLE.get(pr["status"], (SURFACE2, TEXT_SEC, BORDER))
        icon = (ft.Icons.MERGE if pr["status"] == "Merged"
                else ft.Icons.CLOSE if pr["status"] == "Closed"
                else ft.Icons.CALL_SPLIT)
        return _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Icon(icon, color=fg, size=16),
                        ft.Text(pr["pr_number"], size=13, color=TEXT_SEC, width=36),
                        ft.Text(pr["title"], size=14, weight=ft.FontWeight.W_600,
                                color=TEXT_PRI, expand=True),
                        ft.Container(
                            content=ft.Text(pr["status"], size=11,
                                            weight=ft.FontWeight.W_600, color=fg),
                            bgcolor=bg,
                            padding=ft.Padding(left=10, right=10, top=4, bottom=4),
                            border_radius=20,
                            border=ft.Border.all(1, border_c),
                        ),
                    ], spacing=8),
                    ft.Text(pr["description"], size=13, color=TEXT_SEC),
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.COMMIT, size=12, color=TEXT_SEC),
                        ft.Text(f"{pr['commits']} commits", size=12, color=TEXT_SEC),
                        ft.Text("·", size=12, color=BORDER),
                        ft.Icon(ft.Icons.PERSON, size=14, color=TEXT_SEC),
                        ft.Text(pr["reviews"], size=12, color=TEXT_SEC),
                    ], spacing=4),
                ], spacing=8),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=16, right=16, top=16, bottom=16),
                border=ft.Border.all(1, BORDER),
                margin=ft.Margin(left=0, right=0, top=0, bottom=10),
            ),
            fg,
        )

    def _screenshot_card(self, title, src):
        return _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Text(title, size=13, weight=ft.FontWeight.W_600, color=TEXT_PRI),
                    ft.Container(
                        content=ft.Image(
                            src=src, fit=ft.BoxFit.CONTAIN,
                            error_content=ft.Column(controls=[
                                ft.Icon(ft.Icons.IMAGE_NOT_SUPPORTED, color=BORDER, size=32),
                                ft.Text(f"Add screenshot to:\nassets/{src}", size=11,
                                        color=TEXT_SEC, text_align=ft.TextAlign.CENTER),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4),
                        ),
                        bgcolor=SURFACE2, border_radius=8, height=160,
                        border=ft.Border.all(1, BORDER),
                        clip_behavior=ft.ClipBehavior.HARD_EDGE,
                        alignment=ft.Alignment(0, 0),
                    ),
                ], spacing=6),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=12, right=12, top=12, bottom=12),
                border=ft.Border.all(1, BORDER),
                expand=True,
            ),
            BLUE,
        )

    def build(self):
        hero = _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.FOLDER, color=TEXT_PRI, size=28),
                        ft.Text("GitHub Evidence", size=24, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                    ], spacing=10),
                    ft.Text("Documentation of my individual contributions to the group repository.",
                            size=13, color=TEXT_SEC),
                ], spacing=8),
                bgcolor=SURFACE, border_radius=16,
                padding=ft.Padding(left=24, right=24, top=24, bottom=24),
                margin=ft.Margin(left=0, right=0, top=0, bottom=16),
                border=ft.Border.all(1, BORDER),
            ),
            ACCENT,
        )

        stats = ft.Row(controls=[
            self._stat_card(ft.Icons.COMMIT,      "6", "Commits",      BLUE),
            self._stat_card(ft.Icons.CALL_MERGE,  "2", "PRs Opened",   ACCENT),
            self._stat_card(ft.Icons.RATE_REVIEW, "3", "PRs Reviewed", PURPLE),
            self._stat_card(ft.Icons.BUG_REPORT,  "1", "Bugs Fixed",   AMBER),
        ], spacing=12)

        graph       = self._build_contribution_graph()
        commit_rows = [self._commit_row(c) for c in self.COMMITS]

        commits_section = ft.Container(
            content=ft.Column(controls=[
                ft.Text("Commit History", size=16, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                ft.Container(
                    content=ft.Column(controls=commit_rows, spacing=0),
                    bgcolor=SURFACE, border_radius=12,
                    border=ft.Border.all(1, BORDER),
                    clip_behavior=ft.ClipBehavior.HARD_EDGE,
                ),
            ], spacing=10),
        )

        screenshots = ft.Row(controls=[
            self._screenshot_card("15 Commits Overview", "screenshots/admin_pr_15_commits.png.jpeg"),
            self._screenshot_card("Pull Request Header", "screenshots/admin_pr_header.png.jpeg"),
        ], spacing=12)

        pr_cards   = [self._pr_card(p) for p in self.PULL_REQUESTS]
        pr_section = ft.Column(controls=[
            ft.Text("Pull Request Logs", size=16, weight=ft.FontWeight.W_700, color=TEXT_PRI),
            *pr_cards,
        ], spacing=8)

        impact_section = _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.STAR, color=AMBER, size=20),
                        ft.Text("Impact Summary", size=16, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                    ], spacing=8),
                    ft.Markdown(self.IMPACT_SUMMARY, selectable=True,
                                extension_set="gitHubFlavored"),
                ], spacing=10),
                bgcolor=SURFACE2, border_radius=12,
                padding=ft.Padding(left=16, right=16, top=16, bottom=16),
                border=ft.Border.all(1, AMBER + "55"),
            ),
            AMBER,
        )

        return ft.Column(controls=[
            hero, stats,
            ft.Divider(height=16, color="transparent"),
            graph,
            ft.Divider(height=16, color="transparent"),
            commits_section,
            ft.Divider(height=12, color="transparent"),
            ft.Text("Screenshots", size=16, weight=ft.FontWeight.W_700, color=TEXT_PRI),
            screenshots,
            ft.Divider(height=16, color="transparent"),
            pr_section,
            ft.Divider(height=16, color="transparent"),
            impact_section,
        ], spacing=4, scroll=ft.ScrollMode.AUTO)