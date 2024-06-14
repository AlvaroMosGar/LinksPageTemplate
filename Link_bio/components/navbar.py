import reflex as rx

import Link_bio.styles.styles as sty
from Link_bio.styles.colors import Color as co

def navbar() -> rx.Component:
    return rx.hstack(
        rx.chakra.box(
            rx.chakra.span("manolo", color=co.PRIMARY.value),
            rx.chakra.span("dev", color=co.SECONDARY.value),
            style=sty.navbar_tittle_style,
        ),
        position="sticky",
        bg=co.CONTENT.value,
        padding_x=sty.Size.BIG.value,
        padding_y=sty.Size.DEFAULT.value,
        z_index="999",
        top = "0"
    ),