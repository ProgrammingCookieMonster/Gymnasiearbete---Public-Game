# Frogger; OG-game; Main page for the game with the little frog, trying to cross the road.
import time
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
shapes = ["graphics/sprite_individuals/frog_frontv1.gif", "graphics/cars/car1_left.gif", "graphics/cars/car1_right.gif", "graphics/logs/log_full.gif", "graphics/others/turtles_left.gif", "graphics/others/turtles_right.gif", "graphics/others/turtles_right_half.gif", "graphics/others/turtles_left_half.gif", "graphics/others/turtles_left_submerged.gif", "graphics/others/turtles_right_submerged.gif"]
for shape in shapes:
    wn.register_shape(shape)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

#Classes
class Sprite(): # sprite = character
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

class Turtle(Sprite):
    def __init__(self, x, y, width, height, image, dx): #Dx stands for Delta x, changing the direction
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx
        self.state = "full" # half, submerged --> full and half can hold the player but a submerged turtle won't --> player gets reseted and looses a life
        self.full_time = 10
        self.half_time = 5
        self.submerged_time = 5
        self.start_time = time.time()
    def update(self):
        self.x += self.dx

        #Space Checking - borders
        if self.x < -500:
            self.x = 500
        if self.x > 500:
            self.x = -500

        #Update image based on state:
        if self.state == "full":
            if self.dx > 0:
                self.image = "graphics/others/turtles_right.gif"
            else:
                self.image = "graphics/others/turtles_left.gif"
        elif self.state == "half":
            if self.dx > 0:
                self.image = "graphics/others/turtles_right_half.gif"
            else:
                self.image = "graphics/others/turtles_left_half.gif"
        elif self.state == "submerged":
            if self.dx > 0:
                self.image = "graphics/others/turtles_right_submerged.gif"
            else:
                self.image = "graphics/others/turtles_left_submerged.gif"

        #Game Timer - turtle state
        if self.state == "full" and time.time() - self.start_time > self.full_time:
            self.state = "half"
            self.start_time = time.time()
        elif self.state == "half" and time.time() - self.start_time > self.half_time:
            self.state = "submerged"
            self.start_time = time.time()
        elif self.state == "submerged" and time.time() - self.start_time > self.submerged_time:
            self.state = "full"
            self.start_time = time.time()


#Objects
player = Player(0, -300, 40, 40, "graphics/sprite_individuals/frog_frontv1.gif")

car_left = Car(300, -255, 121, 40, "graphics/cars/car1_left.gif", -2.5)
car_right = Car(-300, -200, 121, 40, "graphics/cars/car1_right.gif", +2.5)
log_left = Log(-300, -150, 100, 40, "graphics/logs/log_full.gif", -1.5)
log_right = Log(-300, -100, 100, 40, "graphics/logs/log_full.gif", +1.5)
turtle_left = Turtle(-300, -50, 100, 32, "graphics/others/turtles_left.gif", -1.0)
turtle_right = Turtle(-300, 0, 100, 32, "graphics/others/turtles_right.gif", +1.0)

#List of Objects
sprites = [car_left, car_right, log_left, log_right, turtle_right, turtle_left, player] # Creating a list to minimize the further code

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
            if isinstance(sprite, Car): #Collisions with cars --> Frog dies
                player.x = 0
                player.y = -300
                break
            elif isinstance(sprite, Log): #Collisions with log --> Frog floats
                player.dx = sprite.dx
                break
            elif isinstance(sprite, Turtle) and sprite.state != "submerged": #Collision with turtles --> Frog floats only on full and half state
                player.dx = sprite.dx
                break


    #Update Screen
    wn.update()

    #Clearing Pen
    pen.clear()
