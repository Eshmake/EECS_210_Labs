# Name: Sina Asheghalishahi
# KUID: 3127403
# LAB Session: Wednesday 11 a.m.
# LAB Assignment: 04
# Description: Program takes in 2 ordered lists of pos. integers, and
# produces merged ordered list w/o duplicates as output.
# search algorithm.
# Collaborators: None


def merge(list1, list2):        #merge func. declared
    merged_list = []

    while(len(list1) > 0 and len(list2) > 0):                                                                       # While 2 lists have elements, choose smaller of 1st elements of 2 lists and append it to output list if previous                                                         
        if(list1[0] < list2[0]):                                                                                    # element of output list is not a duplicate. Then, remove chosen element from respective input list, and check if 
            if(len(merged_list) == 0 or (len(merged_list) > 0 and list1[0] != merged_list[len(merged_list)-1])):    # the input list has been reduced to length zero. If so, append all elements of other input list to output list, 
                merged_list.append(list1[0])                                                                        # provided they do not have duplicates in the output list.

            list1.pop(0)
            if(len(list1) == 0):
                for i in range(len(list2)):
                    if(list2[i] == merged_list[len(merged_list)-1]):
                        continue
                    else:
                        merged_list.append(list2[i])

        else:
            if(len(merged_list) == 0 or (len(merged_list) > 0 and list2[0] != merged_list[len(merged_list)-1])):
                merged_list.append(list2[0])
            
            list2.pop(0)
            if(len(list2) == 0):
                for i in range(len(list1)):
                    if(list1[i] == merged_list[len(merged_list)-1]):
                        continue
                    else:
                        merged_list.append(list1[i])

    return merged_list              #return merged list as output



def main():
    lists = input("Enter lists: ").split()                  # Note: For input, separate lists with tab, and separate individual elements in each
                                                            # list with commas (see I/O image for example)
    list_1 = lists[0].split(",")
    list_1 = [int(i) for i in list_1]           #input processing


    list_2 = lists[1].split(",")
    list_2 = [int(i) for i in list_2]


    merged_list = merge(list_1, list_2)        #call "merge" func. with given input lists               

    merged_str = ",".join(str(i) for i in merged_list)

    print(merged_str)               #print output to terminal


main()      #run main func.
