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
shapes = [
        "graphics/sprite_individuals/frog_frontv1.gif", "graphics/cars/car1_left.gif",
        "graphics/cars/car1_right.gif", "graphics/logs/log_full.gif", "graphics/others/turtles_left.gif",
        "graphics/others/turtles_right.gif", "graphics/others/turtles_right_half.gif",
        "graphics/others/turtles_left_half.gif", "graphics/others/turtles_left_submerged.gif",
        "graphics/others/turtles_right_submerged.gif", "graphics/cars/racing_car1_left.gif",
        "graphics/cars/racing_car2_left.gif", "graphics/cars/police_car_left.gif",
        "graphics/cars/truck_right.gif", "graphics/cars/truck_left.gif", "graphics/others/croc_killer.gif"
        ]
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
        if self.x < -550:
            self.x = 550
        if self.x > 550:
            self.x = -550

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

class Crocodile(Sprite):
    def __init__(self, x, y, width, height, image, dx): #Dx stands for Delta x, changing the direction
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx
    def update(self):
        self.x += self.dx



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


#Objects --> Objects won't be in row others as there is a certain variation of positions; creating game pattern
player = Player(0, -300, 40, 40, "graphics/sprite_individuals/frog_frontv1.gif")
# CARS
car_left = Car(300, -250, 121, 40, "graphics/cars/car1_left.gif", -2.5) # Row 1
car_right = Car(-300, -100, 121, 40, "graphics/cars/car1_right.gif", +2.5) # Row 4
racing_car1 = Car(-300, -150, 121, 40, "graphics/cars/racing_car1_left.gif", -4.0) # Row 3
racing_car2 = Car(-450, -150, 121, 40, "graphics/cars/racing_car2_left.gif", -4.0) # Row 3 --> Racing cars and police car are racing
racing_car3 = Car(-540, -150, 121, 40, "graphics/cars/police_car_left.gif", -3.0) # Row 3
truck_left = Car(300, -50, 200, 40, "graphics/cars/truck_left.gif", -2.5) # Row 5
truck_right = Car(300, -200, 200, 40, "graphics/cars/truck_right.gif", +2.5) # Row 2
# LOGS
log_left = Log(-300, 50, 100, 40, "graphics/logs/log_full.gif", -2.5) # Row 6
log_right = Log(-300, 150, 100, 40, "graphics/logs/log_full.gif", +2.5) #
# TURTLES
turtle_left = Turtle(-300, 100, 200, 32, "graphics/others/turtles_left.gif", -1.0) # Row 7
turtle_right = Turtle(-300, 200, 250, 32, "graphics/others/turtles_right.gif", +1.0)
killer = Crocodile(400, 100, 100, 40, "graphics/others/croc_killer.gif", -1.0)

#List of Objects
sprites = [
        car_left, car_right, log_left, log_right,
        turtle_right, turtle_left, racing_car1, racing_car2, racing_car3, truck_right, truck_left, killer, player
        ] # Creating a list to minimize the further code

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
            elif isinstance(sprite, Crocodile):
                player.x = 0
                player.y = -300
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
