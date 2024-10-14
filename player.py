from turtle import Turtle, Screen
from config import PlayerConfig
from time import sleep


screen = Screen()

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.lives = PlayerConfig.LIVES
        self.setup()


    def setup(self):
        self.shape(PlayerConfig.SHAPE)
        self.color(PlayerConfig.COLOR)
        self.shapesize(*PlayerConfig.SIZE)
        self.penup()
        self.speed(0)
        self.goto(*PlayerConfig.START_POS)
        self.setheading(90)


    def move_left(self):
        if self.xcor() > PlayerConfig.LEFT_WALL:
            self.setx(self.xcor() - PlayerConfig.MOVE_DISTANCE)


    def move_right(self):
        if self.xcor() < PlayerConfig.RIGHT_WALL:
            self.setx(self.xcor() + PlayerConfig.MOVE_DISTANCE)

    def destroyed(self):
        self.hideturtle()
        sleep(3)
        self.lives -= 1
        self.goto(*PlayerConfig.START_POS)
        self.showturtle()

    def reset_screen(self):
        self.lives = PlayerConfig.LIVES
        self.setup()