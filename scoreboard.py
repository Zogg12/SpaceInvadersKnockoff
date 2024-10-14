from turtle import Turtle
from config import ScoreboardConfig

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(ScoreboardConfig.COLOR)
        self.penup()
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(*ScoreboardConfig.SCORE_POS)
        self.write(f"Score: {self.score}", font=(ScoreboardConfig.FONT[0], ScoreboardConfig.FONT[1],
                                                 ScoreboardConfig.FONT[2]))


    def increase_score(self, points):
        self.score += points
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=(ScoreboardConfig.FONT[0], ScoreboardConfig.FONT[1],
                                                      ScoreboardConfig.FONT[2]))


    def display_lives(self, lives):
        self.clear()
        self.goto(*ScoreboardConfig.LIVES_POS)
        self.write(f"Lives: {lives}", align="right", font=(ScoreboardConfig.FONT[0], ScoreboardConfig.FONT[1],
                                                           ScoreboardConfig.FONT[2]))


    def level_up(self, level):
        self.goto(*ScoreboardConfig.LEVEL_POS)
        self.write(f"Level: {level}", align="center", font=(ScoreboardConfig.FONT[0], ScoreboardConfig.FONT[1],
                                                            ScoreboardConfig.FONT[2]))
