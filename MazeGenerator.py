import random
import os
from PIL import Image

width = 41
height = 41

# 0 = mur    1 = horizontal    2 = vertical

def generate_maze(width, height):

    image = Image.new("RGB", (width, height), (255, 255, 255))
    pixels = image.load()
    # Création de la grille de cellules
    maze = [[0 for _ in range(width)] for _ in range(height)]

    for y in range(width):
        for x in range(height):
            # Mettre des pixels noirs dans les contours
            if x in (0, width-1) or y in (0, height-1):
                pixels[x, y] = (0, 0, 0)
            else:
                if(y%2 != 0):
                    if(x%2 != 0 and random.choice([0, 1]) == 0):
                        maze[y][x] = 2
                        pixels[x, y] = (255, 255, 255)
                    elif(x%2 == 0 and random.choice([0, 1]) == 0):
                        maze[y][x] = 0
                        pixels[x, y] = (0, 0, 0)
                    else:
                        maze[y][x] = 1
                        pixels[x, y] = (255, 255, 255)
                # Le fait une ligne sur deux
                else:
                    if(maze[y-1][x-1] == 0 and maze[y-1][x+1] == 0):
                        maze[y][x] = 2
                        pixels[x, y] = (255, 255, 255)
                    elif(maze[y-1][x] == 2):
                        maze[y][x] = 2
                        pixels[x, y] = (255, 255, 255)
                    elif(maze[y-1][x] == 1):
                        maze[y][x] = 0
                        pixels[x, y] = (0, 0, 0)
                    elif(maze[y-1][x] == 0):
                        maze[y][x] = 0
                        pixels[x, y] = (0, 0, 0)

    pixels[0,1] = (255,0,0)
    pixels[width-1,height-2] = (0,255,0)
                    

    image.save("MazeGenerated/maze"+str(nb)+".png")
                     

"""
def generate_pixel_art(maze):
    image = Image.new("RGB", (width, height), (255, 255, 255))
    pixels = image.load()

    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 1:
                pixels[x, y] = (255, 255, 255)
            elif maze[y][x] == 0:
                pixels[x, y] = (0, 0, 0)

    image.save("C:/Users/Benja/Desktop/ici/maze.png")
"""


nb = 0
for i in range(1):
    generate_maze(width, height)
    nb += 1