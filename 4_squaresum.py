from manim import *


class BinomialSquareVisualization(Scene):
    def construct(self):
        # Título da cena
        title = MathTex("(x + y)^2", "=", "{{x}}^2", "+", "2","xy", "+", "{{y}}^2").to_edge(UP)
        self.play(Write(title), run_time=2)
        title2 = MathTex("(x + y)","(x + y)", "=", "{{x}}^2", "+", "xy", "+", "xy", "+", "{{y}}^2").to_edge(UP)
        self.play(TransformMatchingTex(title, title2), run_time=2)
        title3 = MathTex("(x + y)","(x + y)", "=", "xx", "+", "xy", "+", "xy", "+", "yy").to_edge(UP)
        self.play(TransformMatchingTex(title2, title3), run_time=2)

        # Criação dos quadrados menores
        square_x2 = Square(side_length=1, fill_color=RED, fill_opacity=0.5).shift(LEFT*3) #x^2
        square_y2 = Square(side_length=2, fill_color=YELLOW, fill_opacity=0.5).next_to(square_x2, buff=1) #y^2
        rectangle_xy1 = Rectangle(width=1, height=2, fill_color=BLUE, fill_opacity=0.5).next_to(square_y2, buff=1) #xy
        rectangle_xy2 = Rectangle(width=1, height=2, fill_color=BLUE, fill_opacity=0.5).next_to(rectangle_xy1, buff=1) #xy

        # Mostrar os quadrados menores
        self.play(Create(square_x2), run_time=1)
        self.play(Create(square_y2), run_time=1)
        self.play(Create(rectangle_xy1), run_time=1)
        self.play(Create(rectangle_xy2), run_time=1)
        self.wait(1)

        # Adicionar textos x e y
        x_text_square_x2 = MathTex("x").next_to(square_x2, LEFT, buff=0.1)
        y_text_square_x2 = MathTex("x").next_to(square_x2, DOWN, buff=0.1)
        x_text_rectangle_xy1 = MathTex("x").next_to(rectangle_xy1, DOWN, buff=0.1)
        y_text_rectangle_xy1 = MathTex("y").next_to(rectangle_xy1, LEFT, buff=0.1)
        x_text_rectangle_xy2 = MathTex("x").next_to(rectangle_xy2, DOWN, buff=0.1)
        y_text_rectangle_xy2 = MathTex("y").next_to(rectangle_xy2, LEFT, buff=0.1)
        y_text_square_y2 = MathTex("y").next_to(square_y2, LEFT, buff=0.1)
        y_text_square_y2_below = MathTex("y").next_to(square_y2, DOWN, buff=0.1)


        SCALE = 2

        self.play(ScaleInPlace(title3[3], SCALE))
        self.play(Create(x_text_square_x2), run_time=0.5)
        self.play(Create(y_text_square_x2), run_time=0.5)
        self.play(ScaleInPlace(title3[3], 1/SCALE))  # Retorna o termo ao tamanho original

        self.play(ScaleInPlace(title3[5], SCALE))
        self.play(Create(x_text_rectangle_xy1), run_time=0.5)
        self.play(Create(y_text_rectangle_xy1), run_time=0.5)
        self.play(ScaleInPlace(title3[5], 1/SCALE))
        
        self.play(ScaleInPlace(title3[7], SCALE))
        self.play(Create(x_text_rectangle_xy2), run_time=0.5)
        self.play(Create(y_text_rectangle_xy2), run_time=0.5)
        self.play(ScaleInPlace(title3[7], 1/SCALE))

        self.play(ScaleInPlace(title3[9], SCALE))
        self.play(Create(y_text_square_y2), run_time=0.5)
        self.play(Create(y_text_square_y2_below), run_time=0.5)
        self.play(ScaleInPlace(title3[9], 1/SCALE))


        self.play(
        Uncreate(x_text_square_x2),
        Uncreate(y_text_square_x2),
        Uncreate(x_text_rectangle_xy1),
        Uncreate(y_text_rectangle_xy1),
        Uncreate(x_text_rectangle_xy2),
        Uncreate(y_text_rectangle_xy2),
        Uncreate(y_text_square_y2),
        Uncreate(y_text_square_y2_below)
        )

        # Animação para posicionar os quadrados e retângulos
        self.play(
            square_x2.animate.move_to(LEFT + UP)  # Mover square_x2 para a posição desejada
        )

        # Animação para posicionar os quadrados e retângulos
        self.play(
            rectangle_xy1.animate.next_to(square_x2, DOWN, buff=0)  # Coloca rectangle_xy1 abaixo de square_x2
        )


        # Rotacionar o rectangle_xy2 para ficar "deitado"
        self.play(Rotate(rectangle_xy2, angle=PI / 2, run_time=1.5))   # Rotaciona 90 graus para ficar horizontal

        # Animação para posicionar os quadrados e retângulos
        self.play(
            rectangle_xy2.animate.next_to(square_x2, RIGHT, buff=0)  # Coloca rectangle_xy2 à direita de square_x2
        )

        # Animação para posicionar os quadrados e retângulos
        self.play(
            square_y2.animate.next_to(rectangle_xy2, DOWN, buff=0)  # Coloca square_y2 abaixo de rectangle_xy2
        )

        
        # Desenho do quadrado final (x + y)^2
        big_square = Square(side_length=3, fill_opacity=0.1).move_to(ORIGIN)
        self.play(Create(big_square), run_time=1)
        
        xy_text_square1 = MathTex("x+y").next_to(big_square, LEFT, buff=0.1)
        xy_text_square2 = MathTex("x+y").next_to(big_square, DOWN, buff=0.1)

        self.play(ScaleInPlace(title3[0], SCALE))
        self.play(Create(xy_text_square1))
        self.play(ScaleInPlace(title3[0], 1/SCALE))

        self.play(ScaleInPlace(title3[1], SCALE))
        self.play(Create(xy_text_square2))
        self.play(ScaleInPlace(title3[1], 1/SCALE))

        self.play(
        Uncreate(xy_text_square1),
        Uncreate(xy_text_square2)
        )
        self.wait(1)

        # animação final
        self.play(ScaleInPlace(title3[3], SCALE))
        self.play(Indicate(square_x2))
        self.play(ScaleInPlace(title3[3], 1/SCALE))  # Retorna o termo ao tamanho original

        self.play(ScaleInPlace(title3[9], SCALE))
        self.play(Indicate(square_y2))
        self.play(ScaleInPlace(title3[9], 1/SCALE))
        
        self.play(ScaleInPlace(title3[5], SCALE))
        self.play(Indicate(rectangle_xy1))
        self.play(ScaleInPlace(title3[5], 1/SCALE))

        self.play(ScaleInPlace(title3[7], SCALE))
        self.play(Indicate(rectangle_xy2))
        self.play(ScaleInPlace(title3[7], 1/SCALE))

        self.play(ScaleInPlace(title3[0:2], SCALE))
        self.play(Indicate(big_square))
        self.play(ScaleInPlace(title3[0:2], 1/SCALE))

        self.wait(1)

        # Finalizar a cena
        self.play(FadeOut(big_square, xy_text_square1, xy_text_square2, square_y2, rectangle_xy2, rectangle_xy1, square_x2, title3), run_time=2)