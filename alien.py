from turtle import Turtle, Screen
from config import AlienConfig

screen = Screen()

class Alien(Turtle):

    def __init__(self):
        super().__init__()
        self.aliens_list = []
        self.shooter_columns = []
        self.level = 1
        self.create_enemies()

    def create_enemies(self):
        while len(self.aliens_list) < AlienConfig.ROW_L * AlienConfig.NR_ROWS:  # 55 aliens
            alien = Turtle(AlienConfig.SHAPE)
            alien.shapesize(*AlienConfig.SIZE)
            alien.penup()
            alien.color(AlienConfig.COLOR)
            alien.setheading(-90)  # Point them downwards for shooting
            self.aliens_list.append(alien)

        for row_num in range(AlienConfig.NR_ROWS):
            x = AlienConfig.X_START
            y = AlienConfig.Y_START + row_num * AlienConfig.Y_SPACING
            for alien in self.aliens_list[AlienConfig.ROW_L * row_num: AlienConfig.ROW_L * (row_num + 1)]:
                alien.goto(x, y)
                x += AlienConfig.X_SPACING

        # Find first alien in each column
        self.update_shooter_columns()

        # Start alien movement
        self.move_aliens()

    def update_shooter_columns(self):
        """Update the list of first aliens in each column for shooting."""
        self.shooter_columns = []  # Reset the shooter columns list

        for col in range(AlienConfig.ROW_L):
            # Iterate from bottom to top (which is the original order in aliens_list)
            for row in range(AlienConfig.NR_ROWS):
                alien_index = col + row * AlienConfig.ROW_L

                if alien_index < len(self.aliens_list):
                    alien = self.aliens_list[alien_index]
                    if alien.isvisible():
                        self.shooter_columns.append(alien)
                        break  # Stop after finding the first visible alien in this column


    def move_aliens(self):
        """Move the aliens and handle the bouncing logic."""
        for alien in self.aliens_list:
            alien.setx(alien.xcor() + AlienConfig.MOVE_DISTANCE)
            alien.setheading(alien.heading() + 90)  # Rotate them after each move
        self.bounce()
        self.update_shooter_columns()
        screen.ontimer(self.move_aliens, AlienConfig.SPEED)


    def bounce(self):
        """Bounce aliens off the walls and make them approach."""
        for alien in self.aliens_list:
            if AlienConfig.MOVE_DISTANCE > 0 and alien.xcor() >= AlienConfig.RIGHT_WALL:
                AlienConfig.MOVE_DISTANCE *= -1
                self.approach()
            elif AlienConfig.MOVE_DISTANCE < 0 and alien.xcor() <= AlienConfig.LEFT_WALL:
                AlienConfig.MOVE_DISTANCE *= -1
                self.approach()


    def approach(self):
        """Move the aliens closer to Earth."""
        for alien in self.aliens_list:
            alien.sety(alien.ycor() - abs(AlienConfig.APPROACH_DISTANCE))


    def invaded(self):
        """Check if any alien has reached Earth."""
        for alien in self.aliens_list:
            if alien.ycor() <= AlienConfig.EARTH:
                return True
        return False


    def reset_screen(self, level):
        self.level = level
        for alien in self.aliens_list:
            alien.hideturtle()
        self.aliens_list.clear()
        self.shooter_columns.clear()
        AlienConfig.MOVE_DISTANCE *= AlienConfig.SPEED_INCREASE
        AlienConfig.APPROACH_DISTANCE *= AlienConfig.APPROACH_INCREASE
        AlienConfig.Y_START -= 20 * (level - 1)  # Lower starting position
        self.create_enemies()
