from math import cos, sin, sqrt
import numpy as np
from manim import *

class ExampleSphere(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=PI / 3, theta=PI / 3)
        sphere = Sphere(radius = 1, stroke_width = 2, checkerboard_colors=[BLUE, BLUE], fill_opacity=0.3, fill_color = BLUE)
        self.add(sphere)

# class GridSphere(ThreeDScene):
#     def construct(self):
#         r = 2
#         sphere = Sphere(radius = r, stroke_width = 2, checkerboard_colors=[RED_D, RED_C], fill_opacity=0.9, fill_color = BLUE)
#         line = Line([0,0,0],[3,3,3], color = WHITE)
#         axes = ThreeDAxes()

#         # This supposedly makes the 2D objects compatible with the 3D scene
#         line.set_shade_in_3d(True)

#         self.set_camera_orientation(phi = 70*DEGREES, theta = -30*DEGREES)
#         self.add(sphere,line,axes)

#         #Begin camera rotation - at some angles the line 'pop's out' - However the 3D axes seem fine
#         self.begin_ambient_camera_rotation(rate=0.8)

#         self.wait(10)

class GridSphere(ThreeDScene):
    def construct(self):
        r = 2
        sphere = Sphere(radius = r, stroke_width = 2, checkerboard_colors=[BLUE, BLUE], fill_opacity=0.3, fill_color = BLUE)
        theta = PI / 6
        phi = 5 * PI / 12
        x = np.array([sin(theta) * cos(phi), sin(theta) * sin(phi), cos(theta)])
        x2 = np.array([sin(theta) * cos(phi), sin(theta) * sin(phi), 0])
        r = 0.6
        point_sp = Point(location=x, color = RED)
        point_2d = Point(location=x2, color = RED)
        line_sp = Line3D([0,0,0], point_sp, color = WHITE)
        line_2d = Line3D([0,0,0], point_2d, color = WHITE)
        line_z = Line3D([0,0,-1], [0,0,1], color = WHITE)
        line_x = Line3D([-1,0,0], [1,0,0], color = WHITE)
        axes = ThreeDAxes()
        # angle_theta = Angle(line_z, line_sp)
        # angle_phi = Angle(line_x, line_2d)

        self.set_camera_orientation(phi=PI / 3, theta=PI / 6)
        self.add(sphere, line_sp, line_2d, point_sp, point_2d, axes)
