import Player
import g_vs
import pygame
import sys
import time


pygame.init()


def make_transparent(image, color):
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            if image.get_at((x, y)) == color:
                image.set_at((x, y), g_vs.COLOR_DICT["Transparent"])
    return image


if __name__ == "__main__":
    # Screen creation
    infoObject = pygame.display.Info()
    g_vs.WIDTH = infoObject.current_w  # Using the width of the computer screen the window is presented on.
    g_vs.HEIGHT = infoObject.current_h  # Using the height of the computer screen the window is presented on.
    # screen = pygame.display.set_mode((g_vs.WIDTH, g_vs.HEIGHT), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((g_vs.WIDTH, g_vs.HEIGHT))
    head = make_transparent(pygame.image.load(g_vs.HEAD_IMAGE), g_vs.COLOR_DICT["Black"])

    window_runs = True
    while window_runs:
        screen.fill(g_vs.BACKGROUND_COLOR)

        # Players creation
        players_file = open(g_vs.PLAYERS_PATH)
        players_file_lines = players_file.readlines()
        assert g_vs.AMOUNT_OF_PLAYERS <= len(players_file_lines)
        players = []
        for line in players_file_lines:
            players.append(Player.Player(line))
        for player in players:
            screen.blit(head, (player.pos[0] - g_vs.HEAD_RADIUS, player.pos[1] - g_vs.HEAD_RADIUS))
        pygame.display.update()
        for player in players:
            pygame.draw.circle(screen, player.color, player.pos, g_vs.THICKNESS, width=0)

        time_before_start = time.perf_counter()
        curr_turn = 0
        time_exceeded_delay = False
        game_runs = True

        while game_runs:
            if not time_exceeded_delay:
                curr_time = time.perf_counter()
                if curr_time - time_before_start >= g_vs.GAME_START_DELAY:
                    time_exceeded_delay = True
                    for player in players:
                        player.turn_direction = g_vs.KEYS_DICT["Straight"]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window_runs = False
                    game_runs = False
                if event.type == pygame.KEYDOWN:
                    if event.key == g_vs.KEYS_DICT["Reset"]:
                        game_runs = False
                    elif time_exceeded_delay:
                        for player in players:
                            if event.key == player.l_key:
                                player.l_pressed = True
                                player.turn_direction = player.l_key
                            if event.key == player.r_key:
                                player.r_pressed = True
                                player.turn_direction = player.r_key
                if event.type == pygame.KEYUP:
                    if time_exceeded_delay:
                        for player in players:
                            if event.key == player.l_key:
                                player.l_pressed = False
                                if player.r_pressed:
                                    player.turn_direction = player.r_key
                                else:
                                    player.turn_direction = "Straight"
                            if event.key == player.r_key:
                                player.r_pressed = False
                                if player.l_pressed:
                                    player.turn_direction = player.l_key
                                else:
                                    player.turn_direction = "Straight"
            if time_exceeded_delay:
                if curr_turn == g_vs.FRAMES_FOR_MOVE:
                    for player in players:
                        player.manage_movement()
                        screen.blit(head, (player.pos[0] - g_vs.HEAD_RADIUS, player.pos[1] - g_vs.HEAD_RADIUS))
                    pygame.display.update()
                    for player in players:
                        pygame.draw.circle(screen, player.color, player.pos, g_vs.THICKNESS, width=0)
                    curr_turn = 0
                else:
                    curr_turn += 1
    sys.exit()
