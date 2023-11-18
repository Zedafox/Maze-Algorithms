import heapq
from PIL import Image
import time

temps = 0

def heuristic(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

def astar(img, pixels, width, height, graph, start, end):
    debut = time.time()
    from_vertex = {}
    repeat = 50000
    for i in range(repeat):
        queue = [(0, start)]
        distances = {vertex: float('inf') for vertex in graph}
        distances[start] = 0
        current_distance = 0
        current_vertex = start
        testpath = []
        while queue:
            current_distance, current_vertex = heapq.heappop(queue)
            testpath.append(current_vertex)
            if current_vertex == end:
                break
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in graph.get(current_vertex, {}).items():
                edistance = heuristic(neighbor, end)
                distance = current_distance + weight + edistance
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (edistance, neighbor))
    fin = time.time()

    debut2 = time.time()
    for i in range(repeat):
        queue2 = [(0, start)]
        distances2 = {vertex: float('inf') for vertex in graph}
        distances2[start] = 0
        current_distance2 = 0
        current_vertex2 = start
        testpath2 = []
    fin2 = time.time()

    global temps
    temps1 = fin - debut
    temps2 = fin2 - debut2
    temps = temps1 - temps2
    print("\033[32mTemps de résolution :\033[0m", temps, "(pour",repeat,"exécutions)")

    print(len(testpath))
    images = []
    # Dessiner le chemin sur une nouvelle image

    '''
    for i in range(len(testpath)):
        with Image.open(input_file) as img:
            for vertex in testpath[:i]:
                img.putpixel(vertex, (255, 132, 50))  # pixel noir = chemin du plus court
            images.append(img.resize((img.width * 4, img.height * 4)))



    # Sauvegarder le gif dans un fichier
    img.resize((img.width * 4, img.height * 4)).save("AStar/step.gif", save_all=True, append_images=images[1:], 
        optimize=False, duration=20)
    print("image saved")
    '''

    path = []

    '''
    vertex = end
    while vertex != start:
        path.append(vertex)
    '''
    path.append(start)


    print("\033[32mLonguer du chemin :\033[0m", len(path), "pixels")
    print("\033[32mPixels Visités :\033[0m", len(testpath))

    return path[::-1]

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
            path = astar(img, pixels, width, height, graph, start, end)

        images = []
        # Dessiner le chemin sur une nouvelle image

        '''
        for i in range(len(path)):
            with Image.open(input_file) as img:
                for vertex in path[:i]:
                    img.putpixel(vertex, (0, 148, 255))
                images.append(img.resize((img.width * 4, img.height * 4)))



        # Sauvegarder le gif dans un fichier
        img.resize((img.width * 4, img.height * 4)).save(output_file+".gif", save_all = True, append_images = images[1:], 
               optimize = False, duration = 20)
        # Sauvegarder l'image dans un fichier
        images[-1].resize((img.width * 4, img.height * 4)).save(output_file+".png")
        '''


if __name__ == '__main__':
    input_file = "Mazes/maze1.png"
    output_file = "AStar/output"
    solve_labyrinth(input_file, output_file)

