def QuickSort(Qlist):
    return quick(Qlist, 0, len(Qlist) - 1)


def quick(Qlist, start, end):
    if start < end:
        left = start
        right = end
        key = Qlist[start]
    else:
        return Qlist
    while left < right:
        while left < right and Qlist[right] >= key:
            right -= 1
        if left < right:
            Qlist[left] = Qlist[right]
            left += 1
        while left < right and Qlist[left] < key:
            left += 1
        if left < right:
            Qlist[right] = Qlist[left]
            right -= 1
    Qlist[left] = key
    quick(Qlist, start, left - 1)
    quick(Qlist, left + 1, end)
    return Qlist


if __name__ == "__main__":
    Qlist = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
    print(QuickSort(Qlist))
