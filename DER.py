import heapq
from PIL import Image
import time

final = []
temps = 0

def der(img, pixels, width, height, graph, start, end):
    path = []
    alone = 1
    debut = time.time()
    repeat = 50000

    for i in range(repeat):
        alone = 1
        while alone != 0:
            alone = 0
            graph = {}
            for x in range(width):
                for y in range(height):
                    if not pixels[x, y] == (0, 0, 0) and not pixels[x, y] == (255, 0, 0) and not pixels[x, y] == (0, 255, 0):  # pixel noir = mur
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

            for vertex in graph:
                if neighbors(vertex, pixels, width, height) == 1:
                    path.append(vertex)
                    pixels[vertex] = (0, 0, 0)
                    alone += 1

    fin = time.time()
    global temps
    temps = fin - debut
    print("\033[32mTemps de résolution :\033[0m", temps, "(pour",repeat,"exécutions)")
        

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
                if not pixels[x, y] == (0, 0, 0) and not pixels[x, y] == (255, 0, 0) and not pixels[x, y] == (0, 255, 0):  # pixel noir = mur
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
            path = der(img, pixels, width, height, graph, start, end)

        images = []
        # Dessiner le chemin sur une nouvelle image
        '''
        for i in range(len(path)):
            with Image.open(input_file) as img:
                for vertex in path[:i]:
                    img.putpixel(vertex, (0, 0, 0))
                images.append(img.resize((img.width * 4, img.height * 4)))


        # Sauvegarder le gif dans le fichier
        img.resize((img.width * 4, img.height * 4)).save(output_file+".gif", save_all=True, append_images=images[1:], 
            optimize=False, duration=20)
        # Sauvegarder l'image dans le fichier
        images[-1].resize((img.width * 4, img.height * 4)).save(output_file+".png")
        '''


def neighbors(vertex, pixels, width, height):
    x, y = vertex
    nCount = 0
    if x > 0 and pixels[x-1, y] != (0, 0, 0):
        nCount += 1
    if x < width-1 and pixels[x+1, y] != (0, 0, 0):
        nCount += 1
    if y > 0 and pixels[x, y-1] != (0, 0, 0):
        nCount += 1
    if y < height-1 and pixels[x, y+1] != (0, 0, 0):
        nCount += 1
    return nCount

if __name__ == '__main__':
    input_file = "Input/input.png"
    output_file = "DER/output"
    solve_labyrinth(input_file, output_file)

