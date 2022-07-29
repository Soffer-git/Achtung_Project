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
        self.color, self.l_key, self.r_key, self.j_key = parse_player_line(line)
        # Add distance between starting points!
        self.pos = [int(random.randint(g_vs.BORDER_SIZE[0], g_vs.WIDTH - g_vs.BORDER_SIZE[0])),
                    int(random.randint(g_vs.BORDER_SIZE[1], g_vs.HEIGHT - g_vs.BORDER_SIZE[1]))]
        self.speed = [int(random.choice([-1, 1]) * g_vs.SPEED), int(random.choice([-1, 1]) * g_vs.SPEED)]
        self.speed_counter = 0

    # Implement this!
    def move(self):
        pass

    # Implement this!
    def turn_left(self):
        pass

    # Implement this!
    def turn_right(self):
        pass

    # Implement this!
    def shoot(self):
        pass
