# Frogger; OG-game; Main page for the game with the little frog, trying to cross the road.
import time
import turtle
import math
import random
import pygame

#Set up the screen
wn = turtle.Screen()
wn.title("Frogger by Andrei")
wn.setup(600, 800) # width x height
wn.cv._rootwindow.resizable(False, False)
wn.bgcolor("green")
wn.bgpic("graphics/others/frogger_background.gif")
wn.tracer(0)

#Set up game time (FPS)
pygame.init()
clock = pygame.time.Clock()
FPS = 60
# dt = clock.tick(FPS) / 100.0 #delta time
dt = 1
# Start level value
game_level = 1
# Score; higher on higher value; start values
score_variable = 1
speed = 1
score = 0

#Shapes registration
shapes = [
        "graphics/sprite_individuals/frog_frontv1.gif", "graphics/cars/car1_left.gif",
        "graphics/cars/car1_right.gif", "graphics/logs/log_full.gif", "graphics/others/turtles_left.gif",
        "graphics/others/turtles_right.gif", "graphics/others/turtles_right_half.gif",
        "graphics/others/turtles_left_half.gif", "graphics/others/turtles_left_submerged.gif",
        "graphics/others/turtles_right_submerged.gif", "graphics/cars/racing_car1_left.gif",
        "graphics/cars/racing_car2_left.gif", "graphics/cars/police_car_left.gif", "graphics/cars/racing_car1_right.gif",
        "graphics/cars/truck_right.gif", "graphics/cars/truck_left.gif", "graphics/others/croc_killer.gif",
        "graphics/others/goal.gif", "graphics/others/frog_is_home.gif", "graphics/others/heart_full.gif", "graphics/others/heart_empty.gif"
        ]
for shape in shapes:
    wn.register_shape(shape)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()

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

    def update(self):
        pass

    def is_collision(self, other):
        x_collosion = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collosion and y_collision)

