# -*- coding: utf-8 -*-
from manim import *

class SinhPoisson(Scene):
    def construct(self):
        spe = MathTex(r"-\Delta", " \Psi", "=", "2 \sinh(-\\beta \Psi)")
        self.play(Write(spe[:2]))
        self.play(Write(spe[2]))
        self.play(Write(spe[3]))

        # self.play(FadeOut(spe[0]))
        # spe[0].set_color(RED)
        # self.play(FadeIn(spe[0]))

        # self.play(ApplyFunction(lambda mobject : mobject.shift(2*DOWN), spe[0]), FadeOut(spe[1], spe[2]))
        self.play(FadeOut(*spe[1:]))
        laplacian = Tex(r"$ = - \frac{1}{\sin\theta} \frac{\partial}{\partial \theta} \left(\sin\theta \frac{\partial}{\partial \theta} \right)$")
        laplacian.shift(RIGHT)
        self.play(Write(laplacian))
