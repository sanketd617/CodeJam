#!/usr/bin/python3

import sys


def done(op):
    for o in op:
        if o != 1:
            return False
    return True


def getBit(flag):
    if flag:
        return 1
    return 0


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())

    for t in range(T):
        N, B, F = [int(x) for x in sys.stdin.readline().strip().split(" ")]
        flags = [True for x in range(N - B)] + [False for x in range(B)]
        op = [0 for x in range(N - B)]

        while True:

            if done(op):
                result = ""
                for i in range(N):
                    if not flags[i]:
                        result += str(i) + " "
                print(result.strip())
                sys.stdout.flush()
                break

            with open("eheee", "a+") as f:
                f.write("ksjabd")

            ip = [getBit(x) for x in flags]
            opStr = "".join([str(x) for x in ip])
            print(opStr)
            sys.stdout.flush()

            jip = input()

            if jip == "1":
                break
            elif jip == "-1":
                sys.exit()
            else:

                op = [int(x) for x in jip]

                target = N - B
                count = 0
                i = 0
                j = 0
                while count < target:
                    if ip[i] == op[j]:
                        flags[i] = True
                        i += 1
                        j += 1
                        count += 1
                    else:
                        flags[i] = False
                        i += 1
    sys.exit()
