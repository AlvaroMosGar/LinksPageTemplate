import reflex as rx
import datetime

from Link_bio.components.link_icon import link_icon
from Link_bio.components.info_text import info_text
from Link_bio.components.title import title
from Link_bio.styles.colors import TextColor as tc
from Link_bio.styles.colors import Color as co
from Link_bio.styles.styles import Size as sz
from Link_bio.styles.fonts import Font as fo

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                fallback="M",
                size="9",
                radius="full",
                src="capybara_adobespark.png",
                border="4px solid",
                border_color=co.PRIMARY.value
            ),
            rx.vstack(
                rx.heading("MANOLO"),
                rx.text(
                    "@Manolo",
                    margin_top=sz.ZERO.value,
                    color=tc.BODY.value,
                ),
                rx.hstack(
                    link_icon("https://x.com/?lang=es"),
                    link_icon("https://x.com/?lang=es"),
                    link_icon("https://x.com/?lang=es"),
                ),
                align_items ="start",
            ),
            align="center",
            spacing="3"
        ),
        rx.flex(
            info_text(f"+{experience()}","años de experiencia"),
            rx.spacer(),
            info_text(f"+{experience()}","años de experiencia"),
            rx.spacer(),
            info_text(f"+{experience()}","años de experiencia"),
            width="100%",
        ),
        rx.text(
            """
            (Presentacion)
            """,
            color= tc.BODY.value
        ),
        spacing="3",
        align_items ="start",
        width="100%"
    ),

def experience() -> int:
    return datetime.date.today().year - 2023