import reflex as rx
import Link_bio.styles.styles as sty
from Link_bio.styles.styles import Size

def link_button(text: str, url: str, des: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                        tag="minus",
                        width=Size.BIG.value,
                        height=Size.BIG.value,
                        margin=Size.MEDIUM.value,

                ),
                rx.vstack(
                    rx.heading(text, style=sty.button_title_style),
                    rx.text(des, style=sty.button_body_style, size="1"),
                    spacing="0",
                    align_items="start",
                    margin=Size.ZERO.value,
                ),
                align="center",
            ),
        ),
        href=url,
        is_external=True,
        width="100%"
    ),
    
 