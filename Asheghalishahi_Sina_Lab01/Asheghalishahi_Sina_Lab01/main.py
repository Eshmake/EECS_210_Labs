#Name: Sina Asheghalishahi
# KUID: 3127403
# LAB Session: Wednesday 11 a.m.
# LAB Assignment: 01
# Description: Program collects 2 bit strings of length n from user, and applies 3
# logic functions to output the calculations of bitwise AND, OR, and XOR.
# Collaborators: None



string1 = input("Enter bit string 1: ")     #Input collection for 2 bit strings
string2 = input("Enter bit string 2: ")

seq_AND = []       #List declarations
seq_OR = []
seq_XOR = []


for i in range(len(string1)):           #For-loop converts each pair of corresponding bits in bit strings to ints,
    bit1 = int(string1[i])              #and appends the result of each logical function applied to them to the respective list.
    bit2 = int(string2[i])

    seq_AND.append(bit1 & bit2)
    seq_OR.append(bit1 | bit2)
    seq_XOR.append(bit1 ^ bit2)

res_AND = "".join(str(i) for i in seq_AND)      #For each list, elements are converted to type str, and then joined into bit strings.
res_OR = "".join(str(i) for i in seq_OR)
res_XOR = "".join(str(i) for i in seq_XOR)


print(f"AND Output: {res_AND}")            #Resultant strings are printed as output
print(f"OR Output: {res_OR}")
print(f"XOR Output: {res_XOR}")






