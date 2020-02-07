# encoding:utf-8

def BubbleSort(Blist):
    len_num = len(Blist)
    flag = True
    for i in range(len_num):
        for j in range(0, len_num-1-i):
            if Blist[j] > Blist[j+1]:
                Blist[j], Blist[j+1] = Blist[j+1], Blist[j]
                flag = False
        if flag:
            break
    return Blist

if __name__ == "__main__":
    d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
    d0_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]
    Blist = BubbleSort(d0)
    print(Blist)

