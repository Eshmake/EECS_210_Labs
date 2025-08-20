#dijkstra.py

# Name: Sina Asheghalishahi
# KUID: 3127403
# LAB Session: Wednesday 11 a.m.
# LAB Assignment: 10
# Description: Program takes in as input an nxn weighted adjacency matrix, representing a simple connected undirected
# weighted graph, and 2 vertices, and produces the shortest path between the 2 vertices and its length as output.
# Collaborators: None

import math as m

def dijkstra(matrix, vertices):                                     # definition of dijkstra method, which receives a qualified graph matrix and list of start and end
    vertexList = [chr(i + 97) for i in range(len(matrix))]          # vertices, and outputs list containing both shortest path between vertices in given graph, and the
                                                                    # length of such path.

    verWeights = {v: float('inf') for v in vertexList}          # initialization of first vertex weight as 0, and weights of all other vertices as relative inf.

    prevVertices = {v: None for v in vertexList}  

    verWeights[vertices[0]] = 0  

    verMarked = {v: False for v in vertexList}           # initialization of "done" status of each vertes as false


    prevVertices = {v: None for v in vertexList}        # initialization of dict. containing vertices pointing to corresponding previous vertices


    while(not verMarked[vertices[1]]):                   # implementation of Dijikstra's Algorithm (i.e. minimal obtained, weights of unmarked vertices updated accordingly,
        u = minimal(verWeights, verMarked)              # and prevVertices dict. updated with minimal as previous vertex w/ respect to current vertex).

        verMarked[u] = True

        for v in vertexList:
            weight_uv = matrix[vertexList.index(u)][vertexList.index(v)]
            if(not verMarked[v] and weight_uv != -1):
                if(verWeights[u] + weight_uv < verWeights[v]):
                    verWeights[v] = verWeights[u] + weight_uv
                    prevVertices[v] = u


    path = derivePath(prevVertices, vertices[1])                 # vertex order of shortest path obtained via method call

    outputList = [v for v in path]

    finalLength = verWeights[vertices[1]]               # output list updated with shortest path and its length, and then returned
    outputList.append(str(finalLength))

    return outputList


def minimal(verWeights, verMarked):     # definition of minimal method, which received current weights and markings of vertices, and returns minimal vertex
    u = None
    minWeight = float('inf')
    
    for v, w in verWeights.items():                 # for all vertices, if a vertex is unmarked and its weight is less than current weight, update var. values
        if not verMarked[v] and w < minWeight:
            minWeight = w
            u = v

    return u                                # return minimal vertex


def derivePath(prevVertices, dest):       # definition of derivePath method, which returns ordered list of vertices in shortest path using given destination vertex
    pathList = []

    while(dest is not None):
        pathList.append(dest)

        dest = prevVertices[dest]
    
    pathList.reverse()

    return pathList


def main():

    graphMatrix = []

    n = int(input("Enter number of elements in matrix: "))              # input collection for size and contents of graph matrix

    size = int(m.sqrt(n))

    for i in range(size):
        row = []
        strList = input(f"Enter elements of row {i} of matrix (space-separated; -1 for infinite weight): ").split(" ")
        row = [int(j) for j in strList]

        graphMatrix.append(row)
    
    vertices = input("Enter 2 vertices (space-separated): ").split(" ")         # input collection for start and end vertices
    
    outputList = dijkstra(graphMatrix, vertices)            # call dijikstra method on given graph and vertices

    print(", ".join(outputList[:-1]), end=" ")          # output shortest path and its length to terminal
    print(f" {outputList[-1]}")

main()              #call main method