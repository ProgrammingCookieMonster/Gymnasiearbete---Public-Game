#Frogger; OG-game; Main page for the game with the little frog, trying to cross the road.

import turtle

#Set up the screen
wn = turtle.Screen()
wn.title("Frogger")
wn.setup = (600, 800)
wn.bgcolor("black")
wn.tracer(0)

#Shapes registration
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
    def up(self):
        self.y += 45
    def down(self):
        self.y -= 45
    def right(self):
        self.x += 45
    def left(self):
        self.x -= 45

#Class for Car --> Player objective: Avoid the Car
class Car(Sprite):
    def __init__(self, x, y, width, height, image, dx): #Dx stands for Delta x, changing the direction
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx


#Objects
player = Player(0, -300, 40, 40, "graphics/sprite_individuals/frog_frontv1.gif")
player.render(pen)

# Keyboard binding --> controlls
wn.listen()
wn.onkeypress(player.up, "Up")
wn.onkeypress(player.down, "Down")
wn.onkeypress(player.right, "Right")
wn.onkeypress(player.left, "Left")

while True:
    #Render
    player.render(pen)
    #Update Screen
    wn.update()
    #Clearing Pen
    pen.clear()

wn.mainloop()