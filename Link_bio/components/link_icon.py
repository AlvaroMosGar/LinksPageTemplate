import reflex as rx
import Link_bio.styles.styles as sty


def link_icon(url: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag="brick-wall"
        ),
        href=url,
        is_external=True,
    )