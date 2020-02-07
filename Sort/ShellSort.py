def ShellSort(Slist):
    count = len(Slist)
    step = count // 2
    while step >= 1:
        for i in range(step, count):
            while i >= step and Slist[i] < Slist[i - step]:
                Slist[i], Slist[i - step] = Slist[i - step], Slist[i]
                i -= step
        step = step // 2
    return Slist


if __name__ == "__main__":
    Slist = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
    print(ShellSort(Slist))
