from manim import *

elements_to_fade_out = []

class BooleanOperations(Scene):
    def construct(self):
        ellipse1 = Ellipse(
            width=4.0, height=5.0, fill_opacity=0.5, color=BLUE, stroke_width=10
        ).move_to(LEFT)
        ellipse2 = ellipse1.copy().set_color(color=RED).move_to(RIGHT)
        bool_ops_text = MarkupText("<u>Operação de Conjuntos</u>").move_to(UP * 3 + LEFT * 2)
        ellipse_group = Group(ellipse1, ellipse2).move_to(LEFT * 2 + DOWN * 0.5)
        self.play(FadeIn(ellipse_group, bool_ops_text), run_time=2)

        elements_to_fade_out.append(ellipse_group)
        elements_to_fade_out.append(bool_ops_text)

        intersection = Intersection(ellipse1, ellipse2, color=GREEN, fill_opacity=0.5)
        self.play(intersection.animate.scale(0.35).move_to(RIGHT * 3 + UP * 1))
        intersection_text = Text("Interseção", font_size=23).next_to(intersection, UP)
        self.play(FadeIn(intersection_text))

        elements_to_fade_out.append(intersection)
        elements_to_fade_out.append(intersection_text)

        union = Union(ellipse1, ellipse2, color=ORANGE, fill_opacity=0.5)
        union_text = Text("União", font_size=23)
        self.play(union.animate.scale(0.3).next_to(intersection, DOWN * 5))
        union_text.next_to(union, UP)
        self.play(FadeIn(union_text))

        elements_to_fade_out.append(union)
        elements_to_fade_out.append(union_text)

        exclusion = Exclusion(ellipse1, ellipse2, color=YELLOW, fill_opacity=0.5)
        exclusion_text = Text("Diferença Simétrica", font_size=23)
        self.play(exclusion.animate.scale(0.3).next_to(intersection, RIGHT * 5))
        exclusion_text.next_to(exclusion, UP)
        self.play(FadeIn(exclusion_text))

        elements_to_fade_out.append(exclusion)
        elements_to_fade_out.append(exclusion_text)

        difference = Difference(ellipse1, ellipse2, color=PINK, fill_opacity=0.5)
        difference_text = Text("Diferença", font_size=23)
        self.play(difference.animate.scale(0.28).next_to(union, RIGHT * 5))
        difference_text.next_to(difference, UP)
        self.play(FadeIn(difference_text))

        elements_to_fade_out.append(difference)
        elements_to_fade_out.append(difference_text)
        
        #self.play(FadeOut(difference_text, exclusion_text, union_text, intersection_text, difference, exclusion, intersection, union, ellipse_group, bool_ops_text), run_time=2)
        self.play(FadeOut(*elements_to_fade_out), run_time=2)


BooleanOperations()