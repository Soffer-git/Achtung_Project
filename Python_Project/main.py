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
    # screen = pygame.display.set_mode((g_vs.WIDTH, g_vs.HEIGHT), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((g_vs.WIDTH, g_vs.HEIGHT))
    screen.fill(g_vs.BACKGROUND_COLOR)

    # Players creation
    players_file = open(g_vs.PLAYERS_PATH)
    players_file_lines = players_file.readlines()
    assert g_vs.AMOUNT_OF_PLAYERS <= len(players_file_lines)
    players = []
    for line in players_file_lines:
        players.append(Player.Player(line))
    curr_turn = 0

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                for player in players:
                    if player.l_key == event.key:
                        player.last_pressed = player.l_key
                    if player.r_key == event.key:
                        player.last_pressed = player.r_key
            if event.type == pygame.KEYUP:
                for player in players:
                    if player.l_key == event.key:
                        player.last_pressed = None
                    if player.r_key == event.key:
                        player.last_pressed = None

        if curr_turn == g_vs.FRAMES_FOR_MOVE:
            for player in players:
                player.move()
                pygame.draw.circle(screen, player.color, player.pos, g_vs.RADIUS, width=0)
                pygame.display.update()
            curr_turn = 0
        else:
            curr_turn += 1

        pygame.display.flip()
