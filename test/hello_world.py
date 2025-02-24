from manimlib import *

class HelloWorld(InteractiveScene):
    def construct(self):
        circle = Circle()
        square = Square()
        self.add(circle)
        self.add(square)

class LorenzAttractor(Scene):
    def construct(self):
        self.interactive_mode = True
        # Set up axes
        axes = ThreeDAxes(
            x_range=(-50, 50, 5),
            y_range=(-50, 50, 5),
            z_range=(-0, 50, 5),
            # width=16,
            # height=16,
            depth=8,
        )
        # axes.set_width(FRAME_WIDTH)
        axes.center()

        # self.frame.reorient(43, 76, 1, IN, 10)
        # self.frame.add_updater(lambda m, dt: m.increment_theta(dt * 3 * DEGREES))
        self.add(axes)

        # Add the equations
        equations = Tex(
            R"""
            \begin{aligned}
            \frac{\mathrm{d} x}{\mathrm{~d} t} & =\sigma(y-x) \\
            \frac{\mathrm{d} y}{\mathrm{~d} t} & =x(\rho-z)-y \\
            \frac{\mathrm{d} z}{\mathrm{~d} t} & =x y-\beta z
            \end{aligned}
            """,
            # t2c={
            #     "x": RED,
            #     "y": GREEN,
            #     "z": BLUE,
            # },
            tex_to_color_map={
                "x": RED,
                "y": GREEN,
                "z": BLUE,
            },
            font_size=30
        )
        # # equations.fix_in_frame()
        # equations.to_corner(UL)
        # # equations.set_backstroke()
        # self.play(Write(equations))

        # # Compute a set of solutions
        # epsilon = 1e-5
        # evolution_time = 30
        # n_points = 10
        # states = [
        #     [10, 10, 10 + n * epsilon]
        #     for n in range(n_points)
        # ]
        # colors = color_gradient([BLUE_E, BLUE_A], len(states))

        # curves = VGroup()
        # for state, color in zip(states, colors):
        #     points = ode_solution_points(lorenz_system, state, evolution_time)
        #     curve = VMobject().set_points_smoothly(axes.c2p(*points.T))
        #     curve.set_stroke(color, 1, opacity=0.25)
        #     curves.add(curve)

        # curves.set_stroke(width=2, opacity=1)

        # # Display dots moving along those trajectories
        # dots = Group(GlowDot(color=color, radius=0.25) for color in colors)

        # def update_dots(dots, curves=curves):
        #     for dot, curve in zip(dots, curves):
        #         dot.move_to(curve.get_end())

        # dots.add_updater(update_dots)

        # tail = VGroup(
        #     TracingTail(dot, time_traced=3).match_color(dot)
        #     for dot in dots
        # )

        # self.add(dots)
        # self.add(tail)
        # curves.set_opacity(0)
        # # self.play(
        # #     *(
        # #         ShowCreation(curve, rate_func=linear)
        # #         for curve in curves
        # #     ),
        # #     run_time=evolution_time,
        # # )
        # self.play(
        #     *(
        #         Create(curve, rate_func=linear)
        #         for curve in curves
        #     ),
        #     run_time=evolution_time,
        # )


