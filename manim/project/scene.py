from manim import *

class SquareToCircle(Scene):
    def construct(self): # derives from Scene
        # create a circle
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        # create a square
        square = Square()
        square.rotate(PI / 4)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(Create(circle)) # show the circle on screen