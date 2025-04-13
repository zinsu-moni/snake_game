# from turtle import Turtle
# import random

# class Food(Turtle):
#     def __init__(self):
#         super().init()
#         self.shape("circle")
#         self.penup()
#         self.color("red")
#         self.speed(0)
#         self.refresh()

#     def refresh(self):
#         x = random.randint(-280, 280)
#         y = random.randint(-280, 280)
#         self.goto(x, y)

# import turtle
# import random

# class Food(turtle.Turtle):
#     def init(self):
#         super().init()
#         self.shape("circle")
#         self.color("red")
#         self.penup()
#         self.speed(0)
#         self.refresh()

#     def refresh(self):
#         x = random.randint(-280, 280)
#         y = random.randint(-280, 280)
#         self.goto(x, y)
#     def refresh(self):
#         x = random.randint(-280, 280)
#         y = random.randint(-280, 280)
#         self.goto(x, y)

from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):  # Fixed method name
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed(0)
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)