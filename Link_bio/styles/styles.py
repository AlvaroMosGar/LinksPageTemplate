import reflex as rx
from enum import Enum
from .colors import Color as co
from .colors import TextColor as tc
from .fonts import Font as fo
#Constantes
MAX_WIDTH = "550px"

#Tamaños
# 1em = 16px
class Size(Enum):
    ZERO = "0px"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"

#Estilos
BASE_STYLE = {
    "font_family": fo.DEFAULT.value,
    "html, body": {
        "margin": "0",  # Reiniciar margen
        "padding": "0",  # Reiniciar padding
        "width": "100%",  # Asegurar que ocupen el 100% del ancho
        "height": "100%",  # Asegurar que ocupen el 100% de la altura
    },

    "#main-box": {
        "background_color": co.BACKGROUND.value,
        "display": "flex",
        "flex_direction": "column",
        "min_height": "100vh"
    },
    rx.heading: {
        "size":"6",
        "color":tc.HEADER.value,
        "fon_family":fo.TITLE.value,
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "background_color": co.CONTENT.value,
        "color": tc.HEADER.value,
        "_hover": {
            "background_color": co.SECONDARY.value,
        }

    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {},
    }
}

navbar_tittle_style = dict(
    font_family=fo.LOGO.value,
    font_size=Size.LARGE.value,
)


tittle_style = dict(
    width="100%",
    padding_top = Size.DEFAULT.value,
)

button_title_style = dict(
    font_family=fo.TITLE.value,
    font_size = Size.DEFAULT.value,
    color=tc.HEADER.value,
)

button_body_style = dict(
    font_family=fo.DEFAULT.value,
    font_size = Size.MEDIUM.value,
    color=tc.BODY.value,
)