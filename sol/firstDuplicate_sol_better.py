# Find the first duplicate in list of numbers (ls)
# the numbers are between 1 and n, where n is the length or list
# if the list not valid or there is no duplicate, it will return -1

def firstDuplicate(ls):
    n = len(ls)
    if n < 2 :
        return -1

    seen = list()
    for i in ls:
        if i > n :
            return -1
        if i in seen:
            return i
        seen.append(i)

    return -1

