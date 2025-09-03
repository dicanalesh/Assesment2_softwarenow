import turtle
import math

#Function to draw a fractal side (Koch-like)
# We have to use recursion function similar to factorial function.
# To make a recursive function, we need a base case and a recursive case.
# Base case: when depth is 0, just draw a straight line.
# Recursive case: divide the line into 3 parts, draw the middle part as a peak
# The base case must be utilize in the recursive case.
# The recursive case must call itself with a reduced depth.
# When depth is reduced to 0, the base case will be executed and act as exit.
# The base case must be at the begining of the function to avoid infinite recursive calls.

def fractal_side(pen, length, depth):
    if depth == 0: # Base case
        pen.forward(length)
    else:
        length /= 3 # Divide the line into 3 parts every time we go deeper in recursion
        fractal_side(pen, length, depth - 1) # First segment
        pen.left(60) # Turn left to create the peak
        fractal_side(pen, length, depth - 1) # Second segment (the peak)
        pen.right(120) # Turn right to create the other side of the peak
        fractal_side(pen, length, depth - 1) # Third segment
        pen.left(60) # Turn left to align with the original direction
        fractal_side(pen, length, depth - 1) # Last segment
# We use 60 and 120 degrees to create the Koch curve shape (equilateral triangle peak).
# First 60 degrees ar the internal angle of an equilateral triangle.
# 120 degrees is the external angle (180 - 60).
# When depth is 0, it draws a straight line.

# Función para dibujar un polígono fractal
# We have to draw a isogonal polygon with the numer of sides given by de the user.

def draw_fractal_polygon(pen, sides, length, depth): #We use the object pen from turtle module to draw
    angle = 360 / sides # Calculate the external angle of the polygon, which is the same for all isogonal polygons.
    for i in range(sides):
        fractal_side(pen, length, depth)
        pen.right(angle)
# When the pen finish one side will start drwaing the next side inmideately.
# The pen will draw with the fractal_side how many sides the user input.
#When the pen finish one side will turn right the next external angle of the polygon to start drawing the next side.

# -------------------------
# Main program
# -------------------------
# Inputs
# Ask details from user. We need 3 data: number of sides, side length, and depth.
sides = int(input("Enter the number of sides: "))
length = int(input("Enter the side length: "))
depth = int(input("Enter the recursion depth: "))

# Setup turtle screen
screen = turtle.Screen()
screen.setup(width=800, height=800) # Set up window size
screen.title("Fractal Polygon")   
screen.tracer(0, 0)  # Disable animation for faster drawing

# Setup turtle pen
pen = turtle.Turtle() # Create a turtle pen 
pen.color("blue")
pen.pensize(2)
pen.speed(0) # Set drawing speed to maximum
pen.hideturtle() # Hide the turtle cursor. It looks cleaner.

# Calcular tamaño máximo para centrar
# Ajuste automático según número de lados y profundidad
total_length = length * (4/3) ** depth  # Aproximación del crecimiento del fractal
radius = total_length / (2 * math.sin(math.pi / sides))

# Centrar tortuga
pen.penup()
pen.goto(-radius, radius / 2)  # Ajuste vertical
pen.pendown()

# Dibujar fractal
draw_fractal_polygon(pen, sides, length, depth)

turtle.update()      # Mostrar todo de golpe
turtle.exitonclick() # Cierra al hacer clic
