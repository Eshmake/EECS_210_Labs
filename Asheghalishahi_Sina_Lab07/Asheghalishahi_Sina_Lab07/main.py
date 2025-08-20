#main.py

# Name: Sina Asheghalishahi
# KUID: 3127403
# LAB Session: Wednesday 11 a.m.
# LAB Assignment: 07
# Description: Program takes in an integer "n" as input, and produces list of all 
# bit sequences of length "n" w/o a pair of consecutive 0s as output. 
# Collaborators: None


def printNonConsecSeq(n, seq):                  #recursive init. function defined, which makes 2 recursive calls,
    if(n <= 0):                                 #one for the 1st elements being 0, and the other for it being 1.
        return 0
    else:
        seq[0] = "0"
        _nonconsec(n, seq, 1)

        seq[0] = "1"
        _nonconsec(n, seq, 1)


def _nonconsec(n, seq, i):                      #recursive helper func. defined, which either prints the current seq. if
                                                #it is of length "n", or makes more recursive calls for the following index
    if(n == i):                                 #after setting the current one to an appropriate value.
        print("".join(seq), end=" ")
        return                                  #Note: output sequences printed with space separation.

    elif(seq[i-1] == "0"):
        seq[i] = "1"
        _nonconsec(n, seq, i+1)

    else:
        seq[i] = "0"
        _nonconsec(n, seq, i+1) 

        seq[i] = "1"
        _nonconsec(n, seq, i+1)


def main():     
    n = int(input("Enter a positive integer: "))            #input collection
    seq = ["0" for _ in range(n)]                   #sequence init.

    printNonConsecSeq(n, seq)
    print()

main()          #run main func.