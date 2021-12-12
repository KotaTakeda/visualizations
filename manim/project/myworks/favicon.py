from manim import *
from manim.utils.color import Colors

class Favicon1(Scene):
    def construct(self):
        MY_PINK = "#eF45FF"
        MY_BLUE = "#2a7ae2"
        rect = Circle(color=BLACK)
        rect.set_fill(color=WHITE, opacity=1.0)
        self.add(rect)

        text = Text("Kota Takeda", gradient=(MY_PINK, MY_BLUE), font_size=20, font="Segoe UI", fill_opacity=0.9)
        self.add(text)

class Favicon2(Scene):
    def construct(self):
        MY_PINK = "#eF45FF"
        MY_BLUE = "#2a7ae2"
        logo_black = "#343434"
        rect = Circle(color=logo_black)
        rect.set_fill(color=WHITE, opacity=1.0)
        self.add(rect)

        K = MathTex(r"\mathbb{K}", fill_color=logo_black).scale(2)
        K.shift(0.25 * LEFT + 0.1 * UP)
        T = MathTex(r"\mathbb{T}", fill_color=logo_black).scale(2)
        T.shift(0.1 * RIGHT + 0.1 * DOWN)
        # text = Tex("Kota Takeda", gradient=(MY_PINK, MY_BLUE), font_size=20, font="Segoe UI", fill_opacity=0.9)
        logo = VGroup(T, K)
        logo.move_to(ORIGIN)
        self.add(logo)
