import reflex as rx

from Link_bio.components.navbar import navbar
from Link_bio.views.header.header import header
from Link_bio.views.links.links import links
from Link_bio.components.footer import footer
import Link_bio.styles.styles as sty

class State(rx.State):
    pass 

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=sty.MAX_WIDTH,
                width="100%",
                margin_y=sty.Size.BIG.value,
            ),
        ),
        footer(),
        id="main-box",
    ),




app = rx.App(
    style=sty.BASE_STYLE,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Comfortaa:wght@300..700&family=Poppins:wght@300;400;700&display=swap",
    ]
)
app.add_page(index)