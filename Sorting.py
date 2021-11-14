# test file for demos

def sort(list):
    for x in range(len(list) - 1):
        if list[x+1] > list[x]:
            temp = list[x]
            list[x] = list[x+1]
            list[x+1] = list[x]
    return list