from manim import *


class WriteText(Scene):
    def construct(self):
        # MathTexに分けて数式を入れることで部分的に表示できる．
        text = MathTex(
            "N \\rightarrow \\infty", ", \\Gamma \\sim N^{-1}", ",\\beta \\sim N \\Gamma^{-2}"
        )
        self.play(Write(text[0]))
        self.wait()
        self.play(Write(text[1]))
        self.wait()
        self.play(Write(text[2]))
