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


class Como_se_crean_matematicas1(Scene):
    def setup(self, add_border=False):
        if add_border:
            self.border = Rectangle(
                width=FRAME_WIDTH,
                height=FRAME_HEIGHT,
                color=WHITE,
            )
            self.add(self.border)
            
    def construct(self):
        title = Tex(r"¿Cómo se crean las matemáticas?")
        title2 = MathTex(r"p \rightarrow q", tex_template=extraTemplate)
        title3 = MathTex(r"q \vee \neg\; p", tex_template=extraTemplate)
        VGroup(title, title2, title3).arrange(DOWN)
        self.play(
            FadeIn(title),
            Write(title2, shift=DOWN),
            Write(title3, shift=DOWN),
        )
        self.wait(4.5)
        

        formulas1 = []
        formulas1 += Tex(r"Un Teorema es un predicado,")
        formulas1 += Tex(r"o afirmación cierta.")
        VGroup(*formulas1).arrange(DOWN)
        self.play(
            FadeTransform(title, formulas1[0]),
            FadeTransformPieces(title2, formulas1[1]),
            FadeOut(title3)
        )
        self.wait(12)

        
        dots = [Dot([-2, -1, 0]), Dot([2, 1, 0]), Dot([2, -1, 0])]
        lines = [Line(dot1.get_center(), dot2.get_center()) for dot1, dot2 in zip(dots, [*dots[1:], dots[0]])]
        a = MathTex(r"a").next_to(lines[2], DOWN)
        b = MathTex(r"b").next_to(lines[1], RIGHT)
        c = MathTex(r"c").next_to(lines[0], 0.01*UP)
        
        theorem = Tex(r"Teorema de Pitágoras:").next_to(c, 4*UP)

        formula = MathTex(r"a^2 + b^2 = c^2").next_to(a, 2*DOWN)
        self.play(
            FadeIn(theorem),
            *[FadeTransform(f1, f2) for f1, f2 in zip(formulas1, dots[:2])],
            FadeIn(dots[2], *lines, a, b, c, formula),
        )
        self.wait(9)
        
        
        texts1 = [Tex("Un axioma es una verdad previa"),
                  Tex("que debemos tomar como cierta"),
                  Tex("sin necesidad de demostración.")]
        VGroup(*texts1).arrange(DOWN)
        self.play(
            FadeOut(VGroup(*dots, *lines, a, b, c, formula, theorem)),
            FadeIn(*texts1),
        )
        
        self.wait(13.5)
        
        
        dots2 = [Dot(2*(2*LEFT+DOWN)), Dot(2*(2*RIGHT+UP))]
        union = Line((2*LEFT+DOWN)*8, (2*RIGHT+UP)*8)
        self.play(
            *[FadeTransform(t, d) for t, d in zip(texts1, dots2)],
            FadeOut(texts1[-1]),
        )
        self.wait(2)
        self.play(
            FadeIn(union),
        )
        self.wait(3)
        
        
        texts2 = [MathTex(r"0\in \mathbb{N}", tex_template=extraTemplate)]
        self.play(
            FadeOut(VGroup(*dots2), union),
            FadeIn(*texts2),
        )
        self.wait(3)
        self.play(FadeOut(*texts2))
        
        
        
        texts3 = [MathTex(r"\text{Axiomas} \rightarrow \text{Teoremas}", tex_template=extraTemplate)]
        self.play(
            FadeIn(*texts3),
        )
        
        self.wait(5)
        
        texts4 = [Tex(r"Lógica de predicados", tex_template=extraTemplate)]
        self.play(
            FadeTransform(*texts3, *texts4),
        )
        
        self.wait(9.5)
        
        texts5 = [MathTex(r"p\vee q"), MathTex(r"\neg p")]
        VGroup(*texts5).arrange(DOWN)
        self.play(
            FadeTransform(*texts4, texts5[0]),
        )
        self.wait(8)
        
        self.play(FadeIn(texts5[1]))
        self.wait(4)
        
        
        
class Como_se_crean_matematicas2(Scene):
    def setup(self, add_border=False):
        if add_border:
            self.border = Rectangle(
                width=FRAME_WIDTH,
                height=FRAME_HEIGHT,
                color=WHITE,
            )
            self.add(self.border)
            
    def construct(self):
        texts1 = [MathTex(r"p\rightarrow q"), MathTex(r"q\vee \neg \;p")]
        VGroup(*texts1).arrange(DOWN)
        self.play(
            FadeIn(texts1[0]),
        )
        self.wait(7.5)
        self.play(
            FadeIn(texts1[1]),
        )
        
        
        texts2 = [
            Tex(r"Teorema:"),
            Tex(r"Tú eres mortal"),
            MathTex(r"\text{EsMortal(Tú)}")]
        VGroup(*texts2).arrange(DOWN)
        
        
        self.wait(12)
        
        
        self.play(
            *[FadeTransform(t1, t2) for t1, t2 in zip(texts1, texts2)],
            FadeIn(texts2[2]),
        )
        self.wait(3)

        
        texts3 = [
            Tex(r"Axiomas:\\"),
            Tex(r"EsPersona(Tú)"),
            MathTex(r"\forall x \;\; \text{EsPersona(x)} \rightarrow \text{EsMortal(x)}")
        ]
        VGroup(*texts3).arrange(DOWN)
        
        self.play(
            FadeOut(*texts2),
            FadeIn(texts3[0]),   
        )
        
        self.wait(2.5)
        self.play(FadeIn(texts3[1]))
        
        self.wait(4)
        self.play(FadeIn(texts3[2]))
        self.wait(2)
        
        texts3_1 = [Tex(r"Conclusiones:\\").next_to(texts3[0], DOWN*0), texts3[1].copy(),
                    MathTex(r" \text{EsPersona(Tú)} \rightarrow \text{EsMortal(Tú)}").next_to(texts3[2], DOWN*0)]
        self.play(
            FadeTransform(texts3[0], texts3_1[0]),
        )
        self.wait(2)
        self.play(
            FadeTransform(texts3[2], texts3_1[2]))
        self.wait(4)
        
        texts3_2 = [texts3_1[0].copy(), texts3_1[1].copy(),
                    MathTex(r"\text{EsMortal(Tú)} \vee \neg \text{EsPersona(Tú)}").next_to(texts3_1[2], DOWN*0)]
        
        
        self.play(
            FadeTransform(texts3_1[2], texts3_2[2]))
        
        self.wait(22)
        
        texts3_3 = [texts3_2[0].copy(),
                    MathTex(r"\text{EsMortal(Tú)}").next_to(texts3_2[2], DOWN*0)]
        self.play(
            FadeOut(texts3[1]),
            FadeTransform(texts3_2[2], texts3_3[1]))
        self.wait(8)
        
        
        self.play(
            FadeOut(texts3_1[0], texts3_3[1]),)
        self.wait(8)
        
        
        texts4 = [Tex(r"Es casi imposible que sean nuestros juicios", font_size=30),
                  Tex(r"tan puros y tan sólidos como lo fuera si,", font_size=30),
                  Tex(r"desde el momento de nacer, tuviéramos el", font_size=30),
                  Tex(r"uso pleno de nuestra razón y no hubiéramos", font_size=30),
                  Tex(r"sido nunca dirigidos más que por ésta", font_size=30)
                ]
        VGroup(*texts4).arrange(DOWN)
        
        self.play(FadeIn(*texts4))
        
        self.wait(40)