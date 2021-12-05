from manim import *
from manim.utils.color import Colors

class Favicon(Scene):
    def construct(self):
        MY_PINK = "#eF45FF"
        MY_BLUE = "#2a7ae2"
        rect = Circle(color=BLACK)
        rect.set_fill(color=WHITE, opacity=1.0)
        self.add(rect)

        text = Text("Kota Takeda", gradient=(MY_PINK, MY_BLUE), font_size=20, font="Segoe UI", fill_opacity=0.9)
        self.add(text)
