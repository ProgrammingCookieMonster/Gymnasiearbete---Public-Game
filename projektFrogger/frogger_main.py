#Frogger; OG-game; Main page for the game with the little frog, trying to cross the road.

import turtle

#Set up the screen
wn = turtle.Screen()
wn.title("Frogger")
wn.setup = (600, 800)
wn.bgcolor("black")

#Classes
class Sprite(): #sprite = character
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

class Player(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)

#Objects
player = Player(0, -300, 40, 40, "frog_front.gif")


wn.mainloop()