from turtle import Turtle, Screen
from config import BulletConfig, AlienConfig
from scoreboard import Scoreboard
import random

screen = Screen()
scoreboard = Scoreboard()

class Bullet(Turtle):

    def __init__(self, player, bunkers, aliens, shooters):
        super().__init__()
        self.player = player
        self.bunkers = bunkers
        self.aliens = aliens
        self.shooters = shooters
        self.bullets_list = []
        self.can_shoot = True
        self.move_bullet()


    def create_bullet(self, shooter):
        bullet = Turtle(BulletConfig.SHAPE)
        bullet.color(BulletConfig.COLOR)
        bullet.shapesize(*BulletConfig.SIZE)
        bullet.penup()
        self.place_bullet(shooter, bullet)
        self.bullets_list.append(bullet)


    def player_shoot(self):
        """Create a bullet from the player's position."""
        if self.can_shoot:
            self.create_bullet(self.player)


    def alien_shoot(self):
        """Randomly choose an alien to shoot from the first aliens in each column."""
        if self.shooters:
            shooter = random.choice(self.shooters)
            self.create_bullet(shooter)
        screen.ontimer(self.alien_shoot, random.randint(*BulletConfig.A_SHOOT_DELAY))


    def place_bullet(self, shooter, bullet):
        bullet.setheading(90)
        if shooter == self.player:
            bullet.setposition(shooter.xcor(), shooter.ycor() + 40)
            bullet.bullet_type = "player"
            self.can_shoot = False
            screen.ontimer(self.reset_shoot, BulletConfig.P_SHOOT_DELAY)
        else:
            bullet.setposition(shooter.xcor(), shooter.ycor() - 40)
            bullet.bullet_type = "alien"


    def move_bullet(self):
        for bullet in self.bullets_list:
            if bullet.bullet_type == "player":
                bullet.sety(bullet.ycor() + BulletConfig.MOVE_DIST_P)
            else:
                bullet.sety(bullet.ycor() - BulletConfig.MOVE_DIST_A)
        self.collision()
        screen.ontimer(self.move_bullet, BulletConfig.SPEED)


    def collision(self):
        for bullet in self.bullets_list[:]:  # Copy of the list to avoid modification during iteration
            for bunker in self.bunkers[:]:
                if bullet.distance(bunker) < BulletConfig.THRESHOLD:
                    bunker.hideturtle()
                    self.bunkers.remove(bunker)
                    bullet.hideturtle()
                    self.bullets_list.remove(bullet)
                    break

            for alien in self.aliens[:]:
                if bullet.distance(alien) < BulletConfig.THRESHOLD and bullet.bullet_type == "player":
                    alien.hideturtle()
                    self.aliens.remove(alien)
                    bullet.hideturtle()
                    self.bullets_list.remove(bullet)
                    scoreboard.increase_score(AlienConfig.POINTS)
                    break

            if bullet.distance(self.player) < BulletConfig.THRESHOLD:
                self.player.destroyed()
                bullet.hideturtle()
                self.bullets_list.remove(bullet)

            if bullet.ycor() > BulletConfig.CEILING or bullet.ycor() < BulletConfig.FLOOR:
                bullet.hideturtle()
                self.bullets_list.remove(bullet)


    def reset_shoot(self):
        """Allow the player to shoot again after cooldown."""
        self.can_shoot = True

    def reset_screen(self):
        for bullet in self.bullets_list:
            bullet.hideturtle()
        self.bullets_list.clear()
        self.can_shoot = True
