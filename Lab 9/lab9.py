# Daniel Williamson
import turtle
# turtle.tracer makes turtle happen instantly
turtle.tracer(0)

# reads text file stars.txt
file = open("stars.txt", "r")

'''
dict's created to hold data from stars.txt that's
created by the function read_cords
'''

magnitude_dict = {}
coordinate_dict = {}
name_of_star = {}

'''
read_cords function reads the coordinates from the stars.txt
file and uses the split and join methods to put the
data into a usable form from which we can make our
stars
'''


def read_cords(file):
    for i in file:
        data = i.split(" ")
        names = data[3]
        magnitude_dict[names] = data[4]
        coordinate_dict[names] = (data[0], data[1])
        if len(data) >= 6:
            line1 = ' '.join(data[6:])
            line2 = line1.split(";")
            for i in line2:
                name_of_star[i.strip()] = names
        star_data = (coordinate_dict, magnitude_dict, name_of_star)
    return star_data

'''
plot_plain_stars function plots the coordinates of the stars,
makes them squares, makes the picture black, and the line drawn
by turtle white then fills it with white making an all white
square for each star in its correct position.
'''

'''
def plot_plain_stars(picture_size, coordinates_dict):
    turtle.setup(picture_size, picture_size)
    turtle.bgcolor("black")
    turtle.pencolor("white")
    turtle.fillcolor("white")
    for i in coordinates_dict:
        x_cord = float(coordinates_dict[i][0])
        y_cord = float(coordinates_dict[i][1])
        turtle.penup()
        turtle.goto(((picture_size*x_cord)/2), (picture_size*y_cord)/2)
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(2)
        turtle.right(90)
        turtle.forward(2)
        turtle.right(90)
        turtle.forward(2)
        turtle.right(90)
        turtle.forward(2)
        turtle.right(90)
        turtle.end_fill()
        turtle.penup()
    turtle.exitonclick()
'''

'''
plot_by_magnitude goes to each coordinate and essentially overwrites the
stars in plot_plain_stars and incorporates the magnitude of the star
given to us in the txt file. Making plot_plain_stars useless.
'''


def plot_by_magnitude(picture_size, coordinates_dict, magnitudes_dict):
    turtle.setup(picture_size, picture_size)
    turtle.bgcolor("black")
    turtle.pencolor("white")
    turtle.fillcolor("white")
    for i in magnitudes_dict:
        x_cord = float(coordinates_dict[i][0])
        y_cord = float(coordinates_dict[i][1])
        mag_cord = float(magnitudes_dict[i])
        magnitude = round(10.0/(mag_cord+2))
        turtle.penup()
        turtle.goto(((x_cord*picture_size)/2), (y_cord*picture_size)/2)
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(magnitude)
        turtle.right(90)
        turtle.forward(magnitude)
        turtle.right(90)
        turtle.forward(magnitude)
        turtle.right(90)
        turtle.forward(magnitude)
        turtle.right(90)
        turtle.end_fill()
        turtle.penup()
    turtle.exitonclick()

star_data = read_cords(file)

plot_by_magnitude(700, star_data[0], star_data[1])
