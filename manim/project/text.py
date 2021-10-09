from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello World", font_size=144)
        self.add(text)

class SingleLineColor(Scene):
    def construct(self):
        text = MarkupText(f'all in red <span fgcolor="{YELLOW}">except this</span>', color=RED)
        self.add(text)

# manimpango.list_fonts()で使えるfontを確認
class FontsExample(Scene):
    def construct(self):
        ft = Text("Noto Sans", font="Noto Sans")
        self.add(ft)

# style of text
class SlantsExample(Scene):
    def construct(self):
        a = Text("Italic", slant=ITALIC) # or OBLIQUE
        self.add(a)

class DifferentWeight(Scene):
    def construct(self):
        import manimpango

        g = VGroup()
        weight_list = dict(sorted({weight: manimpango.Weight(weight).value for weight in manimpango.Weight}.items(), key=lambda x: x[1]))
        for weight in weight_list:
            g += Text(weight.name, weight=weight.name, font="Open Sans")
        self.add(g.arrange(DOWN).scale(0.5))