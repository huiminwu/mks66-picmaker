import random
import math
pic = open("pic.ppm", "w+")

width = 500
height = 500
max_val = 255

def header():
    pic.write("P3" + "\n")
    pic.write(str(width) + " " + str(height) + "\n")
    pic.write(str(max_val) + "\n")

def body():
    for x in range(width):
        for y in range(height):
            if (x > 110 and x < 390):
                #equation of semicircle. Had to math.floor because then you would get a striped mouth
                eq = math.floor(-1 * math.sqrt(20000 - pow(x - 250, 2)) + 250)
                #creates mouth
                if (y == eq  or
                        y == eq + 1 or
                        y == eq + 2 or
                        y == eq + 3 or
                        y == eq + 4 or
                        y == eq + 5):
                    pic.write("0 0 0\n")
                #creates eyes
                elif (y < 300 and y > 250 and (x == 200 or x == 201 or x == 202 or x == 300 or x == 301 or x == 302)):
                    pic.write("0 0 0\n")
                else:
                    #gradient of yellow
                    r = 255
                    g = 255
                    #divided the two so b doesnt go to 255 as fast
                    b = x / 2
                    pic.write(str(r) + " " + str(g) + " " + str(b) + "\n")
            elif (y < 250) :
                r = 255
                g = random.randint(0,255)
                b = y
                pic.write(str(r) + " " + str(g) + " " + str(b) + "\n")
            else:
                g = y / 2
                r = random.randint(0,255)
                b = 255
                pic.write(str(r) + " " + str(g) + " " + str(b) + "\n")

header()
body()
pic.close()
