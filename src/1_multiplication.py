from manim import *

FONT_SIZE_TITLE = 50
FONT_SIZE_PROPERTIES = 45
FONT_SIZE_EXAMPLES = 40
FONT_SIZE_DEMO = 36
FONT_SIZE_VARIABLE = 36
IDEAL_TIME = 0.5
RUN_TIME = 2

class multiplicationProperties(Scene):
    def construct(self):
        # Título
        title = Text("Propriedades da Multiplicação", font_size=FONT_SIZE_TITLE, color=BLUE, font="Z003").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Comutatividade
        commutative_title = Text("Comutatividade", font_size=FONT_SIZE_PROPERTIES, color=GREEN, font="Z003").next_to(title, DOWN, buff=0.5)
        commutative_example = MathTex("a \\times b = b \\times a", font_size=FONT_SIZE_EXAMPLES, color=YELLOW).next_to(commutative_title, DOWN, buff=0.5)
        a_times_b = commutative_example[0][:3]  # a \\times b
        b_times_a = commutative_example[0][4:]  # b \\times a
        variable_example = Tex(r"Exemplo: seja $a = 3$ e $b = 4$", font_size=FONT_SIZE_VARIABLE).next_to(commutative_example, DOWN, buff=0.5)

        self.play(Write(commutative_title))
        self.wait(IDEAL_TIME)
        self.play(Write(commutative_example))
        self.wait(IDEAL_TIME)
        self.play(Write(variable_example))
        self.wait(IDEAL_TIME)

        commutative_demo = VGroup(
            MathTex("3 \\times 4 = 12", font_size=FONT_SIZE_DEMO, color=ORANGE),
            MathTex("4 \\times 3 = 12", font_size=FONT_SIZE_DEMO, color=ORANGE)
        ).arrange(DOWN).next_to(variable_example, DOWN, buff=0.5)

        self.play(a_times_b.animate.set_color(PURE_RED))
        self.play(Write(commutative_demo[0], run_time=(RUN_TIME-1)))
        self.play(a_times_b.animate.set_color(YELLOW))

        self.play(b_times_a.animate.set_color(PURE_RED))
        self.play(Write(commutative_demo[1], run_time=(RUN_TIME-1)))
        self.play(b_times_a.animate.set_color(YELLOW))
        self.wait(IDEAL_TIME)

        conclusion_example1 = Tex(r"Portanto,", font_size=FONT_SIZE_VARIABLE).next_to(commutative_demo, DOWN, buff=0.5)
        conclusion_example2 = MathTex("3 \\times 4 = 4 \\times 3", font_size=FONT_SIZE_DEMO, color=ORANGE).next_to(conclusion_example1, DOWN, buff=0.5)
        self.play(Write(conclusion_example1))
        self.wait(IDEAL_TIME)
        self.play(Write(conclusion_example2, run_time=RUN_TIME))

        self.wait(1)
        self.play(FadeOut(commutative_title), FadeOut(commutative_example), FadeOut(commutative_demo), FadeOut(variable_example), FadeOut(conclusion_example1), FadeOut(conclusion_example2))

        # Associatividade
        associative_title = Text("Associatividade", font_size=FONT_SIZE_PROPERTIES, color=GREEN, font="Z003").next_to(title, DOWN, buff=0.5)
        associative_example = MathTex("(a \\times b) \\times c = a \\times (b \\times c)", font_size=FONT_SIZE_EXAMPLES, color=YELLOW).next_to(associative_title, DOWN, buff=0.5)
        left_associative = associative_example[0][:7]  # (a \\times b)
        right_associative = associative_example[0][8:]  # (b \\times c)
        variable_example = Tex(r"Exemplo: seja $a = 2$, $b = 3$ e $c = 4$", font_size=FONT_SIZE_VARIABLE).next_to(associative_example, DOWN, buff=0.5)

        self.play(Write(associative_title))
        self.wait(IDEAL_TIME)
        self.play(Write(associative_example))
        self.wait(IDEAL_TIME)
        self.play(Write(variable_example))
        self.wait(IDEAL_TIME)

        associative_demo = VGroup(
            MathTex("(2 \\times 3) \\times 4 = 6 \\times 4 = 24", font_size=FONT_SIZE_DEMO, color=ORANGE),
            MathTex("2 \\times (3 \\times 4) = 2 \\times 12 = 24", font_size=FONT_SIZE_DEMO, color=ORANGE)
        ).arrange(DOWN).next_to(variable_example, DOWN, buff=0.5)

        self.play(left_associative.animate.set_color(PURE_RED))
        self.play(Write(associative_demo[0], run_time=RUN_TIME))
        self.play(left_associative.animate.set_color(YELLOW))

        self.play(right_associative.animate.set_color(PURE_RED))
        self.play(Write(associative_demo[1], run_time=RUN_TIME))
        self.play(right_associative.animate.set_color(YELLOW))
        self.wait(IDEAL_TIME)
        
        conclusion_example1 = Tex(r"Portanto,", font_size=FONT_SIZE_VARIABLE).next_to(associative_demo, DOWN, buff=0.5)
        conclusion_example2 = MathTex("(2 \\times 3) \\times 4 = 2 \\times (3 \\times 4)", font_size=FONT_SIZE_DEMO, color=ORANGE).next_to(conclusion_example1, DOWN, buff=0.5)
        self.play(Write(conclusion_example1))
        self.play(Write(conclusion_example2, run_time=RUN_TIME))

        self.wait(1)
        self.play(FadeOut(associative_title), FadeOut(associative_example), FadeOut(associative_demo), FadeOut(variable_example), FadeOut(conclusion_example1), FadeOut(conclusion_example2))

        # Distributividade
        distributive_title = Text("Distributividade", font_size=FONT_SIZE_PROPERTIES, color=GREEN, font="Z003").next_to(title, DOWN, buff=0.5)
        distributive_example = MathTex("a \\times (b + c) = a \\times b + a \\times c", font_size=FONT_SIZE_EXAMPLES, color=YELLOW).next_to(distributive_title, DOWN, buff=0.5)
        left_distributive = distributive_example[0][:7]  # a (b + c)
        right_distributive = distributive_example[0][8:]  # a \times b + a \times c
        variable_example = Tex(r"Exemplo: seja $a = 2$ e $b = 3$ e $c = 4$", font_size=FONT_SIZE_VARIABLE).next_to(distributive_example, DOWN, buff=0.5)

        self.play(Write(distributive_title))
        self.wait(IDEAL_TIME)
        self.play(Write(distributive_example))
        self.wait(IDEAL_TIME)
        self.play(Write(variable_example))
        self.wait(IDEAL_TIME)

        distributive_demo = VGroup(
            MathTex("2 \\times (3 + 4) = 2 \\times 7 = 14", font_size=FONT_SIZE_DEMO, color=ORANGE),
            MathTex("2 \\times 3 + 2 \\times 4 = 6 + 8 = 14", font_size=FONT_SIZE_DEMO, color=ORANGE)
        ).arrange(DOWN).next_to(variable_example, DOWN, buff=0.5)

        self.play(left_distributive.animate.set_color(PURE_RED))
        self.play(Write(distributive_demo[0], run_time=RUN_TIME))
        self.play(left_distributive.animate.set_color(YELLOW))

        self.play(right_distributive.animate.set_color(PURE_RED))
        self.play(Write(distributive_demo[1], run_time=RUN_TIME))
        self.play(right_distributive.animate.set_color(YELLOW))
        self.wait(IDEAL_TIME)
        
        conclusion_example1 = Tex(r"Portanto,", font_size=FONT_SIZE_VARIABLE).next_to(distributive_demo, DOWN, buff=0.5)
        conclusion_example2 = MathTex("2 \\times (3 + 4) = 2 \\times 3 + 2 \\times 4", font_size=FONT_SIZE_DEMO, color=ORANGE).next_to(conclusion_example1, DOWN, buff=0.5)
        self.play(Write(conclusion_example1))
        self.play(Write(conclusion_example2, run_time=RUN_TIME))

        self.wait(1)
        self.play(FadeOut(distributive_title), FadeOut(distributive_example), FadeOut(distributive_demo), FadeOut(variable_example), FadeOut(conclusion_example1), FadeOut(conclusion_example2))

        # Finalizar cena
        self.play(FadeOut(title))


multiplicationProperties()

# Para executar: abra o terminal e execute na pasta do arquivo:
# manim -pqh multiplication.py
