from tkinter import *
from wanderer.maze import Maze
from wanderer.hero import Hero


# Create the tk environment as usual
root = Tk()
canvas = Canvas(root, width=720, height=720)

"""
img = PhotoImage(file="images/floor.gif")
canvas.create_image(40, 40, image=img)
"""

maze = Maze(canvas)
hero = Hero(canvas)

def on_key_press(e):

    current_pos = hero.get_hero_position()

    if e.keycode == 87:
        #up
        hero.draw_hero(current_pos[0], current_pos[1]-1)
        print("up [" + str(current_pos[0]) + "  " + str(current_pos[1]) + " ]")
    elif e.keycode == 83:
        #down
        hero.draw_hero(current_pos[0], current_pos[1]+1)
        print("down [" + str(current_pos[0]) + "  " + str(current_pos[1]) + " ]")
    elif e.keycode == 68:
        #right
        hero.draw_hero(current_pos[0]+1, current_pos[1])
        print("right [" + str(current_pos[0]) + "  " + str(current_pos[1]) + " ]")
    elif e.keycode == 65:
        #left
        hero.draw_hero(current_pos[0]-1, current_pos[1])
        print("left [" + str(current_pos[0]) + "  " + str(current_pos[1]) + " ]")

"""

# Creating a box that can draw itself in a certain position
box = Box()

# Create a function that can be called when a key pressing happens
def on_key_press(e):
    # When the keycode is 111 (up arrow) we move the position of our box higher
    if e.keycode == 111:
        box.testBoxY = box.testBoxY - 100
    elif e.keycode == 116:
        box.testBoxY = box.testBoxY + 100
    # and lower if the key that was pressed the down arrow
    # draw the box again in the new position
    box.draw(canvas)

"""

# Tell the canvas that we prepared a function that can deal with the key press events
canvas.bind("<KeyPress>", on_key_press)
canvas.pack()

# Select the canvas to be in focused so it actually recieves the key hittings
canvas.focus_set()

# Draw the box in the initial position
#box.draw(canvas)


root.mainloop()