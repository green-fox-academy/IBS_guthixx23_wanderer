from tkinter import *
from wanderer.character import Character


class Hero(Character):

    def __init__(self, canvas, controller):
        Character.__init__(self)
        self.hp = 20 + 3 * self.roll_d6()
        self.dp = 2 * self.roll_d6()
        self.sp = 5 + self.roll_d6()
        self.current_hp = self.hp

        self.controller = controller
        self.canvas = canvas

        self.image_down = PhotoImage(file="images/hero-down.gif")
        self.image_right = PhotoImage(file="images/hero-right.gif")
        self.image_left = PhotoImage(file="images/hero-left.gif")
        self.image_up = PhotoImage(file="images/hero-up.gif")
        self.position_x = 1
        self.position_y = 1
        self.draw_hero(self.position_x, self.position_y)

    def draw_hero(self, x_pos, y_pos):

        if x_pos == self.position_x and y_pos == self.position_y:
            self.canvas.create_image((self.position_x - 1) * 72 + 36, (self.position_y - 1) * 72 + 36,
                                     image=self.image_down)

        if x_pos == self.position_x + 1:
            if self.controller.maze.layout[self.position_y][self.position_x + 1] != 1:
                self.canvas.create_image(self.position_x * 72 + 36, (self.position_y - 1) * 72 + 36,
                                         image=self.image_right)
                self.position_x = x_pos
            else:
                self.canvas.create_image((self.position_x - 1) * 72 + 36, (self.position_y - 1) * 72 + 36,
                                         image=self.image_right)

        if x_pos == self.position_x - 1:
            if self.controller.maze.layout[self.position_y][self.position_x - 1] != 1:
                self.canvas.create_image((self.position_x - 2) * 72 + 36, (self.position_y - 1) * 72 + 36,
                                         image=self.image_left)
                self.position_x = x_pos
            else:
                self.canvas.create_image((self.position_x - 1) * 72 + 36, (self.position_y - 1) * 72 + 36,
                                         image=self.image_left)

        if y_pos == self.position_y + 1:
            if self.controller.maze.layout[self.position_y + 1][self.position_x] != 1:
                self.canvas.create_image((self.position_x - 1) * 72 + 36, self.position_y * 72 + 36,
                                         image=self.image_down)
                self.position_y = y_pos
            else:
                self.canvas.create_image((self.position_x - 1) * 72 + 36, (self.position_y - 1) * 72 + 36,
                                         image=self.image_down)

        if y_pos == self.position_y - 1:
            if self.controller.maze.layout[self.position_y - 1][self.position_x] != 1:
                self.canvas.create_image((self.position_x - 1) * 72 + 36, (self.position_y - 2) * 72 + 36,
                                         image=self.image_up)
                self.position_y = y_pos
            else:
                self.canvas.create_image((self.position_x - 1) * 72 + 36, (self.position_y - 1) * 72 + 36,
                                         image=self.image_up)

    def get_hero_position(self):
        return [self.position_y, self.position_x]
