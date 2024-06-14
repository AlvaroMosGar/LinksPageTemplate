import reflex as rx
import datetime
import Link_bio.styles.styles as sty
from Link_bio.styles.colors import TextColor as tc

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"© 2024-{datetime.date.today().year} PAGE CREATE BY AlvaroMosGar v1.0.",
            href="https://github.com/AlvaroMosGar",
            is_external=True,
            color=tc.FOOTER.value,
        ),
        align="center",
        margin_bottom=sty.Size.BIG.value,
    )