#Frogger; OG-game; Main page for the game with the little frog, trying to cross the road.

import turtle

#Set up the screen
wn = turtle.Screen()
wn.title("Frogger")
wn.setup = (600, 800)
wn.bgcolor("black")

#Shapes
wn.register_shape("graphics/sprite_individuals/frog_frontv1.gif")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

#Classes
class Sprite(): #sprite = character
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.image)
        pen.stamp()

class Player(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)


#Objects
player = Player(0, -300, 40, 40, "graphics/sprite_individuals/frog_frontv1.gif)")
player.render(pen)


wn.mainloop()