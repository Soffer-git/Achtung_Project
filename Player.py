import g_vs
import pygame
import copy
import random
import itertools


def parse_player_line(line):
    arguments = line.strip().split(', ')
    return g_vs.COLOR_DICT[arguments[0]], g_vs.KEYS_DICT[arguments[1]], \
           g_vs.KEYS_DICT[arguments[2]], g_vs.KEYS_DICT[arguments[3]]


def detect_collisions(center):
    if not g_vs.CIRCLE_MAT:
        g_vs.CIRCLE_MAT = [[x ** 2 + y ** 2 <= g_vs.THICKNESS ** 2 for y in g_vs.THICKNESS_RANGE]
                           for x in g_vs.THICKNESS_RANGE]
    return any([g_vs.CIRCLE_MAT[x + g_vs.THICKNESS][y + g_vs.THICKNESS]
                and 0 <= x + center[0] < g_vs.WIDTH
                and 0 <= y + center[1] < g_vs.HEIGHT
                and g_vs.SCREEN.get_at((x + center[0], y + center[1])) != g_vs.COLOR_DICT["Black"]
                for x, y in itertools.product(g_vs.THICKNESS_RANGE, g_vs.THICKNESS_RANGE)])


class Player:
    def __init__(self, line):
        assert g_vs.WIDTH != -1 and g_vs.HEIGHT != -1  # Makes sure the screen is initialized beforehand.
        self.color, self.l_key, self.r_key, self.j_key = parse_player_line(line)
        # Add distance between starting points!
        self.pos = [int(random.randint(g_vs.BORDER_SIZE[0], g_vs.WIDTH - g_vs.BORDER_SIZE[0])),
                    int(random.randint(g_vs.BORDER_SIZE[1], g_vs.HEIGHT - g_vs.BORDER_SIZE[1]))]
        starting_x_sign = random.choice([-1, 1])
        starting_y_sign = random.choice([-1, 1])
        starting_x_velocity = random.randint(0, g_vs.SPEED)
        starting_y_velocity = g_vs.SPEED - starting_x_velocity

        self.speed = [starting_x_sign * starting_x_velocity, starting_y_sign * starting_y_velocity]
        self.turn_count = 0
        self.turn_direction = "Stop"
        self.l_pressed = False
        self.r_pressed = False
        self.lives = 1

    def turn_left(self):
        new_speed = copy.copy(self.speed)
        if self.speed[0] > 0:
            new_speed[1] -= 1
        elif self.speed[0] < 0:
            new_speed[1] += 1
        elif self.speed[1] > 0:
            new_speed[1] -= 1
        else:
            new_speed[1] += 1

        if self.speed[1] > 0:
            new_speed[0] += 1
        elif self.speed[1] < 0:
            new_speed[0] -= 1
        elif self.speed[0] > 0:
            new_speed[0] -= 1
        else:
            new_speed[0] += 1

        self.speed = new_speed

    def turn_right(self):
        new_speed = copy.copy(self.speed)
        if self.speed[0] > 0:
            new_speed[1] += 1
        elif self.speed[0] < 0:
            new_speed[1] -= 1
        elif self.speed[1] > 0:
            new_speed[1] -= 1
        else:
            new_speed[1] += 1

        if self.speed[1] > 0:
            new_speed[0] -= 1
        elif self.speed[1] < 0:
            new_speed[0] += 1
        elif self.speed[0] > 0:
            new_speed[0] -= 1
        else:
            new_speed[0] += 1

        self.speed = new_speed

    def manage_movement(self):
        if self.lives == 0 or self.turn_direction == "Stop":
            return
        if self.turn_direction == self.l_key:
            if self.turn_count == g_vs.ITERS_FOR_TURN:
                self.turn_left()
                self.turn_count = 0
            else:
                self.turn_count += 1
        elif self.turn_direction == self.r_key:
            if self.turn_count == g_vs.ITERS_FOR_TURN:
                self.turn_right()
                self.turn_count = 0
            else:
                self.turn_count += 1
        new_pos = (self.pos[0] + self.speed[0], self.pos[1] + self.speed[1])
        pygame.draw.circle(g_vs.SCREEN, g_vs.COLOR_DICT["Black"], self.pos, g_vs.THICKNESS, width=0)
        if new_pos[0] < g_vs.THICKNESS or new_pos[0] > g_vs.WIDTH - g_vs.THICKNESS \
                or new_pos[1] < g_vs.THICKNESS or new_pos[1] > g_vs.HEIGHT - g_vs.THICKNESS \
                or detect_collisions(new_pos):
            self.lives = 0
        pygame.draw.circle(g_vs.SCREEN, self.color, self.pos, g_vs.THICKNESS, width=0)
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]

    # Implement this!
    def shoot(self):
        pass
