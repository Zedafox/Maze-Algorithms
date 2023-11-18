import heapq
from PIL import Image
import time

final = []
temps = 0

def rightHand(img, pixels, width, height, graph, start, end):
    # 0 : à droite, 1 : en bas, 2 : à gauche, 3: en haut
    repeat = 50000
    totalTime = 0
    for i in range(repeat):
        current = start
        direction = 0
        path = []
        debut = time.time()
        while(current != end):
            if direction == 0:
                if current[1] < height-1 and pixels[current[0], current[1]+1] != (0, 0, 0):
                    current = current[0], current[1]+1
                    direction = 1
                    path.append(current)
                elif current[0] < width-1 and pixels[current[0]+1, current[1]] != (0, 0, 0):
                    current = current[0]+1, current[1]
                    path.append(current)
                elif current[1] > 0 and pixels[current[0], current[1]-1] != (0, 0, 0):
                    current = current[0], current[1]-1
                    direction = 3
                    path.append(current)
                else:
                    path.append(current)
                    direction = 2
            if direction == 1:
                if current[0] > 0 and pixels[current[0]-1, current[1]] != (0, 0, 0):
                    current = current[0]-1, current[1]
                    direction = 2
                    path.append(current)
                elif current[1] < height-1 and pixels[current[0], current[1]+1] != (0, 0, 0):
                    current = current[0], current[1]+1
                    path.append(current)
                elif current[0] < width-1 and pixels[current[0]+1, current[1]] != (0, 0, 0):
                    current = current[0]+1, current[1]
                    direction = 0
                    path.append(current)
                else:
                    path.append(current)
                    direction = 3
            if direction == 2:
                if current[1] > 0 and pixels[current[0], current[1]-1] != (0, 0, 0):
                    current = current[0], current[1]-1
                    direction = 3
                    path.append(current)
                elif current[0] > 0 and pixels[current[0]-1, current[1]] != (0, 0, 0):
                    current = current[0]-1, current[1]
                    path.append(current)
                elif current[1] < height-1 and pixels[current[0], current[1]+1] != (0, 0, 0):
                    current = current[0], current[1]+1
                    direction = 1
                    path.append(current)
                else:
                    path.append(current)
                    direction = 0
            if direction == 3:
                if current[0] < width-1 and pixels[current[0]+1, current[1]] != (0, 0, 0):
                    current = current[0]+1, current[1]
                    direction = 0
                    path.append(current)
                elif current[1] > 0 and pixels[current[0], current[1]-1] != (0, 0, 0):
                    current = current[0], current[1]-1
                    path.append(current)
                elif current[0] > 0 and pixels[current[0]-1, current[1]] != (0, 0, 0):
                    current = current[0]-1, current[1]
                    direction = 2
                    path.append(current)
                else:
                    path.append(current)
                    direction = 1

        fin = time.time()
        totalTime = totalTime + (fin - debut)
    global temps
    temps = totalTime
    print("\033[32mTemps de résolution :\033[0m", temps, "(pour",repeat,"exécutions)")

    print("\033[32mPixels Visités :\033[0m", len(path))

    return path


def solve_labyrinth(input_file, output_file):
    # Charger l'image du labyrinthe
    with Image.open(input_file) as img:
        pixels = img.convert("RGB").load()
        width, height = img.size

        # Créer un graph pour représenter le labyrinthe
        graph = {}
        for x in range(width):
            for y in range(height):
                if not pixels[x, y] == (0, 0, 0):  # pixel noir = mur
                    vertex = (x, y)
                    edges = {}
                    if x > 0 and pixels[x-1, y] != (0, 0, 0):
                        edges[(x-1, y)] = 1  # pixel blanc = chemin possible
                    if x < width-1 and pixels[x+1, y] != (0, 0, 0):
                        edges[(x+1, y)] = 1
                    if y > 0 and pixels[x, y-1] != (0, 0, 0):
                        edges[(x, y-1)] = 1
                    if y < height-1 and pixels[x, y+1] != (0, 0, 0):
                        edges[(x, y+1)] = 1
                    graph[vertex] = edges

        # Trouver les sommets de départ et d'arrivée
        start = None
        end = None
        for x in range(width):
            for y in range(height):
                if pixels[x, y] == (255, 0, 0):  # pixel rouge = point de départ
                    start = (x, y)
                elif pixels[x, y] == (0, 255, 0):  # pixel vert = point d'arrivée
                    end = (x, y)
                if start and end:
                    break
            if start and end:
                break

        # Trouver le chemin le plus court
        if(start and end):
            path = rightHand(img, pixels, width, height, graph, start, end)

        images = []
        # Dessiner le chemin sur une nouvelle image
        visited = []
        '''
        for i in range(len(path)):
            with Image.open(input_file) as img:
                visited = []
                for vertex in path[:i]:
                    if vertex in visited:
                        img.putpixel(vertex, (204, 55, 55))
                    else:
                        img.putpixel(vertex, (255, 132, 50))
                        visited.append(vertex)
                images.append(img.resize((img.width * 4, img.height * 4)))


        # Sauvegarder le gif dans le fichier
        img.resize((img.width * 4, img.height * 4)).save(output_file+".gif", save_all=True, append_images=images[1:], 
            optimize=False, duration=20)
        # Sauvegarder l'image dans le fichier
        images[-1].resize((img.width * 4, img.height * 4)).save(output_file+".png")
        '''



def neighbors(vertex, pixels, width, height):
    x, y = vertex
    neighbors = []
    if x > 0 and pixels[x-1, y] != (0, 0, 0):
        neighbors.append((x-1, y))
    if x < width-1 and pixels[x+1, y] != (0, 0, 0):
        neighbors.append((x+1, y))
    if y > 0 and pixels[x, y-1] != (0, 0, 0):
        neighbors.append((x, y-1))
    if y < height-1 and pixels[x, y+1] != (0, 0, 0):
        neighbors.append((x, y+1))
    return neighbors

if __name__ == '__main__':
    input_file = "Input/input24.png"
    output_file = "RightHand/output"
    solve_labyrinth(input_file, output_file)

