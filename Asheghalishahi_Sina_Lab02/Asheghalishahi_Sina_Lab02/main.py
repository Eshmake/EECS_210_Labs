#Name: Sina Asheghalishahi
# KUID: 3127403
# LAB Session: Wednesday 11 a.m.
# LAB Assignment: 02
# Description: Program takes in list of mappings between 2 sets of letters and numbers in the form of pairs,
#and outputs whether given mapping is a function, and if so, whether it is one-to-one and onto.
# Collaborators: None


mapStr = input("Enter mapping pairs: ")     #collect mapping pairs as input (syntax: each value in a pair is separated by 
                                            #a comma, each pair of values is separated from adjacent pairs by parentheses,
                                            #and entire sequence contains no spaces --> e.g. "(0,A)(1,B)(2,C)").
mapList = []

isFunc = True                               #booleans declared
isOneToOne = True
isOnto = True

for elem in mapStr:                                                         #for-loop stores mapList with I/O values by parsing string
    if (elem != "(" and elem != ")" and elem != "," and elem != " "):           
        mapList.append(elem)


mapInputs = []      #Input and Output lists declared
mapOutputs = []

for i in range(len(mapList)):           #for-loop stores all values at even indices in mapInputs, and all values at odd indices in mapOutputs
    if (i%2==0):
        mapInputs.append(mapList[i])
    else:
        mapOutputs.append(mapList[i])


for i in mapInputs:             #nested for-loop checks for duplicates in mapInputs, and if one is found, isFunc is set to false and loop breaks
    countInput = 0              #(as each input can only be associated with a single output in a function).
    for j in mapInputs:
        if (i == j):
            countInput += 1

    if(countInput > 1):
        isFunc = False
        break


if(not isFunc):                     #Output whether mappins is a function or not (is so, then continue with checks)
    print("Not a function")

else:
    print("Function", end=", ")

    for i in mapOutputs:            #nested for-loop checks for duplicates in mapOutputs, and if one is found, isOnetoOne is set to false and loop breaks
        countOut = 0                #(since one-to-one function can only have each output value associated with a single input value).
        for j in mapOutputs:
            if (i == j):
                countOut += 1

        if(countOut > 1):
            isOneToOne = False
            break
    
    if(isOneToOne):                         #Outputs whether function is one-to-one
        print("one-to-one", end=", ")
    else:
        print("not one-to-one", end=", ")

    outList = ["A", "B", "C", "D", "E", "F", "G", "H"]          #Output list (i.e. possible range) is declared and initialized

    for out in outList:                         #for-loop checks whether all possible outputs have associations in function, and 
        if(out not in mapOutputs):              #if any are absent, then isOnto is set to false and loop breaks     
            isOnto = False
            break

    if(isOnto):             #Outputs whether function is onto
        print("onto")
    else:
        print("not onto")
    



    