# encoding:utf-8

def SelectionSort(Slist):
    for i in range(len(Slist)-1):
        min_index = Slist[i:].index(min(Slist[i:]))
        Slist[i], Slist[min_index+i] = Slist[min_index+i], Slist[i]
    return Slist

if __name__ == "__main__":
    d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
    print(SelectionSort(d0))
