from manim import *

class MyName(Scene):
    def construct(self):
        tex = Tex(r"{{K}}ota {{T}}akeda", font_size=144)
        tex.set_color_by_tex("K", BLUE_C)
        tex.set_color_by_tex("T", BLUE_B)
        self.add(tex)

class DataAssimilation(Scene):
    def construct(self):
        tex = MathTex(r"x_n &= M(x_{n-1}) + \zeta_n\\ y_n &= H(x_n) + \eta_n")
        self.add(tex)