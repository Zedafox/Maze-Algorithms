import heapq
from PIL import Image
import time

final = []
temps = 0

def dijkstra(img, pixels, width, height, graph, start, end):
    debut = time.time()

    repeat = 2
    for i in range(repeat):
        queue = [(0, start)]
        distances = {vertex: float('inf') for vertex in graph}
        current_distance = 0
        current_vertex = start
        testpath = []
        while queue:
            current_distance, current_vertex = heapq.heappop(queue)
            if(current_vertex == end):
                break
            testpath.append(current_vertex)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in graph.get(current_vertex, {}).items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
    fin = time.time()

    '''
    debut2 = time.time()
    for i in range(repeat):
        queue2 = [(0, start)]
        distances2 = {vertex: float('inf') for vertex in graph}
        current_distance2 = 0
        current_vertex2 = start
        testpath2 = []
    fin2 = time.time()
    '''

    global temps
    temps1 = fin - debut
    temps2 = 0
    temps = temps1 - temps2
    print("\033[32mTemps de résolution :\033[0m", temps, "(pour",repeat,"exécutions)")

    images = []
    
    '''
    # Dessiner le chemin sur une nouvelle image
    for i in range(len(testpath)):
        with Image.open(input_file) as img:
            for vertex in testpath[:i]:
                img.putpixel(vertex, (255, 132, 50))
            images.append(img.resize((img.width * 4, img.height * 4)))


    # Sauvegarder le gif dans un fichier
    img.resize((img.width * 4, img.height * 4)).save("Dijkstra/step.gif", save_all=True, append_images=images[1:], 
        optimize=False, duration=20)
    '''
    

    path = []
    vertex = end
    while vertex != start:
        path.append(vertex)
        vertex = min(graph[vertex], key=lambda x: distances[x] + graph[vertex][x])
    path.append(start)

    print("\033[32mLonguer du chemin :\033[0m", len(path), "pixels")
    print("\033[32mPixels Visités :\033[0m", len(testpath))
    

    return path[::-1]

def solve_labyrinth(input_file, output_file):
    
    with Image.open(input_file) as img:
        pixels = img.convert("RGB").load()
        width, height = img.size

        
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
            path = dijkstra(img, pixels, width, height, graph, start, end)

        images = []
        # Dessiner le chemin sur une nouvelle image
        
        for i in range(len(path)):
            with Image.open(input_file) as img:
                for vertex in path[:i]:
                    img.putpixel(vertex, (0, 148, 255))
                images.append(img.resize((img.width * 1, img.height * 1)))

                
        '''
        # Sauvegarder le gif dans le fichier
        img.resize((img.width * 4, img.height * 4)).save(output_file+".gif", save_all=True, append_images=images[1:], 
            optimize=False, duration=20)
        '''


        # Sauvegarder l'image dans le fichier
        images[-1].save(output_file+".png")
        


if __name__ == '__main__':
    input_file = "Input/input.png"
    output_file = "Dijkstra/output"
    solve_labyrinth(input_file, output_file)

def solve():
    input_file = "Input/input25.png"
    output_file = "Dijkstra/output"
    solve_labyrinth(input_file, output_file)
