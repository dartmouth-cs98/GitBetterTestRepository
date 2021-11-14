# test file for demos

def merge(list1, list2):
    newlist = []
    for i in range(len(list1)):
        newlist.append(list1[i])
    for i in range(len(list2)):
        newlist.append(list2[i])
    return newlist