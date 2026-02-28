import turtle
import random

# Sky functions - sun, clouds, and rainbow.
def draw_sun_with_rays(t, x, y):
    t.up()
    t.goto(x, y - 40)
    t.color("orange", "yellow")
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    t.pensize(3)
    t.color("orange")
    for i in range(12):
        t.up()
        t.goto(x, y)
        t.setheading(i * 30)
        t.forward(45)
        t.down()
        t.forward(20)

def draw_cloud(t, x, y):
    t.color("white", "white")
    for _ in range(6):
        t.up()
        t.goto(x + random.randint(-30, 30), y + random.randint(-20, 20))
        t.begin_fill()
        t.circle(20)
        t.end_fill()

def draw_rainbow(t):
    rainbow_colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
    t.pensize(10)
    current_radius = 120
    for col in rainbow_colors:
        t.up()
        t.color(col)
        t.goto(150 - current_radius, 50)
        t.setheading(90)
        t.down()
        t.circle(-current_radius, 180)
        current_radius = current_radius + 10

# Landscape functions - mountains and meadow.
def draw_mountain(t, x, y, w, h):
    t.up()
    t.goto(x, y)
    t.setheading(0)
    t.down()
    t.color("dimgray", "gray")
    t.begin_fill()
    t.goto(x + w / 2, y + h)
    t.goto(x + w, y)
    t.goto(x, y)
    t.end_fill()
    t.up()
    t.goto(x + w * 0.35, y + h * 0.7)
    t.down()
    t.color("white")
    t.begin_fill()
    t.goto(x + w / 2, y + h)
    t.goto(x + w * 0.65, y + h * 0.7)
    t.goto(x + w * 0.35, y + h * 0.7)
    t.end_fill()

def draw_meadow_ground(t):
    t.up()
    t.goto(-1000, 50)
    t.color("forest green", "lime green")
    t.begin_fill()
    for _ in range(2):
        t.forward(2000)
        t.right(90)
        t.forward(600)
        t.right(90)
    t.end_fill()

def draw_grass_texture(t, count):
    t.pensize(1)
    for _ in range(count):
        t.color(random.choice(["dark green", "forest green"]))
        x = random.randint(-1000, 1000)
        y = random.randint(-550, 50)
        t.up()
        t.goto(x, y)
        t.down()
        t.setheading(60)
        t.forward(4)
        t.backward(4)
        t.setheading(120)
        t.forward(4)
    t.up() 

# Ice rink functions
def draw_ice_rink(t):
    t.up()
    t.setheading(0)
    t.goto(-300, -70)
    t.color("light blue", "aliceblue")
    t.begin_fill()
    for _ in range(2):
        t.forward(600)
        t.circle(-50, 90)
        t.forward(120)
        t.circle(-50, 90)
    t.end_fill()
    t.pensize(5)
    t.up()
    t.goto(0, -70)
    t.setheading(270)
    t.color("red")
    t.down()
    t.forward(220)
    for lx in [-120, 120]:
        t.color("blue")
        t.up()
        t.goto(lx, -70)
        t.down()
        t.forward(220)
    t.up()
    t.goto(40, -180)
    t.setheading(90)
    t.color("red")
    t.pensize(3)
    t.down()
    t.circle(40)

def draw_left_goal(t, x, y):
    side_factor = 1
    t.pensize(4)
    t.color("red")
    t.up()
    t.goto(x, y)
    t.setheading(90)
    t.down()
    t.forward(50)
    t.setheading(0)
    t.forward(8 * side_factor)
    t.setheading(270)
    t.forward(50)
    t.color("darkgray")
    t.pensize(2)
    t.up()
    t.goto(x, y + 50)
    t.down()
    t.goto(x - 35 * side_factor, y + 35)
    t.goto(x - 35 * side_factor, y)
    t.goto(x, y)

def draw_right_goal(t, x, y):
    side_factor = -1
    t.pensize(4)
    t.color("red")
    t.up()
    t.goto(x, y)
    t.setheading(90)
    t.down()
    t.forward(50)
    t.setheading(0)
    t.forward(8 * side_factor)
    t.setheading(270)
    t.forward(50)
    t.color("darkgray")
    t.pensize(2)
    t.up()
    t.goto(x, y + 50)
    t.down()
    t.goto(x - 35 * side_factor, y + 35)
    t.goto(x - 35 * side_factor, y)
    t.goto(x, y)

def draw_puck(t, x, y):
    t.up()
    t.goto(x, y)
    t.color("black")
    t.begin_fill()
    t.circle(5)
    t.end_fill()

# Cow functions - draws different cows and their accesories.
def draw_flag(t, x, y, scale):
    t.color("sienna")
    t.pensize(2 * scale)
    t.setheading(90)
    t.up()
    t.goto(x, y)
    t.down()
    t.forward(20 * scale)
    colors = ["maroon", "gold", "darkgreen", "royalblue"]
    t.color(random.choice(colors))
    t.setheading(0)
    t.up()
    t.goto(x, y + (20 * scale))
    t.down()
    t.begin_fill()
    t.forward(15 * scale)
    t.right(150)
    t.forward(17.3 * scale)
    t.goto(x, y + (20 * scale))
    t.end_fill()
    t.up()
    t.goto(x + (5 * scale), y + (12 * scale))
    t.color("white")
    t.write("C", align="center", font=("Arial", int(6 * scale), "bold"))

def draw_big_cow(t, x, y, facing_left_or_right):
    draw_full_cow(t, x, y, facing_left_or_right, 1.0, True, False)

def draw_small_cow(t, x, y, scale):
    draw_full_cow(t, x, y, random.choice([-1, 1]), scale, False, True)

