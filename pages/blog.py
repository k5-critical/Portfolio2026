import flet as ft
import math

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


def _estimate_read_time(content: str) -> str:
    words   = len(content.split())
    minutes = max(1, math.ceil(words / 200))
    return f"{minutes} min read"


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


class BlogPage:
    POSTS = [
        {
            "title": "Theory of Structures: Understanding Beam Analysis",
            "date": "10 Jun 2026",
            "summary": "Fundamentals of analyzing bending moments and shear forces in structural members.",
            "content": """## Beam Analysis Fundamentals

Beams are one of the most common structural elements in civil engineering. Understanding how they respond to loads is crucial for structural design.

### Key Concepts:
- Bending moments and shear forces
- Support reactions
- Deflection calculations
- Load types: point loads, distributed loads, moments

### Applications:
Beam theory is used in designing bridges, buildings, floors, and any horizontal structural member.
""",
            "video_url": "https://www.youtube.com/watch?v=sTc3P8KSG-8",
            "video_thumb": "https://img.youtube.com/vi/sTc3P8KSG-8/hqdefault.jpg",
            "tags": ["Theory of Structures", "Civil Engineering", "Structural Analysis"],
        },
        {
            "title": "Introduction to Geology: Rock Types and Formation",
            "date": "11 Jun 2026",
            "summary": "Understanding the three main rock types and their formation processes.",
            "content": """## Rock Classification and Formation

Geology studies Earth's materials, structure, and processes. Rocks are classified into three main categories:

### Igneous Rocks
- Form from cooling magma
- Granite, basalt, obsidian

### Sedimentary Rocks
- Form from weathered rock fragments
- Sandstone, limestone, shale

### Metamorphic Rocks
- Form under heat and pressure
- Marble, slate, schist

Understanding rocks is essential for construction, mining, and environmental assessment.
""",
            "video_url": "https://www.youtube.com/watch?v=XwrUyKpuVwU",
            "video_thumb": "https://img.youtube.com/vi/XwrUyKpuVwU/hqdefault.jpg",
            "tags": ["Introduction to Geology", "Earth Science", "Materials"],
        },
        {
            "title": "Computer Programming 1: Variables, Data Types, and Operations",
            "date": "12 Jun 2026",
            "summary": "Introduction to fundamental programming concepts for beginners.",
            "content": """## Programming Basics

Every program starts with understanding basic building blocks:

### Variables and Data Types
```
Integer: 42, -10, 0
Float: 3.14, 2.5, -0.001
String: "Hello", "World"
Boolean: True, False
```

### Basic Operations
- Arithmetic: +, -, *, /, %
- Comparison: ==, !=, <, >, <=, >=
- Logical: and, or, not

### Why It Matters
These fundamentals form the foundation for all programming tasks, from simple calculations to complex applications.
""",
            "video_url": "https://www.youtube.com/watch?v=M4lSit3d5W8",
            "video_thumb": "https://img.youtube.com/vi/M4lSit3d5W8/hqdefault.jpg",
            "tags": ["Computer Programming 1", "Programming Basics", "Python"],
        },
        {
            "title": "Engineering Math 3: Calculus Applications in Engineering",
            "date": "13 Jun 2026",
            "summary": "Practical applications of derivatives and integrals in engineering problems.",
            "content": """## Calculus in Engineering

Calculus is essential for solving real-world engineering problems:

### Derivatives
- Rate of change analysis
- Optimization (maxima and minima)
- Velocity and acceleration

### Integrals
- Area and volume calculations
- Work and energy
- Cumulative quantities

### Real-World Examples
- Finding maximum stress in a beam
- Calculating fluid flow rates
- Determining motion trajectories
- Energy consumption analysis
""",
            "video_url": "https://www.youtube.com/watch?v=WUvTyaaNkzM",
            "video_thumb": "https://img.youtube.com/vi/WUvTyaaNkzM/hqdefault.jpg",
            "tags": ["Engineering Math 3", "Calculus", "Mathematics"],
        },
        {
            "title": "Strength of Materials: Stress and Strain Relationships",
            "date": "14 Jun 2026",
            "summary": "Understanding how materials deform under load and the stress-strain relationship.",
            "content": """## Stress and Strain Fundamentals

Strength of Materials (Mechanics of Materials) examines how structures respond to loads.

### Key Definitions
- **Stress**: Force per unit area (Pa, N/m²)
- **Strain**: Change in dimension relative to original

### Types of Stress
- Tensile stress (pulling)
- Compressive stress (pushing)
- Shear stress (sliding)

### Material Behavior
- Elastic: Returns to original shape after load removal
- Plastic: Permanent deformation occurs
- Yield point: Transition between elastic and plastic

### Engineering Design
Understanding stress-strain relationships ensures structures are safe and efficient.
""",
            "video_url": "https://www.youtube.com/watch?v=oE-JlQ3dJko",
            "video_thumb": "https://img.youtube.com/vi/oE-JlQ3dJko/hqdefault.jpg",
            "tags": ["Strength of Materials", "Material Science", "Mechanics"],
        },
        {
            "title": "Advanced Structural Design: Load Paths and Safety Factors",
            "date": "15 Jun 2026",
            "summary": "How engineers ensure structures can safely handle expected and unexpected loads.",
            "content": """## Structural Safety and Design Philosophy

### Load Paths
Understanding how loads transfer through a structure:
1. Applied loads (live, dead, wind, seismic)
2. Load transfer mechanism
3. Support reactions

### Safety Factors
- Factor of Safety (FOS) = Strength / Maximum Expected Stress
- Typical values: 1.5 - 3.0 depending on application
- Conservative design prevents failures

### Design Process
1. Identify loads and load combinations
2. Perform structural analysis
3. Design members with adequate strength
4. Check deflection and stability
5. Verify against design codes
""",
            "video_url": "https://www.youtube.com/watch?v=k8YXf3F2Fqc",
            "video_thumb": "https://img.youtube.com/vi/k8YXf3F2Fqc/hqdefault.jpg",
            "tags": ["Theory of Structures", "Civil Engineering", "Design"],
        },
    ]

    ALL_TAGS = sorted({tag for post in POSTS for tag in post["tags"]})

    def __init__(self):
        self._active_tag = None
        self._cards_ref  = ft.Ref[ft.Column]()

    def _tag_chip(self, label):
        return ft.Container(
            content=ft.Text(label, size=11, color=BLUE),
            bgcolor=BLUE + "22",
            padding=ft.Padding(left=10, right=10, top=4, bottom=4),
            border_radius=20,
            border=ft.Border.all(1, BLUE + "44"),
        )

    def _filter_chip(self, label, on_click):
        is_all = label == "All"
        active = (is_all and self._active_tag is None) or (label == self._active_tag)
        return ft.Container(
            content=ft.Text(label, size=12,
                            color=BG if active else TEXT_SEC,
                            weight=ft.FontWeight.W_600 if active else ft.FontWeight.W_400),
            bgcolor=ACCENT if active else SURFACE,
            padding=ft.Padding(left=14, right=14, top=6, bottom=6),
            border_radius=20,
            border=ft.Border.all(1, ACCENT if active else BORDER),
            on_click=on_click,
            ink=True,
        )

    def _extract_video_id(self, url):
        """Extract YouTube video ID from URL"""
        if "youtube.com/watch?v=" in url:
            return url.split("v=")[1].split("&")[0]
        elif "youtu.be/" in url:
            return url.split("youtu.be/")[1].split("?")[0]
        return None

    def _open_video_player_modal(self, video_url, post_title):
        """Create a modal video player"""
        video_id = self._extract_video_id(video_url)
        embed_url = f"https://www.youtube-nocookie.com/embed/{video_id}?autoplay=1" if video_id else video_url
        
        # Create an HTML5 embed code
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body {{ margin: 0; padding: 0; background: #0D1117; }}
                .video-container {{
                    position: relative;
                    width: 100%;
                    height: 100vh;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }}
                iframe {{
                    width: 100%;
                    height: 100%;
                    border: none;
                }}
            </style>
        </head>
        <body>
            <div class="video-container">
                <iframe 
                    src="{embed_url}"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen>
                </iframe>
            </div>
        </body>
        </html>
        """
        return html_content

    def _open_video_url(self, video_url, post_title="Video"):
        async def _handler(e):
            try:
                # Try to open in default browser first
                await e.page.launch_url(video_url)
            except:
                # Fallback to YouTube if direct open fails
                await e.page.launch_url(f"https://www.youtube.com/results?search_query={post_title}")
        return _handler

    def _build_video_section(self, video_url, thumb_url, post_title=""):
        video_id = self._extract_video_id(video_url)
        
        return ft.Container(
            content=ft.Column(controls=[
                ft.Text("📹 Video Reference", size=13, weight=ft.FontWeight.W_600, color=TEXT_PRI),
                ft.Container(
                    content=ft.Column(controls=[
                        ft.Container(
                            content=ft.Stack(controls=[
                                ft.Image(src=thumb_url, fit=ft.BoxFit.COVER, width=float("inf"), height=220,
                                         error_content=ft.Container(
                                             content=ft.Column(controls=[
                                                 ft.Icon(ft.Icons.PLAY_CIRCLE_FILLED, color=ACCENT, size=64),
                                                 ft.Text("Click to Play", color=TEXT_SEC, size=14),
                                             ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
                                                alignment=ft.MainAxisAlignment.CENTER),
                                             alignment=ft.Alignment(0, 0),
                                             bgcolor=SURFACE2,
                                         )),
                                ft.Container(
                                    content=ft.Icon(ft.Icons.PLAY_CIRCLE_FILLED, color="#FFFFFF", size=64),
                                    alignment=ft.Alignment(0, 0),
                                    bgcolor="#00000066",
                                    expand=True,
                                ),
                            ]),
                            border_radius=8,
                            clip_behavior=ft.ClipBehavior.HARD_EDGE,
                            height=220,
                            on_click=self._open_video_url(video_url, post_title),
                            ink=True,
                            expand=True,
                        ),
                        ft.Row(controls=[
                            ft.Icon(ft.Icons.INFO, size=14, color=ACCENT),
                            ft.Text("Click thumbnail to play video", size=11, color=TEXT_SEC),
                        ], spacing=6),
                    ], spacing=6, expand=True),
                    bgcolor=SURFACE2, border_radius=8,
                    padding=ft.Padding(left=12, right=12, top=12, bottom=12),
                    expand=True,
                ),
            ], spacing=8),
            bgcolor=SURFACE2, border_radius=8,
            padding=ft.Padding(left=12, right=12, top=12, bottom=12),
            margin=ft.Margin(left=0, right=0, top=8, bottom=0),
            border=ft.Border.all(1, BORDER),
            expand=True,
        )

    def _build_post_card(self, post):
        read_time   = _estimate_read_time(post["content"])
        content_col = ft.Column(
            controls=[ft.Markdown(post["content"], selectable=True,
                                  extension_set="gitHubFlavored",
                                  code_theme="atom-one-dark")],
            visible=False,
        )
        
        # Add video section with thumbnail
        if post.get("video_url") and post.get("video_thumb"):
            content_col.controls.append(
                self._build_video_section(post["video_url"], post["video_thumb"], post.get("title", ""))
            )
        
        # Add video reference link if available
        if post.get("video_url"):
            content_col.controls.append(
                ft.Container(
                    content=ft.Column(controls=[
                        ft.Text("📹 Video Link", size=13, weight=ft.FontWeight.W_600, color=TEXT_PRI),
                        ft.Row(controls=[
                            ft.Icon(ft.Icons.LINK, size=14, color=BLUE),
                            ft.Text("Open in new window:", size=12, color=TEXT_SEC),
                        ], spacing=6),
                        ft.TextButton(
                            post["video_url"],
                            url=post["video_url"],
                            style=ft.ButtonStyle(
                                color=BLUE,
                                padding=ft.Padding(left=0, right=0, top=0, bottom=0),
                            ),
                        ),
                        ft.Text("Copy or click the link to open the video", size=10, color=TEXT_SEC, italic=True),
                    ], spacing=4),
                    bgcolor=SURFACE2, border_radius=8,
                    padding=ft.Padding(left=12, right=12, top=12, bottom=12),
                    margin=ft.Margin(left=0, right=0, top=8, bottom=0),
                    border=ft.Border.all(1, BORDER),
                )
            )

        btn_text   = ft.Text("Read more ▾", color=ACCENT, size=13)
        expand_btn = ft.TextButton(content=btn_text)

        def toggle_expand(e, cc=content_col, bt=btn_text):
            cc.visible = not cc.visible
            bt.value   = "Read less ▴" if cc.visible else "Read more ▾"
            e.page.update()

        expand_btn.on_click = toggle_expand

        return _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Text(post["title"], size=15, weight=ft.FontWeight.W_700,
                                color=TEXT_PRI, expand=True),
                        ft.Text(post["date"], size=12, color=TEXT_SEC),
                    ]),
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.ACCESS_TIME, size=13, color=TEXT_SEC),
                        ft.Text(read_time, size=12, color=TEXT_SEC),
                    ], spacing=4),
                    ft.Text(post["summary"], size=13, color=TEXT_SEC),
                    ft.Row(controls=[self._tag_chip(t) for t in post["tags"]], spacing=6, wrap=True),
                    content_col,
                    expand_btn,
                ], spacing=8),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=16, right=16, top=16, bottom=16),
                border=ft.Border.all(1, BORDER),
                margin=ft.Margin(left=0, right=0, top=0, bottom=12),
            ),
            BLUE,
        )

    def _rebuild_cards(self, page):
        filtered = (self.POSTS if self._active_tag is None
                    else [p for p in self.POSTS if self._active_tag in p["tags"]])
        self._cards_ref.current.controls = [self._build_post_card(p) for p in filtered]
        page.update()

    def _make_filter_row(self, page):
        all_labels = ["All"] + self.ALL_TAGS

        def make_handler(label):
            def handler(e):
                self._active_tag = None if label == "All" else label
                filter_row.controls = [self._filter_chip(l, make_handler(l)) for l in all_labels]
                self._rebuild_cards(page)
            return handler

        filter_row = ft.Row(
            controls=[self._filter_chip(l, make_handler(l)) for l in all_labels],
            spacing=8, wrap=True,
        )
        return filter_row

    def build(self, page=None):
        hero = _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.ARTICLE, color=TEXT_PRI, size=28),
                        ft.Text("Technical Blog", size=24, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                    ], spacing=10),
                    ft.Text("Confidence in Concepts — written explanations of core programming and engineering topics.",
                            size=13, color=TEXT_SEC),
                    ft.Row(controls=[
                        ft.Container(
                            content=ft.Text(f"{len(self.POSTS)} Posts", size=12, color=ACCENT),
                            bgcolor=ACCENT_B + "33",
                            padding=ft.Padding(left=12, right=12, top=4, bottom=4),
                            border_radius=20,
                            border=ft.Border.all(1, ACCENT_B),
                        ),
                        ft.Container(
                            content=ft.Text(f"{len(self.ALL_TAGS)} Topics", size=12, color=BLUE),
                            bgcolor=BLUE + "22",
                            padding=ft.Padding(left=12, right=12, top=4, bottom=4),
                            border_radius=20,
                            border=ft.Border.all(1, BLUE + "44"),
                        ),
                    ], spacing=8),
                ], spacing=8),
                bgcolor=SURFACE, border_radius=16,
                padding=ft.Padding(left=24, right=24, top=24, bottom=24),
                margin=ft.Margin(left=0, right=0, top=0, bottom=16),
                border=ft.Border.all(1, BORDER),
            ),
            ACCENT,
        )

        cards_col  = ft.Column(ref=self._cards_ref,
                               controls=[self._build_post_card(p) for p in self.POSTS],
                               spacing=0)
        filter_row = self._make_filter_row(page) if page else ft.Row(spacing=8)

        return ft.Column(controls=[
            hero,
            ft.Text("Filter by Topic", size=13, weight=ft.FontWeight.W_600, color=TEXT_SEC),
            filter_row,
            ft.Divider(height=16, color="transparent"),
            cards_col,
        ], spacing=8, scroll=ft.ScrollMode.AUTO)