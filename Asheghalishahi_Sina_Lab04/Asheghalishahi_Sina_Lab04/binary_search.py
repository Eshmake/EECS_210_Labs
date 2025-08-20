#Name: Sina Asheghalishahi
# KUID: 3127403
# LAB Session: Wednesday 11 a.m.
# LAB Assignment: 04
# Description: Program takes in ordered list of pos. integers and integer value "x" as input, 
# and produces location of "x" if it appears in list, and 0 otherwise via recursive binary
# search algorithm.
# Collaborators: None


def binarySearch(valList, i, j, x):         #binary search algo
    m = (i+j)//2                #position calc.

    if(valList[m] == x):                                #if-else block returns position of x if such is found, and otherwise either recursively repeats process on left side
        return m+1                                      #of m if x is less that acquired value and m is within right side of left boundary, or on right side of m if x is
    elif(x < valList[m] and i < m):                     #greater than acquired value and m is within left side of right boundary, or returns 0 if x is not found in list.
        return binarySearch(valList, i, m-1, x)
    elif(x > valList[m] and j > m):
        return binarySearch(valList, m+1, j, x)
    else:
        return 0


def main():                         
    inpStr = input("Enter ordered list of integers, and desired integer 'x': ")             # Note: for input, list of integers is provided in comma-separated format, followed by 
                                                                                            # desired x value after a space (e.g. 1,2,3,4 2).
    inpList = inpStr.split(" ")                         #input processing

    valList_str = inpList[0].split(",")
    valList_int = [int(i) for i in valList_str]                 

    intVal = int(inpList[1])                           


    valLoc = binarySearch(valList_int, 0, len(valList_int)-1, intVal)           #binary search applied

    print(valLoc)               #result outputted to terminal


main()