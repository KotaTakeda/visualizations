from manim import *

class HelloLaTeX(Scene):
    def construct(self):
        tex = Tex(r"\LaTeX", font_size=144) # or Tex("\\LaTeX", font_size=144)
        self.add(tex)

# Working with MathTex
# $$で囲むと数式が書ける
class MathTeXDemo(Scene):
    def construct(self):
        rtarrow0 = MathTex(r"\xrightarrow{x^6y^8}", font_size=96)
        rtarrow1 = Tex(r"$\xrightarrow{x^6y^8}$", font_size=96)

        self.add(VGroup(rtarrow0, rtarrow1).arrange(DOWN))

class AMSLaTeX(Scene):
    def construct(self):
        tex = Tex(r'$\mathtt{H} \looparrowright$ \LaTeX', font_size=144)
        self.add(tex)

class LaTeXAttributes(Scene):
    def construct(self):
        tex = Tex(r'Hello \LaTeX', color=BLUE, font_size=144) # color指定もできる
        self.add(tex)

# packageを追加できる
# TexTemplateのpreambleを利用する
class AddPackageLatex(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        tex = Tex(r'$\mathscr{H} \rightarrow \mathbb{H}$}', tex_template=myTemplate, font_size=144)
        self.add(tex)

# Substrings and parts
class LaTeXSubstrings(Scene):
    def construct(self):
        tex = Tex('Hello', r'$\bigstar$', r'\LaTeX', font_size=144)
        tex.set_color_by_tex('igsta', RED) # igstaを含むtex substring単位に色を指定
        # tex[1].set_color(RED) # これでも同じ
        self.add(tex)

class IncorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots"
        )
        equation.set_color_by_tex("x", YELLOW) # 全てに色がつく
        self.add(equation)

# xのみに色をつける．時間がかかる．
# substrings_to_isolateか{{}}を使ってsubstringを独立させる
class CorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            substrings_to_isolate="x" # xを独立させる
        )
        equation.set_color_by_tex("x", YELLOW) # xにのみ色がつく
        self.add(equation)

# TexFontTemplates
class LaTeXMathFonts(Scene):
    def construct(self):
        tex = Tex(r'$x^2 + y^2 = z^2$', tex_template=TexFontTemplates.french_cursive, font_size=144)
        self.add(tex)

# TexTemplateLibrary
class LaTeXTemplateLibrary(Scene):
    def construct(self):
        tex = Tex('Hello 你好 \\LaTeX', tex_template=TexTemplateLibrary.ctex, font_size=144)
        self.add(tex)

# Aligning formulae
class LaTeXAlignEnvironment(Scene):
    def construct(self):
        tex = MathTex(r'f(x) &= 3 + 2 + 1\\ &= 5 + 1 \\ &= 6', font_size=96)
        self.add(tex)