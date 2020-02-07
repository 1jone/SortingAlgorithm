def MergeSort(Mlist):
    if len(Mlist) <= 1:
        return Mlist

    center = len(Mlist) // 2
    Llist = MergeSort(Mlist[:center])
    Rlist = MergeSort(Mlist[center:])
    return merge(Llist, Rlist)


def merge(Llist, Rlist):
    res = []
    i = j = 0
    while i < len(Llist) and j < len(Rlist):
        if Llist[i] < Rlist[j]:
            res.append(Llist[i])
            i += 1
        else:
            res.append(Rlist[j])
            j += 1
    res += Llist[i:] + Rlist[j:]
    return res


if __name__ == "__main__":
    Mlist = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
    print(MergeSort(Mlist))
