#permutation.py

# Name: Sina Asheghalishahi
# KUID: 3127403
# LAB Session: Wednesday 11 a.m.
# LAB Assignment: 06
# Description: Program takes in number with "n" unique digits and produces next permutation
#              in lexicographic order as output.
# Collaborators: None


def next_permutation(curr_perm):                        #func. produces next permutation from given permutation value
    curr_perm_str = str(curr_perm)                      #convert int input to int list
    curr_perm_list = [] 

    for i in curr_perm_str:
        curr_perm_list.append(int(i))


    j = len(curr_perm_list)-2                               #code implementation of Algorithm 6.6.1

    while(curr_perm_list[j] > curr_perm_list[j+1]):
        j-=1
    
    k = len(curr_perm_list)-1

    while(curr_perm_list[j] > curr_perm_list[k]):
        k-=1

    temp = curr_perm_list[j]
    curr_perm_list[j] = curr_perm_list[k]
    curr_perm_list[k] = temp

    r = len(curr_perm_list)-1
    s = j+1

    while(r>s):
        temp = curr_perm_list[r]
        curr_perm_list[r] = curr_perm_list[s]
        curr_perm_list[s] = temp
        
        r-=1
        s+=1

    return int("".join(str(i) for i in curr_perm_list))             #int list converted to int again, and returned as output

    

def main():
    num = int(input("Enter number with unique digits: "))       #input collection

    next_perm = next_permutation(num)           #run "next_perm" func.

    print(f"Next permutation: {next_perm}")     #print next perm. to terminal


main()     #run main method