from turtle import Turtle
from config import UFOConfig
import random

class UFO(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(UFOConfig.SHAPE)
        self.color(UFOConfig.COLOR)
        self.shapesize(*UFOConfig.SIZE)
        self.penup()
        self.speed(0)
        self.hideturtle()

    def appear(self):
        self.goto(*UFOConfig.START_POS)
        self.showturtle()

    def move(self):
        self.setx(self.xcor() + UFOConfig.MOVE_DISTANCE)
        if self.xcor() > UFOConfig.RIGHT_WALL:
            self.hideturtle()
            return False
        return True

    def hit(self):
        self.hideturtle()
        return UFOConfig.POINTS
