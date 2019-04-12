
if __name__ == "__main__":
    T = int(input())

    for t in range(T):
        strN = input()
        N = int(strN)
        l = len(strN)
        N1 = N
        N2 = 0
        index = 0

        for n in strN:
            index += 1
            if int(n) == 4:
                x = 10 ** (l - index)
                N1 -= x
                N2 += x

        print("Case #"+str(t+1)+": "+str(N1)+" "+str(N2))