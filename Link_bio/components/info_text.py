import reflex as rx
import Link_bio.styles.styles as sty
from Link_bio.styles.colors import TextColor as tc
from Link_bio.styles.colors import Color as co

def info_text(title:str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
            rx.text(
                title,
                color=co.PRIMARY.value,
                as_="span"),
            f" {body}",
            font_size=sty.Size.MEDIUM.value,
            color=tc.BODY.value,
        ),   
    )