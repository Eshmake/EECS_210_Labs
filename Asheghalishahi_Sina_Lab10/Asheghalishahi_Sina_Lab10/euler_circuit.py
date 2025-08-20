#euler_circuit.py

# Name: Sina Asheghalishahi
# KUID: 3127403
# LAB Session: Wednesday 11 a.m.
# LAB Assignment: 10
# Description: Program takes in as input an nxn 0-1 adjacency matrix representing a connected simple undirected graph
# w/ all vertices of even degree, and produces as output the resp. Euler circuit.
# Collaborators: None

import math as m

def eulerCircuit(graphMatrix):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    vertexList = []

    for i in range(len(graphMatrix)):
        vertexList.append(alphabet[i])

    circuit = []

    prevIndices = [-1, -1]
    currIndices = []


    for i in range(len(graphMatrix)):
        for j in range(len(graphMatrix[0])):
            if(graphMatrix[i][j] == 1):
                currIndices.append(i)
                currIndices.append(j)
                break
        if(len(currIndices) == 2):
            break

    
    currVertex = vertexList[currIndices[1]]
    targetVertex = currVertex
    check = False

    circuit.append(currVertex)

    while(not check or targetVertex != currVertex):
        check = True

        for i in range(len(graphMatrix[0])):
            if(graphMatrix[currIndices[1]][i] == 1):
                if((currIndices[0] != currIndices[1] or i != currIndices[1]) and (currIndices[0] != prevIndices[0] or i != prevIndices[1])):
                    prevIndices[0] = currIndices[0]
                    prevIndices[1] = currIndices[1]

                    currIndices[0] = currIndices[1]
                    currIndices[1] = i
                    currVertex = vertexList[i]
                    break
                elif(i==len(graphMatrix[0])-1):
                    for j in range(len(graphMatrix[0])):
                        if(graphMatrix[currIndices[1]][j] == 1):
                            prevIndices[0] = currIndices[0]
                            prevIndices[1] = currIndices[1]

                            currIndices[0] = currIndices[1]
                            currIndices[1] = j
                            currVertex = vertexList[j]
                            break
        
        circuit.append(currVertex)

        graphMatrix2 = extract(graphMatrix, circuit, vertexList)

        while(hasOne(graphMatrix2)):
            subcircuit = []

            prevIndices = [-1, -1]
            currIndices = []


            for i in range(len(graphMatrix2)):
                for j in range(len(graphMatrix2[0])):
                    if(graphMatrix2[i][j] == 1 and vertexList[j] in circuit):
                        currIndices.append(i)
                        currIndices.append(j)
                        break
                if(len(currIndices) == 2):
                    break

            
            currVertex = vertexList[currIndices[1]]
            targetVertex = currVertex
            check = False

            circuit.append(currVertex)

            while(not check or targetVertex != currVertex):
                check = True

                for i in range(len(graphMatrix2[0])):
                    if(graphMatrix2[currIndices[1]][i] == 1):
                        if((currIndices[0] != currIndices[1] or i != currIndices[1]) and (currIndices[0] != prevIndices[0] or i != prevIndices[1])):
                            prevIndices[0] = currIndices[0]
                            prevIndices[1] = currIndices[1]

                            currIndices[0] = currIndices[1]
                            currIndices[1] = i
                            currVertex = vertexList[i]
                            break
                        elif(i==len(graphMatrix2[0])-1):
                            for j in range(len(graphMatrix2[0])):
                                if(graphMatrix2[currIndices[1]][j] == 1):
                                    prevIndices[0] = currIndices[0]
                                    prevIndices[1] = currIndices[1]

                                    currIndices[0] = currIndices[1]
                                    currIndices[1] = j
                                    currVertex = vertexList[j]
                                    break
        
                subcircuit.append(currVertex)

                graphMatrix2 = extract(graphMatrix2, circuit, vertexList)

            circuit = mergeCircuits(circuit, subcircuit)

    

    return circuit


def extract(graphMatrix, circuit, vertices):

    for i in range(1, len(circuit)):
        graphMatrix[vertices.index(circuit[i-1])][vertices.index(circuit[i])] = 0

    return graphMatrix



def mergeCircuits(cir1, cir2):

    index = cir1.index(cir2[0])

    cir1.remove(cir2[0])

    for i in range(len(cir2)):
        cir1.insert(index+i, cir2[i])

    return cir1


def hasOne(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j] == 1):
                return True
            
    return False



def main():
    graphMatrix = []
    eulerCirList = []

    n = int(input("Enter number of elements in matrix: "))              #input collection for size and contents of graph matrix

    size = int(m.sqrt(n))

    for i in range(size):
        row = []
        strList = input(f"Enter elements of row {i} of matrix (space-separated): ").split(" ")
        row = [int(j) for j in strList]

        graphMatrix.append(row)


    eulerCirList = eulerCircuit(graphMatrix)


    for i in range(len(eulerCirList)):
        if(i == len(eulerCirList)-1):
            print(i)
        else:
            print(i, end=", ")


main()