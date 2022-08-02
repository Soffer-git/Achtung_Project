import g_vs
import copy
import random


def parse_player_line(line):
    arguments = line.strip().split(', ')
    return g_vs.COLOR_DICT[arguments[0]], g_vs.KEYS_DICT[arguments[1]], \
        g_vs.KEYS_DICT[arguments[2]], g_vs.KEYS_DICT[arguments[3]]


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
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
        if self.pos[0] < g_vs.THICKNESS or self.pos[0] > g_vs.WIDTH - g_vs.THICKNESS \
                or self.pos[1] < g_vs.THICKNESS or self.pos[1] > g_vs.HEIGHT - g_vs.THICKNESS:
            self.lives = 0

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

    # Implement this!
    def shoot(self):
        pass
