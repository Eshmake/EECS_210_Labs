#warshall.py

# Name: Sina Asheghalishahi
# KUID: 3127403
# LAB Session: Wednesday 11 a.m.
# LAB Assignment: 09
# Description: Program takes in a 0-1 matrix with relation "R" on a set of "n" elements
#              as input, and produces a matrix of transitive closure as output, by using
#              Warshall's Algorithm.
# Collaborators: None

import math as m 

def copyMatrix(matrix):                 #helper func. defined that simply returns a copy of a given matrix
    newMatrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(matrix[i][j])
        newMatrix.append(row)

    return newMatrix  


def warshall(relMatrix):                        #func. defined that returns transitive closure of given 0-1 matrix via Warshall's Algorithm (i.e. Algo. 9.4.2)
    W = copyMatrix(relMatrix)

    for k in range(len(W)):
        for i in range(len(W)):
            for j in range(len(W)):
                if(W[i][j] or (W[i][k] and W[k][j])):
                    W[i][j] = 1
                else:
                    W[i][j] = 0
    
    return W



def main():
    relMatrix = []
    warshallMatrix = []

    n = int(input("Enter number of elements in matrix: "))              #input collection for size and contents of relation matrix

    size = int(m.sqrt(n))

    for i in range(size):
        row = []
        strList = input(f"Enter elements of row {i} of matrix (space-separated): ").split(" ")
        row = [int(j) for j in strList]

        relMatrix.append(row)
    
    
    warshallMatrix = warshall(relMatrix)              #transitive closure obtained for given relation matrix via Warshall's Algo.


    print("Transitive Closure (via Warshall's Algorithm): ")                           #transitive closure matrix is printed in row-column format to terminal

    for i in range(len(warshallMatrix)):
        for j in range(len(warshallMatrix[0])):
            print(warshallMatrix[i][j], end=" ")
        print()


main()          #main func. called