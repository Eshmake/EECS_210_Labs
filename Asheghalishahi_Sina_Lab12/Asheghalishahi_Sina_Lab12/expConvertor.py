#expConvertor.py

# Name: Sina Asheghalishahi
# KUID: 3127403
# LAB Session: Wednesday 11 a.m.
# LAB Assignment: 12
# Description: Program takes in as input a prefix (Polish) equation, and produces the postfix
# (reverse-Polish) form as output.
# Collaborators: None


def expConvertor(prefixList):           #prefix-to-postfix function defined
    
    opers = ('+','-','*','/','^')           #tuple of operators

    postfixList = []                #list for postfix expression initialized

    for i in range(len(prefixList)-1, -1, -1):        #iterates through indices of prefixList in reverse order

        if(prefixList[i] not in opers):             #if current index contains an operand, append it to postfixList,
            postfixList.append(prefixList[i])       #otherwise if operator, then remove last 2 elements from postfixList
                                                    #(i.e. operands), combine them with the operator in postfix order, and
        else:                                       #then append the resulting expression to postfixList.
            oper1 = postfixList.pop()
            oper2 = postfixList.pop()

            combined = oper1 + oper2 + prefixList[i]

            postfixList.append(combined)

    return postfixList              #return postfixList


def main():
    prefixList = list(input("Enter prefix statement: "))          #input collection and processing for prefix expression

    postfixList = expConvertor(prefixList)          #call convertor function to obtain postfix version of expression

    print(postfixList[0])           #print postfix version (contained in first index of postfixList)


main()          #call main function