def draw_cow_limbs(t, x, y, facing_left_or_right, scale, is_player, holds_pennant):
    t.pensize(3 * scale)
    t.color("black")
    t.up()
    t.goto(x - (18 * scale), y - (5 * scale))
    t.down()
    t.goto(x - (18 + 10 * facing_left_or_right) * scale, y - (25 * scale))
    t.color("gray")
    t.setheading(0)
    t.forward(12 * facing_left_or_right * scale)
    t.color("black")
    t.up()
    t.goto(x - (6 * scale), y - (5 * scale))
    t.down()
    t.goto(x - (6 - 10 * facing_left_or_right) * scale, y - (25 * scale))
    t.color("gray")
    t.setheading(0)
    t.forward(12 * facing_left_or_right * scale)
    if is_player:
        t.color("black")
        t.up()
        t.goto(x - (22 * scale), y + (20 * scale))
        t.down()
        t.goto(x - (22 + 13 * facing_left_or_right) * scale, y + (5 * scale))
        t.up()
        t.goto(x - (2 * scale), y + (20 * scale))
        t.down()
        t.color("sienna")
        t.pensize(4 * scale)
        t.goto(x + (20 * facing_left_or_right * scale), y - (15 * scale))
        t.setheading(0)
        t.forward(15 * facing_left_or_right * scale)
    else:
        t.color("black")
        t.up()
        t.goto(x - (22 * scale), y + (18 * scale))
        t.down()
        if holds_pennant:
            p_x = x - (35 * scale)
            p_y = y + (35 * scale)
            t.goto(p_x, p_y)
            draw_flag(t, p_x, p_y, scale)
        else:
            t.goto(x - (28 * scale), y + (8 * scale))
        t.up()
        t.goto(x - (2 * scale), y + (18 * scale))
        t.down()
        t.goto(x + (4 * scale), y + (8 * scale))

def draw_full_cow(t, x, y, facing_left_or_right=1, scale=1, is_player=True, holds_pennant=False):
    t.up()
    t.goto(x, y)
    t.setheading(90)
    t.color("black", "white")
    t.pensize(2 * scale)
    t.down()
    t.begin_fill()
    for _ in range(2):
        t.forward(30 * scale)
        t.circle(12 * scale, 180)
    t.end_fill()
    t.color("black")
    for sx, sy, sr in [(x - 5*scale, y + 15*scale, 4), (x - 10*scale, y + 25*scale, 3)]:
        t.up()
        t.goto(sx, sy)
        t.begin_fill()
        t.circle(sr)
        t.end_fill()
    t.up()
    t.goto(x - (12 * scale), y + (45 * scale))
    t.setheading(0)
    t.color("black", "white")
    t.down()
    t.begin_fill()
    t.circle(12 * scale)
    t.end_fill()
    for ex in [x - 26*scale, x + 2*scale]:
        t.up()
        t.goto(ex, y + 60*scale)
        t.begin_fill()
        t.circle(4*scale)
        t.end_fill()
    t.color("black", "yellow")
    for hx in [(-18, -22, -14), (-6, -2, -10)]:
        t.up()
        t.goto(x + hx[0]*scale, y + 65*scale)
        t.begin_fill()
        t.goto(x + hx[1]*scale, y + 73*scale)
        t.goto(x + hx[2]*scale, y + 68*scale)
        t.end_fill()
    t.up()
    t.goto(x - 12*scale, y + 45*scale)
    t.color("black", "pink")
    t.begin_fill()
    t.circle(6*scale)
    t.end_fill()
    t.color("black")
    t.up()
    t.goto(x - 16*scale, y + 61*scale)
    t.dot(3*scale)
    t.up()
    t.goto(x - 8*scale, y + 61*scale)
    t.dot(3*scale)
    draw_cow_limbs(t, x, y, facing_left_or_right, scale, is_player, holds_pennant)

# Main function - calls all of the other functions.
def main():
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)
    screen.bgcolor("skyblue")
    screen.tracer(0)
    # Used screen.tracer and screen.update to speed up the drawing process when debugging
    
    alex = turtle.Turtle()
    alex.hideturtle()

    # The sky
    draw_sun_with_rays(alex, -420, 280)
    for cx, cy in [(-850, 240), (-600, 270), (-300, 250), (-50, 280), (300, 230), (550, 260), (800, 250)]:
        draw_cloud(alex, cx, cy)
    draw_rainbow(alex)

    # The landscape
    mountains = [(-1000, 140, 280), (-750, 160, 300), (-500, 130, 250), (-250, 150, 220), (0, 120, 300), (250, 140, 260), (500, 160, 240), (750, 140, 300)]
    for mx, mh, mw in mountains:
        draw_mountain(alex, mx, 50, mw, mh)
    draw_meadow_ground(alex)
    draw_grass_texture(alex, 400)
    
    # The ice rink
    draw_ice_rink(alex)
    draw_left_goal(alex, -280, -180)
    draw_right_goal(alex, 280, -180)

    # The cows and the puck
    for _ in range(80):
        draw_small_cow(alex, random.randint(-400, 400), random.randint(-65, -15), 0.45)
    for _ in range(80):
        draw_small_cow(alex, random.randint(-400, 400), random.randint(-380, -320), 0.65)
    for _ in range(70):
        draw_small_cow(alex, random.randint(-550, -350), random.randint(-330, -50), 0.55)
    for _ in range(70):
        draw_small_cow(alex, random.randint(350, 550), random.randint(-330, -50), 0.55)
    
    draw_big_cow(alex, 100, -160, -1)
    draw_big_cow(alex, -100, -160, 1)

    draw_puck(alex, 0, -180)

# Used screen.tracer and screen.update to speed up the drawing process when debugging
    screen.update() 
    screen.exitonclick()

if __name__ == "__main__":
    main()