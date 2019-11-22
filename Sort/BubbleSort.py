# encoding:utf-8

def BubbleSort(Blist):
    while True:
        status=0
        for i in range(len(Blist)-1):
            if Blist[i]>Blist[i+1]:
                Blist[i], Blist[i+1] = Blist[i+1], Blist[i]
                status = 1
        if not status:
            break
    return Blist

if __name__ == "__main__":
    d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
    d0_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]
    Blist = BubbleSort(d0)
    print(Blist)

