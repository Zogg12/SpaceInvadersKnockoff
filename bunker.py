from turtle import Turtle
from config import BunkerConfig

class Bunker(Turtle):

    def __init__(self):
        super().__init__()
        self.bunkers_list = []
        self.create_bunkers()


    def create_bunkers(self):
        bunker_positions = [-350, -150, 50, 250]  # X positions for the 4 bunkers

        for bunker_pos in bunker_positions:
            # Create a bunker composed of small squares
            self.create_single_bunker(bunker_pos)


    def create_single_bunker(self, x_start):
        # Create a bunker made of rows and columns of small squares
        for row_num in range(BunkerConfig.NR_ROWS):
            for col_num in range(BunkerConfig.ROW_L):
                bunker_piece = Turtle(BunkerConfig.SHAPE)
                bunker_piece.shapesize(*BunkerConfig.SIZE)  # Unpack the tuple
                bunker_piece.penup()
                bunker_piece.color(BunkerConfig.COLOR)

                # Position each piece relative to the bunker start position
                x = x_start + col_num * BunkerConfig.X_SPACING
                y = BunkerConfig.Y_START + row_num * BunkerConfig.Y_SPACING
                bunker_piece.goto(x, y)

                self.bunkers_list.append(bunker_piece)

    def reset_screen(self):
        for bunker in self.bunkers_list:
            bunker.hideturtle()
        self.bunkers_list.clear()
        self.create_bunkers()