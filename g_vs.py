import pygame


COLOR_DICT = {
                 "Red": (255, 0, 0),
                 "Green": (0, 255, 0),
                 "Blue": (0, 0, 255),
                 "Pink": (255, 0, 200),
                 "Purple": (150, 0, 255),
                 "Orange": (200, 150, 0),
                 "Lime": (170, 120, 80),
                 "Brown": (150, 75, 0),
                 "Cyan": (0, 255, 255),
                 "Black": (0, 0, 0)
}


WIDTH = -1
HEIGHT = -1
# The minimum distance between the starting location of the players, and the edges of the screen.
BORDER_SIZE = (100, 100)
GAME_START_DELAY = 0.5
BACKGROUND_COLOR = COLOR_DICT["Black"]
AMOUNT_OF_PLAYERS = 4
THICKNESS = 5  # The thickness of the trails.
SPEED = 5
FRAMES_FOR_MOVE = 15
ITERS_FOR_TURN = 4
PLAYERS_PATH = "players_data.txt"
CHARACTER_IMAGE = "ball.jpg"  # The image used as the head of the players.


KEYS_DICT = {
    # Player 1
    "Left": pygame.K_LEFT,
    "Right": pygame.K_RIGHT,
    "Down": pygame.K_DOWN,

    # Player 2
    "1": pygame.K_1,
    "A": pygame.K_a,
    "Q": pygame.K_q,

    # Player 3
    "B": pygame.K_b,
    "M": pygame.K_m,
    "N": pygame.K_n,

    # Player 4
    "3": pygame.K_3,
    "9": pygame.K_9,
    "6": pygame.K_6,

    # Other keys
    "R": pygame.K_r,
    "Straight": "Straight",
    "Stop": "Stop"
}
