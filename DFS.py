from PIL import Image

import time

temps = 0

def dfs_solve_labyrinth(input_file):
    # Charger l'image du labyrinthe
    with Image.open(input_file) as img:
        pixels = img.convert("RGB").load()
        width, height = img.size
        

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

        # Recherche en profondeur pour trouver le chemin

        testpath = []
        totalTime = 0

        repeat = 50000
        for i in range(repeat):
            stack = [start]
            visited = {start}
            parent = {start: None}
            orangePath = []
            debut = time.time()
            while stack:
                current = stack.pop()

                if current == end:
                    break
                for neighbor in neighbors(current, pixels, width, height):
                    if neighbor not in visited:
                        stack.append(neighbor)
                        visited.add(neighbor)
                        parent[neighbor] = current
                        orangePath.append(neighbor)
            fin = time.time()
            totalTime = totalTime + (fin - debut)

        global temps
        temps = totalTime
        print("\033[32mTemps de résolution :\033[0m", temps, "(pour",repeat,"exécutions)")


        # Reconstituer le chemin
        path = []
        '''
        current = end
        while current != start:
            path.append(current)
            current = parent[current]
        path.append(start)
        path.reverse()

        
        savegif(path, output_file, 0,148,255)
        savegif(orangePath, output_file_step, 255,132,50)
        '''


        return path
    
def savegif(path, name, c1, c2, c3):
    images = []
    for i in range(len(path)):
        with Image.open(input_file) as img:
            for vertex in path[:i]:
                img.putpixel(vertex, (c1,c2,c3))
            images.append(img.resize((img.width * 4, img.height * 4)))

    # Sauvegarder le gif dans le fichier
    img.resize((img.width * 4, img.height * 4)).save(name+".gif", save_all=True, append_images=images[1:], 
        optimize=False, duration=20)
    images[-1].resize((img.width * 4, img.height * 4)).save(output_file+".png")


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
    input_file = "Mazes/maze7.png"
    output_file = "DFS/output"
    output_file_step = "DFS/step"
    dfs_solve_labyrinth(input_file)