#eulerCircuit.py

# Name: Sina Asheghalishahi
# KUID: 3127403
# LAB Session: Wednesday 11 a.m.
# LAB Assignment: 10
# Description: Program takes in as input an nxn 0-1 adjacency matrix representing a connected simple undirected graph
# w/ all vertices of even degree, and produces as output the resp. Euler circuit.
# Collaborators: None

import math as m

def euler(matrix):
    vertexList = [chr(i + 97) for i in range(len(matrix))]
    circuit = ["a"]

    newMatrix = copyMatrix(matrix)

    curr = "a"

    check = False

    while(not check):
        foundPath = False

        i = vertexList.index(curr)
        for j in range(len(newMatrix[0])):
            if(newMatrix[i][j] == 1):
               circuit.append(vertexList[j])
               curr = vertexList[j]

               newMatrix[i][j] = 0
               newMatrix[j][i] = 0
               foundPath = True
               break

        if(curr == "a" and foundPath):
            check = True
    
    while(hasOne(newMatrix)):
        prev = ""
        curr = ""
        subcircuit = []

        for i in range(len(newMatrix)):
            for j in range(len(newMatrix[0])):
                if(newMatrix[i][j] == 1 and vertexList[i] in circuit):
                    subcircuit.append(vertexList[i])
                    prev = vertexList[i]
                    break
            if(len(subcircuit) > 0):
                break

        while(prev != curr):
            if(curr != ""):
                prev = curr

            i = vertexList.index(prev)
            for j in range(len(newMatrix[0])):
                if(newMatrix[i][j] == 1):
                    subcircuit.append(vertexList[j])
                    
                    newMatrix[i][j] = 0
                    newMatrix[j][i] = 0
                    curr = vertexList[j]
                    break
        
        circuit = mergeCircuits(circuit, subcircuit)

    
    if(circuit[-1] != "a"):
        circuit.append("a")
    
    return circuit


def hasOne(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j] == 1):
                return True
      
    return False


def copyMatrix(matrix):                 #helper func. defined that simply returns a copy of a given matrix
    newMatrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(matrix[i][j])
        newMatrix.append(row)

    return newMatrix            #copy of given matrix returned as output


def mergeCircuits(cir1, cir2):          #check merge
    
    index = cir1.index(cir2[0])

    cir1 = cir1[:index+1] + cir2[1:] + cir1[index+1:]

    return cir1
    


def main():
    graphMatrix = []
    eulerCircuit = []

    n = int(input("Enter number of elements in matrix: "))              #input collection for size and contents of graph matrix

    size = int(m.sqrt(n))

    for i in range(size):
        row = []
        strList = input(f"Enter elements of row {i} of matrix (space-separated): ").split(" ")
        row = [int(j) for j in strList]

        graphMatrix.append(row)

    eulerCircuit = euler(graphMatrix)

    print(", ".join(eulerCircuit))

main()