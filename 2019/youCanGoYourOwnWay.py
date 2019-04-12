
if __name__ == "__main__":
    T = int(input())

    for t in range(T):
        N = int(input())
        P = input()
        MP = ""
        for p in P:
            if p == "S":
                MP += "E"
            else:
                MP += "S"

        print("Case #"+str(t+1)+": "+MP)