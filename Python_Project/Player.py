import g_vs

import random


def parse_player_line(line):
    arguments = line.strip().split(', ')
    return g_vs.COLOR_DICT[arguments[0]], \
           g_vs.KEYS_DICT[arguments[1]], \
           g_vs.KEYS_DICT[arguments[2]], \
           g_vs.KEYS_DICT[arguments[3]]


class Player:
    def __init__(self, line):
        assert g_vs.WIDTH != -1 and g_vs.HEIGHT != -1
        self.color, self.l_key, self.r_key, self_j = parse_player_line(line)
        self.curr_x = int(random.randint(g_vs.BORDER_SIZE[0], g_vs.WIDTH - g_vs.BORDER_SIZE[0]))
        self.curr_y = int(random.randint(g_vs.BORDER_SIZE[1], g_vs.HEIGHT - g_vs.BORDER_SIZE[1]))
