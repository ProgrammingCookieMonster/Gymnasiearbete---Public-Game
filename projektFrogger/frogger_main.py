#Frogger; OG-game; Main page for the game with the little frog, trying to cross the road.

import turtle
import math

#Set up the screen
wn = turtle.Screen()
wn.cv._rootwindow.resizable(False, False)
wn.title("Frogger by Andrei")
wn.setup = (600, 800)
wn.bgcolor("black")
wn.tracer(0)

#Shapes registration
wn.register_shape("graphics/sprite_individuals/frog_frontv1.gif")
wn.register_shape("graphics/cars/car1_left.gif")
wn.register_shape("graphics/cars/car1_right.gif")
wn.register_shape("graphics/logs/log_full.gif")

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

    def is_collision(self, other):
        x_collosion = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collosion and y_collision)

class Player(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = 0
    def up(self):
        self.y += 50
    def down(self):
        self.y -= 50
    def right(self):
        self.x += 50
    def left(self):
        self.x -= 50

    def update(self):
        self.x += self.dx

        #Border checking frog --> frog off the screen = player loose 1 life
        if self.x < -360 or self.x > 360:
            self.x = 0
            self.y = -300

#Class for Car --> Player objective: Avoid the Car
class Car(Sprite):
    def __init__(self, x, y, width, height, image, dx): #Dx stands for Delta x, changing the direction
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx
    def update(self):
        self.x += self.dx

        #Space Checking - borders
        if self.x < -400:
            self.x = 400
        if self.x > 400:
            self.x = -400

class Log(Sprite):
    def __init__(self, x, y, width, height, image, dx): #Dx stands for Delta x, changing the direction
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx
    def update(self):
        self.x += self.dx

        #Space Checking - borders
        if self.x < -500:
            self.x = 500
        if self.x > 500:
            self.x = -500


#Objects
player = Player(0, -300, 40, 40, "graphics/sprite_individuals/frog_frontv1.gif")

car_left = Car(300, -255, 121, 40, "graphics/cars/car1_left.gif", -2.5)
car_right = Car(-300, -200, 121, 40, "graphics/cars/car1_right.gif", +2.5)
log_left = Log(-300, -150, 100, 40, "graphics/logs/log_full.gif", -1.5)
log_right = Log(-300, -100, 100, 40, "graphics/logs/log_full.gif", +1.5)

#List of Objects
sprites = [car_left, car_right, log_left, log_right, player] # Creating a list to minimize the further code

# Keyboard binding --> controlls
wn.listen()
wn.onkeypress(player.up, "Up")
wn.onkeypress(player.down, "Down")
wn.onkeypress(player.right, "Right")
wn.onkeypress(player.left, "Left")

while True:
    #Render, Update, Collisions
    for sprite in sprites:
        sprite.render(pen) #Render objects
        sprite.update() #Update objects

    player.dx = 0
    for sprite in sprites:
        if player.is_collision(sprite):
            if isinstance(sprite, Car): #Collisions with cars
                player.x = 0
                player.y = -300
                break
            elif isinstance(sprite, Log):
                player.dx = sprite.dx
                break

    #Logs
    if player.is_collision(log_left):
        player.dx = log_left.dx
    else:
        player.dx = 0

    if player.is_collision(log_right):
        player.dx = log_right.dx
    

    #Update Screen
    wn.update()

    #Clearing Pen
    pen.clear()

wn.mainloop()