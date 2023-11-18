import Dijkstra
import AStar
import RightHand
import Random
import DER
import DFS


def moyenne(liste):
    if not liste:
        raise ValueError("La liste est vide.")
    
    total = sum(liste)
    moyenne = total / len(liste)
    return moyenne

count = 0
count2 = 0
count3 = 0
totalTime = []

'''

while count < 100:
    Dijkstra.input_file = "BigMazes/maze"+str(count)+".png"
    Dijkstra.output_file = "Dijkstra/maze"+str(count)
    Dijkstra.solve_labyrinth(Dijkstra.input_file, Dijkstra.output_file)

    count += 1
    totalTime.append(Dijkstra.temps)
    # print("\033[34mTemps de résolution")
    print("Labyrinthe : ",count," moyenne actuelle :", moyenne(totalTime))


print("===============================\n\033[34mDijkstra Temps Moyen : \033[0m" + str(moyenne(totalTime)))



while count2 < 100:
    RightHand.input_file = "BigMazes/maze"+str(count2)+".png"
    RightHand.output_file = "RightHand/output"+str(count2)
    RightHand.solve_labyrinth(RightHand.input_file, RightHand.output_file)

    count2 += 1
    totalTime.append(RightHand.temps)
    # print("\033[34mTemps de résolution")
    print("Labyrinthe : ",count2," moyenne actuelle :", moyenne(totalTime))


print("===============================\n\033[34mRightHand Temps Moyen : \033[0m" + str(moyenne(totalTime)))



while count < 100:
    AStar.input_file = "BigMazes/maze"+str(count)+".png"
    AStar.output_file = "AStar/output"+str(count)
    AStar.solve_labyrinth(AStar.input_file, AStar.output_file)

    count += 1
    totalTime.append(AStar.temps)
    # print("\033[34mTemps de résolution")
    print("Labyrinthe : ",count," moyenne actuelle :", moyenne(totalTime))


print("===============================\n\033[34mAstar Temps Moyen : \033[0m" + str(moyenne(totalTime)))



while count < 100:
    Random.input_file = "BigMazes/maze"+str(count)+".png"
    Random.output_file = "Random/output"+str(count)
    Random.solve_labyrinth(Random.input_file)

    count += 1
    totalTime.append(Random.temps)
    # print("\033[34mTemps de résolution")
    print("Labyrinthe : ",count," moyenne actuelle :", moyenne(totalTime))


print("===============================\n\033[34mRandom Temps Moyen : \033[0m" + str(moyenne(totalTime)))



while count < 100:
    DER.input_file = "BigMazes/maze"+str(count)+".png"
    DER.output_file = "DER/output"+str(count)
    DER.solve_labyrinth(DER.input_file, DER.output_file)

    count += 1
    totalTime.append(DER.temps)
    # print("\033[34mTemps de résolution")
    print("Labyrinthe : ",count," moyenne actuelle :", moyenne(totalTime))


print("===============================\n\033[34mDER Temps Moyen : \033[0m" + str(moyenne(totalTime)))

'''

while count < 100:
    DFS.input_file = "BigMazes/maze"+str(count)+".png"
    DFS.output_file = "DFS/output"+str(count)
    DFS.dfs_solve_labyrinth(DFS.input_file)

    count += 1
    totalTime.append(DFS.temps)
    # print("\033[34mTemps de résolution")
    print("Labyrinthe : ",count," moyenne actuelle :", moyenne(totalTime))
    estimated = (moyenne(totalTime)*(100-count))/60
    print("\rTemps estimé :",estimated,"minutes")

    


print("===============================\n\033[34mDFS Temps Moyen : \033[0m" + str(moyenne(totalTime)))

