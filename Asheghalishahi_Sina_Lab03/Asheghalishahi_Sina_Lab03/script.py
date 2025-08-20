#Name: Sina Asheghalishahi
# KUID: 3127403
# LAB Session: Wednesday 11 a.m.
# LAB Assignment: 03
# Description: Program takes in positive integers b, n, and m as input, and calculates and outputs
#fast modular exponentiation based on binary expansion of exponent, in form of, "b^n (mod m)".
# Collaborators: None


def baseExpansion(val, base):       #function returns list containing base expansion of given int value
    q = val             #q is set to copy of call value

    bitList = []

    while(q != 0):          #while q is not 0, a is set equal to remainder of q/base, and q is set to floor div. of q/base
        a = q%base         
        q //= base

        bitList.append(a)       #each resultant bit value is store in list

    i = 0
    j = len(bitList)-1


    while(j > i):                   #since list contains bit sequence in reverse order, values of each corresponding
        temp = bitList[i]           #pair of indices in opp. sides of list are exchanged 
        bitList[i] = bitList[j]
        bitList[j] = temp

        i +=1
        j -= 1

    
    return bitList


def main():             #main func. contains modular exponentiation algo

    intStr = input("Enter pos. integers for b, n, and m, respectively: ")       #required ints collected as input string (Syntax: comma separated --> b,n,m)
                                                                                
    intList = intStr.split(",")     #input string converted to list

    b = int(intList[0])
    n = int(intList[1])
    m = int(intList[2])

    n_Seq = baseExpansion(n, 2)         #retrieves binary expansion of "n" int value

    x = 1
    power = b%m

    i = len(n_Seq)-1                    #modular exponentiation algorithm: from end to start of list (so as to traverse from LSB to MSB), if a bit
    while(i >= 0):                      #is equal to 1, set x equal to modulus between product of x and current power, and m. Then, set power equal
        if(n_Seq[i] == 1):              #to modulus between power squared and m
            x = (x*power) % m
        power = (power**2) % m
        i -= 1

    print(f"b^n (mod m) = {x}")         #output result of modular exponentiation


main()






