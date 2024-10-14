from dataclasses import dataclass


@dataclass(frozen=True)
class AlienConfig:
    X_START: int = -370
    Y_START: int = 200
    ROW_L: int = 11
    NR_ROWS: int = 5
    Y_SPACING: int = 40
    X_SPACING: int = 45
    COLOR: str = "white"
    SHAPE: str = "turtle"
    RIGHT_WALL: int = 375
    LEFT_WALL: int = -375
    EARTH: int = -375
    APPROACH_DISTANCE: int = 25
    MOVE_DISTANCE: int = 2.5
    SPEED: int = 200
    SIZE: tuple = (2, 0.75)  # stretch_wid, stretch_len
    POINTS: int = 10
    SPEED_INCREASE: float = 0.8
    APPROACH_INCREASE: float = 1.2


@dataclass(frozen=True)
class PlayerConfig:
    SHAPE: str = "turtle"
    COLOR: str = "green"
    SIZE: tuple = (2.5, 1.5)  # stretch_wid, stretch_len
    MOVE_DISTANCE: int = 10
    RIGHT_WALL: int = 375
    LEFT_WALL: int = -375
    LIVES: int = 3
    START_POS: tuple = (0, -350)


@dataclass(frozen=True)
class BunkerConfig:
    SHAPE: str = "square"
    COLOR: str = "green"
    SIZE: tuple = (0.5, 1)  # stretch_wid, stretch_len
    X_START: int = -300
    Y_START: int = -290
    ROW_L: int = 5
    NR_ROWS: int = 3
    Y_SPACING: int = 11
    X_SPACING: int = 21


@dataclass(frozen=True)
class BulletConfig:
    SHAPE: str = "circle"
    COLOR: str = "green"
    SIZE: tuple = (0.15, 0.75)  # stretch_wid, stretch_len
    SPEED: int = 15
    MOVE_DIST_P: int = 5
    MOVE_DIST_A: int = 2
    CEILING: int = 410
    FLOOR: int = -410
    THRESHOLD: int = 13
    P_SHOOT_DELAY: int = 1000
    A_SHOOT_DELAY: tuple = 1000, 3000


@dataclass(frozen=True)
class ScoreboardConfig:
    COLOR: str = "white"
    FONT: tuple = ("Courier", 24, "normal")
    GAME_OVER_FONT: tuple = ("Courier", 36, "normal")
    SCORE_POS: tuple = (-380, 360)
    LIVES_POS: tuple = (380, 360)
    LEVEL_POS: tuple = (0, 360)


@dataclass(frozen=True)
class UFOConfig:
    SHAPE: str = "circle"
    COLOR: str = "red"
    SIZE: tuple = (1, 2)  # stretch_wid, stretch_len
    START_POS: tuple = (-400, 300)
    MOVE_DISTANCE: int = 5
    RIGHT_WALL: int = 400
    POINTS: int = 50
    APPEARANCE_CHANCE: float = 0.005  # 0.5% chance each frame
