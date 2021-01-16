from tkinter import *

class Maze():

    def __init__(self, canvas):
        self.canvas = canvas
        self.image = PhotoImage(file="images/wall.gif")
        #self.layout = []

        #self.init_layout()
        self.draw_maze()


    def draw_maze(self):
        #self.canvas.create_rectangle(2,2,20,20, fill = 'red')
        img = PhotoImage(file="images/wall.gif")
        self.canvas.create_image(0, 0, image=self.image)


        """
        for i in range(len(self.layout)):
            for j in range(len(self.layout[0])):
                if self.layout[i][j] == 1:
                    self.canvas.create_image(i*40,j*40, image=img)
        """

    def init_layout(self):
        for i in range(10):
            temp = []
            for j in range(10):
                temp.append(1)
            self.layout.append(temp)