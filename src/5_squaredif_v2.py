from manim import *

SCALE = 2
RUN_TIME = 1

class BinomialSquareVisualization(Scene):
    def construct(self):
        # Equação
        binomial_square1 = MathTex("(x - y)^2", "=", "{{x}}^2", "-", "2","xy", "+", "{{y}}^2").to_edge(UP)
        self.play(Write(binomial_square1), run_time=1.5)
        binomial_square2 = MathTex("(x - y)","(x - y)", "=", "{{x}}^2", "-", "xy", "-", "xy", "+", "{{y}}^2").to_edge(UP)
        self.play(TransformMatchingTex(binomial_square1, binomial_square2), run_time=1.5)
        binomial_square3 = MathTex("(x - y)","(x - y)", "=", "xx", "-", "xy", "-", "yx", "+", "yy").to_edge(UP)
        self.play(TransformMatchingTex(binomial_square2, binomial_square3), run_time=1.5)

        # Criação dos quadrados menores
        square_x2 = Square(side_length=3, fill_color=RED, fill_opacity=0.5).shift(DOWN + LEFT*3.5) #x^2
        square_y2 = Square(side_length=1, fill_color=YELLOW, fill_opacity=0.5).next_to(square_x2, buff=0.7) #y^2
        rectangle_xy = Rectangle(width=3, height=1, fill_color=BLUE, fill_opacity=0.5).next_to(square_y2, buff=0.7) #xy
        rectangle_yx = Rectangle(width=1, height=3, fill_color=BLUE, fill_opacity=0.5).next_to(rectangle_xy, buff=0.7) #yx

        # Transforma o texto em quadrado e retângulo
        binomial_square3_x2 = binomial_square3[3].copy() # xx
        binomial_square3_y2 = binomial_square3[9].copy() # yy
        binomial_square3_xy = binomial_square3[5].copy() # xy
        binomial_square3_yx = binomial_square3[7].copy() # yx

        self.play(Transform(binomial_square3_x2, square_x2), run_time=RUN_TIME)
        self.play(Transform(binomial_square3_y2, square_y2), run_time=RUN_TIME)
        self.play(Transform(binomial_square3_xy, rectangle_xy), run_time=RUN_TIME)
        self.play(Transform(binomial_square3_yx, rectangle_yx), run_time=RUN_TIME)

        # Adicionar textos x e y
        x_text_square_x2 = MathTex("x").next_to(square_x2, LEFT, buff=0.1)
        y_text_square_x2 = MathTex("x").next_to(square_x2, DOWN, buff=0.1)
        x_text_rectangle_xy = MathTex("x").next_to(rectangle_xy, DOWN, buff=0.1)
        y_text_rectangle_xy = MathTex("y").next_to(rectangle_xy, LEFT, buff=0.1)
        y_text_rectangle_yx = MathTex("y").next_to(rectangle_yx, DOWN, buff=0.1)
        x_text_rectangle_yx = MathTex("x").next_to(rectangle_yx, LEFT, buff=0.1)
        x_text_square_y2 = MathTex("y").next_to(square_y2, LEFT, buff=0.1)
        y_text_square_y2 = MathTex("y").next_to(square_y2, DOWN, buff=0.1)

        self.play(Create(x_text_square_x2),
                  Create(y_text_square_x2),
                  Create(x_text_rectangle_xy),
                  Create(y_text_rectangle_xy),
                  Create(x_text_rectangle_yx),
                  Create(y_text_rectangle_yx),
                  Create(x_text_square_y2),
                  Create(y_text_square_y2),
                  run_time=RUN_TIME)

        self.wait(1)

        # Retirar textos x e y
        self.play(
        Uncreate(x_text_square_x2),
        Uncreate(y_text_square_x2),
        Uncreate(x_text_rectangle_xy),
        Uncreate(y_text_rectangle_xy),
        Uncreate(x_text_rectangle_yx),
        Uncreate(y_text_rectangle_yx),
        Uncreate(x_text_square_y2),
        Uncreate(y_text_square_y2)
        )

        # Animação para posicionar os quadrados e retângulos
        self.play(Indicate(binomial_square3[3], color=RED, scale_factor=SCALE), run_time=RUN_TIME) 
        self.play(Indicate(binomial_square3_x2, color=RED), run_time=RUN_TIME)

        self.play(binomial_square3_x2.animate.move_to(UP))

        self.play(Indicate(binomial_square3[5], color=BLUE, scale_factor=SCALE), run_time=RUN_TIME)
        self.play(Indicate(binomial_square3_xy, color=BLUE), run_time=RUN_TIME)
        
        self.play(binomial_square3_xy.animate.move_to(UP*2))

        self.play(Circumscribe(binomial_square3[4], color=YELLOW), run_time=RUN_TIME + 0.5)

        target_square_x2 = Rectangle(width=3, height=2, fill_color=RED, fill_opacity=0.5)
        target_square_x2.next_to(binomial_square3_xy, DOWN, buff=0)

        self.play(
            binomial_square3_xy.animate.set_opacity(0),
            Transform(binomial_square3_x2, target_square_x2, run_time=0.5)
        )

        self.play(Indicate(binomial_square3[9], color=YELLOW, scale_factor=SCALE), run_time=RUN_TIME)
        self.play(Indicate(binomial_square3_y2, color=YELLOW), run_time=RUN_TIME)

        self.play(
            binomial_square3_y2.animate.move_to(UP*2+LEFT),  # Mover square_x2 para a posição desejada
        )

        self.play(Indicate(binomial_square3[7], color=BLUE, scale_factor=SCALE), run_time=RUN_TIME)
        self.play(Indicate(binomial_square3_yx, color=BLUE), run_time=RUN_TIME)

        self.play(
            binomial_square3_yx.animate.move_to(UP+LEFT)  # Coloca rectangle_xy abaixo de square_x2
        )

        self.play(Circumscribe(binomial_square3[6], color=YELLOW), run_time=RUN_TIME+0.5)

        target_square_x2 = Rectangle(width=2, height=2, fill_color=RED, fill_opacity=0.5)
        target_square_x2.next_to(binomial_square3_y2, RIGHT+DOWN, buff=0)

        self.play(
            binomial_square3_yx.animate.set_opacity(0),
            binomial_square3_y2.animate.set_opacity(0),
            Transform(binomial_square3_x2, target_square_x2, run_time=0.5)
        )

        self.play(
            binomial_square3_x2.animate.move_to(ORIGIN)
        )
       
        # Adicionar textos x - y
        xy_text_square1 = MathTex("x-y").next_to(binomial_square3_x2, LEFT, buff=0.1)
        xy_text_square2 = MathTex("x-y").next_to(binomial_square3_x2, DOWN, buff=0.1)

        self.play(Create(xy_text_square1), 
                  Create(xy_text_square2),
                  run_time=RUN_TIME)

        # Retirar textos x - y
        self.play(
        Uncreate(xy_text_square1),
        Uncreate(xy_text_square2)
        )

        self.play(Indicate(binomial_square3[0:2], color=WHITE, scale_factor=SCALE), run_time=1)
        self.play(Indicate(VGroup(binomial_square3_x2), color=WHITE), run_time=RUN_TIME)

        self.wait(1)

        # Finalizar a cena
        self.play(FadeOut(binomial_square3_x2, binomial_square3), run_time=1.5)