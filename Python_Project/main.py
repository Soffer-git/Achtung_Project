import Player
import g_vs

import sys
import pygame
pygame.init()


if __name__ == "__main__":
    # Screen creation
    infoObject = pygame.display.Info()
    g_vs.WIDTH = infoObject.current_w
    g_vs.HEIGHT = infoObject.current_h
    screen = pygame.display.set_mode((g_vs.WIDTH, g_vs.HEIGHT), pygame.FULLSCREEN)

    # Players creation
    players_file = open(g_vs.PLAYERS_PATH)
    players_file_lines = players_file.readlines()
    assert g_vs.AMOUNT_OF_PLAYERS <= len(players_file_lines)
    players = []
    for line in players_file_lines:
        players.append(Player.Player(line))

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(g_vs.BACKGROUND_COLOR)
        pygame.display.flip()
