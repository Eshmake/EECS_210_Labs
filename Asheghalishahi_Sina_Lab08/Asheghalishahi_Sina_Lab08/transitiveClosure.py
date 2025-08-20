#transitiveClosure.py

# Name: Sina Asheghalishahi
# KUID: 3127403
# LAB Session: Wednesday 11 a.m.
# LAB Assignment: 08
# Description: Program takes in a 0-1 matrix with relation "R" on a set of "n" elements
#              as input, and produces a matrix of transitive closure as output.
# Collaborators: None

import math as m

def transitiveClosure(relMatrix):           #trans. closure func. defined with Algorithm 9.4.1
    A = copyMatrix(relMatrix)       
    B = copyMatrix(A)

    n = len(relMatrix)

    for i in range(2, n+1):             
        A = booleanProduct(A, relMatrix)
        B = OrMatrix(B, A)
    
    return B                #transitive closure matrix returned


def booleanProduct(matrix1, matrix2):           #func. defined that returns a copy of the boolean product of 2 given matrices
    newMatrix = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    k = len(matrix2)

    for i in range(len(matrix1)):               #nested for-loop sets each corresponding index of output matrix to 1 if result of c_ij formula is 1, and 0 otherwise.
        for j in range(len(matrix2[0])):
            c = []
            for n in range(k):
                if(matrix1[i][n] and matrix2[n][j]):
                    c.append(1)
                else:
                    c.append(0)

            newMatrix[i][j] = 1 if 1 in c else 0
    
    return newMatrix        #output matrix (boolean product) returned



def OrMatrix(matrix1, matrix2):             #func. defined that retunrs a copy of the logical OR of 2 given matrices
    newMatrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):            
            if(matrix1[i][j] or matrix2[i][j]):
                row.append(1)
            else:
                row.append(0)
        newMatrix.append(row)

    return newMatrix                    #output matrix returned

def copyMatrix(matrix):                 #helper func. defined that simply returns a copy of a given matrix
    newMatrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(matrix[i][j])
        newMatrix.append(row)

    return newMatrix            #copy of given matrix returned as output


def main():             #main func. defined
    
    relMatrix = []
    transClosMatrix = []

    n = int(input("Enter number of elements in matrix: "))              #input collection for size and contents of relation matrix

    size = int(m.sqrt(n))

    for i in range(size):
        row = []
        strList = input(f"Enter elements of row {i} of matrix (space-separated): ").split(" ")
        row = [int(j) for j in strList]

        relMatrix.append(row)
    
    
    transClosMatrix = transitiveClosure(relMatrix)              #transitive closure obtained for given relation matrix


    print("Transitive Closure: ")                           #transitive closure matrix is printed in row-column format to terminal

    for i in range(len(transClosMatrix)):
        for j in range(len(transClosMatrix[0])):
            print(transClosMatrix[i][j], end=" ")
        print()



main()          #main func. is run