import reflex as rx

from Link_bio.components.link_button import link_button
from Link_bio.components.title import title
from Link_bio.styles.styles import Size
import Link_bio.constants as cons

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Twitch",
            cons.TWITCH,
            "Directos todos los dias"
        ),
        link_button(
            "Youtube",
            cons.YOUTUBE,
            "Videos resubidos"
        ),
        link_button(
            "Youtube",
            cons.YOUTUBE,
            "Tutoriales",
        ),
        link_button(
            "Discord",
            cons.DISCORD,
            "Discord de la comunidad"
        ),
        title("Comunidad"),
        link_button(
            "Twitch",
            cons.YOUTUBE,
            "Directos todos los dias"
        ),
        link_button(
            "Youtube",
            cons.YOUTUBE,
            "Videos resubidos"
        ),
        link_button(
            "Youtube",
            cons.YOUTUBE,
            "Tutoriales",
        ),
        link_button(
            "Discord",
            cons.DISCORD,
            "Discord de la comunidad"
        ),
        title("Contacto"),
        link_button(
            "Email",
            f"mailto:{cons.EMAIL}",
            cons.EMAIL

        ),
        width="100%",
    ),