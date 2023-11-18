import random
from PIL import Image

def generate_maze(width, height):
    # Création d'une grille vide
    maze = [[0 for _ in range(width)] for _ in range(height)]

    # Définition des directions (haut, droite, bas, gauche)
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    # Fonction pour vérifier si une cellule est valide et non visitée
    def is_valid(x, y):
        return 0 <= x < width and 0 <= y < height and maze[y][x] == 0

    # Fonction pour vérifier si une cellule a des voisins non visités
    def has_unvisited_neighbors(x, y):
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                return True
        return False

    # Fonction pour effectuer la recherche en profondeur
    def dfs(x, y):
        maze[y][x] = 1  # Marquer la cellule comme visitée

        # Mélanger les directions pour explorer aléatoirement
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2  # Calculer les coordonnées du voisin
            if is_valid(nx, ny):
                maze[ny][nx] = 1  # Marquer le voisin comme visité
                maze[y + dy][x + dx] = 1  # Supprimer le mur entre la cellule courante et le voisin
                dfs(nx, ny)  # Continuer la recherche en profondeur à partir du voisin

    # Choisir un point de départ aléatoire (uniquement les cellules impaires)
    start_x, start_y = random.randint(1, width - 1) // 2 * 2 + 1, random.randint(1, height - 1) // 2 * 2 + 1
    dfs(start_x, start_y)

    return maze

def generate_pixel_art(maze):
    width, height = len(maze[0]), len(maze)
    image = Image.new("RGB", (width, height), (255, 255, 255))
    pixels = image.load()

    for y in range(height):
        for x in range(width):
            if maze[y][x] == 1:
                pixels[x, y] = (255, 255, 255)  # Noir pour représenter les murs
            else:
                pixels[x, y] = (0, 0, 0)  # Blanc pour représenter les chemins

    pixels[0, 1] = (255, 0, 0)
    pixels[width-1, height-2] = (0, 255, 0)

    return image



if __name__ == "__main__":
    nb_mazes = 10
    for i in range(0,100):
        success = False
        width, height = 41, 41
        while (success == False):
            try:
                maze = generate_maze(width, height)
                pixel_art = generate_pixel_art(maze)
                success = True

                if pixel_art.getpixel((1, 1)) == (0, 0, 0) or pixel_art.getpixel((width-2, height-2)) == (0, 0, 0):
                    success = False
            except Exception as e:
                print("Une erreur s'est produite :", e)
                success = False
        pixel_art.save(f"BigMazes/maze{i}.png")