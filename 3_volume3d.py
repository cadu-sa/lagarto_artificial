from manim import *

class volume3D(ThreeDScene):
    def construct(self):
        # Configurar a câmera para uma cena 3D
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Configura a cena inicial com o cubo e adiciona label
        cube = Cube(side_length=2)
        self.play(Create(cube), run_time=2)

        # Transformação do cubo em um prisma e adiciona label
        prism = Prism(dimensions=[3, 5, 1])
        self.play(Transform(cube, prism), run_time=3)

        # Transformação do prisma em um cilindro e adiciona label
        cylinder = Cylinder(radius=1, height=4)
        self.play(Transform(cube, cylinder), run_time=3)
        
        # Transformação do cilindro em um cone, move para a origem e adiciona label
        cone = Cone(base_radius=2, height=3, direction=OUT, show_base=True).move_to(ORIGIN)
        self.play(Transform(cube, cone), run_time=3)
        
        # Transformação do cone em um toro e adiciona label
        torus = Torus(major_radius=2, minor_radius=1)
        self.play(Transform(cube, torus), run_time=3)
        
        # Transformação do toro em uma esfera e adiciona label
        sphere = Sphere(radius=2)
        self.play(Transform(cube, sphere), run_time=3)
        
        # Configura a cena final com a esfera
        self.play(Uncreate(cube), run_time=2)

volume3D()
