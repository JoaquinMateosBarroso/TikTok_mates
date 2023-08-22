from manim import *

phone_format = False
if phone_format:
    SCALE_FACTOR = 0.6
    # flip with to height, height to with
    config.pixel_height, config.pixel_width = config.pixel_width, config.pixel_height 
    # Change coord system dimensions
    config.frame_height = config.frame_height / SCALE_FACTOR
    config.frame_width = config.frame_height * 10/16
    FRAME_HEIGHT = config.frame_height
    FRAME_WIDTH = config.pixel_width

# A template to use the bbm package
extraTemplate = TexTemplate()
extraTemplate.add_to_preamble(r"\usepackage{mathrsfs}")


class Que_son_las_matematicas(Scene):
    def setup(self, add_border=False):
        if add_border:
            self.border = Rectangle(
                width=FRAME_WIDTH,
                height=FRAME_HEIGHT,
                color=WHITE,
            )
            self.add(self.border)
            
    def construct(self):
        title = Tex(r"¿Qué son las matemáticas?")
        basel = MathTex(r"e^{i \pi} + 1 = 0")
        VGroup(title, basel).arrange(DOWN)
        self.play(
            FadeIn(title),
            Write(basel, shift=DOWN),
        )
        self.wait(6.5)
        

        formulas = []
        formulas += Tex(r"Ecuación de segundo grado:")
        formulas += MathTex(r"ax^2 + bx + c = 0\Rightarrow")
        formulas += MathTex(r"\Rightarrow \frac{-b\pm\sqrt{b^2-4ac}}{2a}")
        formulas += Tex(r"Vértice de una parábola:")
        formulas += MathTex(r"y=ax^2+bx+c \Rightarrow x_v = \frac{-b}{2a}")
        formulas += Tex(r"Derivada de un polinomio:")
        formulas += MathTex(r"f(x) = x^n \Rightarrow f'(x) = nx^{n-1}")
        formulas += Tex(r"Máximo de una función acotada:")
        formulas += MathTex(r"f: I \rightarrow \mathbb{R} \Rightarrow f'(x_{max}) = 0", tex_template=extraTemplate)
        VGroup(*formulas).arrange(DOWN)
        self.play(
            FadeTransform(title, formulas[0]),
            FadeTransformPieces(basel, formulas[1]),
            FadeIn(formulas[2], shift=DOWN)
        )
        self.play(
            FadeIn(*formulas[3:5], shift=DOWN)
        )
        self.play(
            FadeIn(*formulas[5:7], shift=DOWN)
        )
        self.play(
            FadeIn(*formulas[7:], shift=DOWN)
        )
        self.wait(6)
        
        infinity = MathTex(r"\infty", font_size=150)
        self.play(
            FadeTransform(formulas[0], infinity),
            FadeOut(*formulas[1:]),
        )
        self.wait(3)
        
        
        infinity2 = MathTex(r"\infty", font_size=80)
        infinity2.move_to(LEFT)
        cardinals = MathTex(r" = \#\mathbb{N} = \aleph_0 < \aleph_1 = \#\mathbb{R}",
                            tex_template=extraTemplate, font_size=60)
        VGroup(infinity2, cardinals).arrange(RIGHT)
        self.play(
            FadeTransform(infinity, infinity2),
            FadeIn(cardinals),
        )
        self.wait(4.5)
        
        
        nDots = 9
        lineSize = 7
        d1=Dot(point=(-lineSize/2, 0, 0), color=GREEN, radius=DEFAULT_DOT_RADIUS*1.5)
        d2=Dot(point=(lineSize/2, 0, 0), color=GREEN, radius=DEFAULT_DOT_RADIUS*1.5)
        dGroup = VGroup(*[Dot(point= RIGHT*(-lineSize/2 + lineSize*(i+1)/(nDots+1)),
                              color=BLUE) for i in range(nDots)])
        l1=Line(d1.get_center(),d2.get_center()).set_color(WHITE)

        self.play(
            FadeOut(infinity2),
            FadeIn(d1,d2),
            FadeTransform(cardinals, l1),
            )
        self.bring_to_back(l1)
        self.wait(1)
        for i, dot in enumerate(dGroup):
            self.add(dot)
            self.wait(0.05)
            self.play(
                dot.animate.shift(UP * 3 + RIGHT * lineSize *((nDots//2+1)/(nDots+1) - (i+1)/(2*(nDots+1)) - 1/4)),
                      run_time=0.1
                      )
        self.wait(4)
        
        
class Que_son_las_matematicas2(Scene):
    def setup(self, add_border=False):
        if add_border:
            self.border = Rectangle(
                width=FRAME_WIDTH,
                height=FRAME_HEIGHT,
                color=WHITE,
            )
            self.add(self.border)
            
    def construct(self):
        text = [Tex(r"m\'athema,"), Tex(r"``conocimiento'' en griego")]
        VGroup(*text).arrange(DOWN)
        self.play(
            FadeIn(*text),
        )
        self.wait(13)
        
        
        text2 = [Tex(r"Las matemáticas son"), Tex(r"el juego más grande jamás creado")]
        VGroup(*text2).arrange(DOWN)
        self.play(
            FadeTransform(text[0], text2[0]),
            FadeTransform(text[1], text2[1]),
        )
        self.wait(3)
        
        
        text3 = [Tex(r"Un juego en el que las reglas"), Tex(r"las pone Dios")]
        VGroup(*text3).arrange(DOWN)
        self.play(
            FadeTransform(text2[0], text3[0]),
            FadeTransform(text2[1], text3[1]),
        )
        self.wait(4)

