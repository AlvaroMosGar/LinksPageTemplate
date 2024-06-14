import reflex as rx

import Link_bio.styles.styles as sty

def title(text: str) -> rx.Component:
   return rx.heading(
        text,
        size="7",
        style=sty.tittle_style,
    )