class Player(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = 0
        self.collision = False
        self.frogs_home = 0
        self.max_time = 60
        self.time_remaining = 60
        self.start_time = time.time()
        self.lives = 3
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
            self.go_home()
            self.lives -= 1
        elif self.y <  -400:
            self.go_home()
            self.lives -= 1

        self.time_remaining = self.max_time - round(time.time() - self.start_time)

        #Time's up
        if self.time_remaining <= 0:
            player.lives -= 1
            self.go_home()

    def go_home(self):
        self.dx = 0
        self.y = -350
        self.x = 0
        self.max_time = 60
        self.time_remaining = 60
        self.start_time = time.time()

#Class for Car --> Player objective: Avoid the Car
class Car(Sprite):
    def __init__(self, x, y, width, height, image, dx): #Dx stands for Delta x, changing the direction
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx * dt
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
        self.dx = dx * dt
    def update(self):
        self.x += self.dx

        #Space Checking - borders
        if self.x < -550:
            self.x = 550
        if self.x > 550:
            self.x = -550

class Turtle(Sprite):
    def __init__(self, x, y, width, height, image, dx): #Dx stands for Delta x, changing the direction
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx * dt
        self.state = "full" # half, submerged --> full and half can hold the player but a submerged turtle won't --> player gets reseted and looses a life
        self.full_time = random.randint(8, 12)
        self.half_time = random.randint(6, 8)
        self.submerged_time = random.randint(3, 6)
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

class Home(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = 0

class Timer():
    def __init__(self, max_time):
        self.x = 285
        self.y = 340
        self.max_time = max_time
        self.width = 200
        self.text_x = 150

    def render(self, time, pen):
        pen.color("red")
        pen.pensize(10)
        pen.penup()
        pen.goto(self.x, self.y)
        pen.pendown()
        percent = time/self.max_time
        dx = percent * self.width
        pen.goto(self.x - dx, self.y)
        pen.penup()

        timer_position = ( self.text_x, self.y + 5)
        pen.goto(timer_position)
        pen.write(f"Time: {time}", align="left", font=("Times", 24, "bold"))
        pen.penup()

class game_score():
    def __init__(self, score):
        self.x = 0
        self.y = 0
        self.score = score

    def render(self, pen):
        pen.color("green")
        pen.pensize(10)
        pen.pendown()
        pen.goto(self.x, self.y)
        pen.write(f"Score: {score}", align="right", front=("Times", 24, "bold"))
        pen.penup()

#Objects --> Objects won't be in row others as there is a certain variation of positions; creating game pattern
player = Player(0, -350, 40, 40, "graphics/sprite_individuals/frog_frontv1.gif")
timer = Timer(60)
# Objects
level_1 = [
    Car(300, -300, 121, 40, "graphics/cars/car1_left.gif", -3.0),
    Car(100, -300, 121, 40, "graphics/cars/car1_left.gif", -3.0),
    Car(-300, -150, 121, 40, "graphics/cars/car1_right.gif", +2.5),
    Car(50, -150, 200, 40, "graphics/cars/racing_car1_right.gif", +2.5),
    Car(-300, -200, 121, 40, "graphics/cars/racing_car1_left.gif", -4.0),
    Car(-450, -200, 121, 40, "graphics/cars/racing_car2_left.gif", -4.0),
    Car(-540, -200, 121, 40, "graphics/cars/police_car_left.gif", -3.0),
    Car(300, -100, 200, 40, "graphics/cars/truck_left.gif", -2.5),
    Car(500, -100, 121, 40, "graphics/cars/racing_car2_left.gif", -2.5),
    Car(300, -250, 200, 40, "graphics/cars/truck_right.gif", +2.5),
    Log(-300, 50, 100, 40, "graphics/logs/log_full.gif", +2.45),
    Log(-300, 150, 100, 40, "graphics/logs/log_full.gif", +1.75),
    Log(-300, 250, 100, 40, "graphics/logs/log_full.gif", +3.0),
    Turtle(-300, 100, 200, 32, "graphics/others/turtles_left.gif", -1.8),
    Log(100, 100, 100, 40, "graphics/logs/log_full.gif", -1.8),
    Turtle(-300, 200, 250, 32, "graphics/others/turtles_right.gif", -1.2),
    Turtle(200, 200, 250, 32, "graphics/others/turtles_right.gif", -1.2),
    Car(400, 0, 100, 40, "graphics/others/croc_killer.gif", +1.9) #Crocodile, might delete
]

homes = [
    Home(0, 300, 50, 50, "graphics/others/goal.gif"),
    Home(-100, 300, 50, 50, "graphics/others/goal.gif"),
    Home(-200, 300, 50, 50, "graphics/others/goal.gif"),
    Home(100, 300, 50, 50, "graphics/others/goal.gif"),
    Home(200, 300, 50, 50, "graphics/others/goal.gif")
]


#List of Objects
sprites = level_1 + homes
sprites.append(player)

# Keyboard binding --> controlls
wn.listen()
wn.onkeypress(player.up, "Up")
wn.onkeypress(player.down, "Down")
wn.onkeypress(player.right, "Right")
wn.onkeypress(player.left, "Left")

while True:
    # Render, Update, Collisions
    for sprite in sprites:
        sprite.render(pen) #Render objects
        sprite.update() #Update objects
    # Render timer
    timer.render(player.time_remaining, pen)

    # Render lives
    pen.shape("graphics/others/heart_full.gif")
    for life in range(player.lives):
        pen.goto(-260 + (life * 65), 350)
        pen.stamp()

    # Render score
    game_score.render(score, pen)

    player.dx = 0 # Checking for collisions
    player.collision = False
    for sprite in sprites:
        if player.is_collision(sprite):
            if isinstance(sprite, Car): #Collisions with cars --> Frog dies
                player.go_home()
                player.lives -= 1
                break
            elif isinstance(sprite, Log): #Collisions with log --> Frog floats
                player.dx = sprite.dx
                player.collision = True
                break
            elif isinstance(sprite, Turtle) and sprite.state != "submerged": #Collision with turtles --> Frog floats only on full and half state
                player.dx = sprite.dx
                player.collision = True
                # No Break - so collision with crocodile works - test
            elif isinstance(sprite, Home):
                player.go_home()
                sprite.image = "graphics/others/frog_is_home.gif"
                player.frogs_home += 1
                break
        # Check the player is/isn't touching the water (y > 0 - above the safe line)
    if player.y > 0 and player.collision != True: # ADD SOUND OF WHATER SPLASH WHEN PLAYER FALLS IN THE RIVER !!!
        player.go_home()
        player.lives -= 1

    # Made it home 5 times (wins 1 level):
    if player.frogs_home == 5:
        player.go_home()
        game_level += 1
        score_variable = score_variable * (game_level/2)
        player.frogs_home = 0
        for home in homes:
            home.image = "graphics/others/goal.gif"
    # Calculating score
    for action in range(1, 5):
        if action == player.frogs_home:
            score = score + (50 * score_variable) # giving off points for every frog in the house
        elif action == player.frogs_home:
            score = score + (50 * (2 * score_variable)) # giving even more extra points for completing levels
    # Player runs out of lives
    if player.lives == 0:
        player.go_home()
        game_level = 1
        score_variable = 1
        speed = 1
        player.frogs_home = 0
        for home in homes:
            home.image = "graphics/others/goal.gif"
        player.lives = 3


    #Update Screen
    wn.update()

    #Clearing Pen
    pen.clear()