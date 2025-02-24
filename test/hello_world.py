from manimlib import *

class HelloWorld(InteractiveScene):
    def construct(self):
        circle = Circle()
        square = Square()
        self.add(circle)
        self.add(square)


