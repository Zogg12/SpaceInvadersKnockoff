from turtle import Screen
from alien import Alien
from bullet import Bullet
from config import UFOConfig
from player import Player
from bunker import Bunker
from scoreboard import Scoreboard
from ufo import UFO
import random


def reset_game(aliens, player, bullets, bunkers, scoreboard, level):
    aliens.reset_screen(level)
    player.reset_screen()
    bullets.reset_screen()
    bunkers.reset_screen()
    scoreboard.level_up(level)

def main():
    screen = Screen()
    screen.setup(800, 800)
    screen.bgcolor("black")
    screen.title("Space Invaders")
    screen.tracer(0)

    scoreboard = Scoreboard()
    player = Player()
    bunkers = Bunker()
    aliens = Alien()
    bullets = Bullet(player, bunkers.bunkers_list, aliens.aliens_list, aliens.shooter_columns)
    ufo = UFO()

    screen.listen()
    screen.onkeypress(player.move_left, "Left")
    screen.onkeypress(player.move_right, "Right")
    screen.onkeypress(bullets.player_shoot, "space")

    aliens.move_aliens()
    bullets.move_bullet()
    bullets.alien_shoot()

    level = 1
    game_is_on = True
    ufo_active = False

    while game_is_on:
        screen.update()
        scoreboard.display_lives(player.lives)

        if player.lives <= 0:
            game_is_on = False
            scoreboard.game_over()
        
        if len(aliens.aliens_list) == 0:
            level += 1
            reset_game(aliens, player, bullets, bunkers, scoreboard, level)

        if not ufo_active and random.random() < UFOConfig.APPEARANCE_CHANCE:
            ufo.appear()
            ufo_active = True

        if ufo_active:
            ufo_active = ufo.move()

    screen.exitonclick()

if __name__ == "__main__":
    main()
