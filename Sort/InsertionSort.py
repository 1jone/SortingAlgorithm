# encoding:utf-8

def InsertionSort(Ilist):
    count = len(Ilist)
    for i in range(1, count):
        key = i - 1
        mark = Ilist[i]
        while key >= 0 and Ilist[key] > mark:
            Ilist[key + 1] = Ilist[key]
            key -= 1
        Ilist[key + 1] = mark
    return Ilist


if __name__ == "__main__":
    Ilist = [1, 24, 43, 43, 2, 4, 5, 4, 5, 2]
    print(InsertionSort(Ilist))
