
class Item:
    def __init__(self, nL, nU, val):
        self.nL = nL
        self.nU = nU
        self.val = val
        self.sum = 0


def val(x):
    if x == '@':
        return 1
    return 0

def leftCount(i, j, mem_ip, v):
    if j == 0:
        return v
    return mem_ip[i][j-1].nL + v

def upCount(i, j, mem_ip, v):
    if i == 0:
        return v
    return mem_ip[i-1][j].nU + v

def calc_sum(r1, c1, r2, c2, mem_ip):
    r = r2
    c = c2
    sum = 0

    while r > r1 and c > c1:
        sum += mem_ip[r][c].nL + mem_ip[r][c].nU - mem_ip[r][c].val
        r -= 1
        c -= 1

    if r1 < 0 and c1 < 0:
        return [sum, sum]
    if r1 >= 0 and c1 < 0:
        return [sum, sum - mem_ip[r1][c2].sum]
    if r1 < 0 and c1 >= 0:
        return [sum, sum - mem_ip[r2][c1].sum]

    tempSum = sum

    while c != c1:
        sum += mem_ip[r][c].nU
        c -= 1

    while r != r1:
        sum += mem_ip[r][c].nL
        r -= 1

    sum += mem_ip[r][c].sum
    # print(mem_ip[r][c].sum)
    sum -= mem_ip[r2][c1].sum
    # print(mem_ip[r2][c1].sum)
    sum -= mem_ip[r1][c2].sum
    # print( mem_ip[r1][c2].sum)
    sum += mem_ip[r1][c1].sum
    # print(mem_ip[r1][c1].sum)
    return [tempSum, sum]


def solve(R, C, H, V):
    ac_ip = []
    mem_ip = []
    mem_c = [0 for x in range(C)]
    mem_r = [0 for x in range(R)]
    num_cc = 0
    cuts_h = []
    cuts_v = []
    share = 0
    for i in range(R):
        ip_str = input()
        ac_ip.append([])
        mem_ip.append([])
        for j in range(C):
            c = ip_str[j]
            ac_ip[i].append(c)
            v = val(c)
            l = leftCount(i, j, mem_ip, v)
            u = upCount(i, j, mem_ip, v)
            mem_ip[i].append(Item(l, u, v))
            if v == 1:
                num_cc += 1
                mem_c[j] += 1
                mem_r[i] += 1

    share = int((num_cc)/((H+1)*(V+1)))

    # print("total : "+str(num_cc))
    # print("share : "+str(share))

    if num_cc == 0:
        return True

    if num_cc % ((H+1)*(V+1)) != 0:
        return False

    sum_r = 0
    num_cuts = 0
    per_cut_h = int(num_cc/(H+1))
    for i in range(R-1):
        sum_r += mem_r[i]
        if sum_r % per_cut_h == 0 and mem_r[i] != 0:
            cuts_h.append(i)
            num_cuts += 1

    if num_cuts != H:
        # print("Horizontal cuts: "+str(num_cuts)+" != "+str(H))
        return False

    sum_c = 0
    num_cuts = 0
    per_cut_v = int(num_cc/(V+1))
    for j in range(C-1):
        sum_c += mem_c[j]
        if sum_c % per_cut_v == 0 and mem_c[j] != 0:
            cuts_v.append(j)
            num_cuts += 1
            # print(num_cuts, sum_c)

    if num_cuts != V:
        # print("Vertical cuts: "+str(num_cuts)+" != "+str(V))
        return False

    for i in range(H):
        for j in range(V):
            r1 = c1 = r2 = c2 = -1
            r2 = cuts_h[i]
            c2 = cuts_v[j]
            if i > 0:
                r1 = cuts_h[i-1]
            if j > 0:
                c1 = cuts_v[j-1]

            # print(r1, c1, r2, c2)

            sum = calc_sum(r1, c1, r2, c2, mem_ip)
            mem_ip[r2][c2].sum = sum[0]

            # print("sum("+str(r1)+", "+str(c1)+", "+str(r2)+", "+str(c2)+") = "+str(sum))
            if sum[1] != share:
                return False

    return True

def printCase(n, result):
    print("Case #"+str(n)+": "+result)

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        R, C, H, V = [int(x) for x in input().split(" ")]
        result = solve(R, C, H, V)

        if result:
            printCase(t+1, "POSSIBLE")
        else:
            printCase(t+1, "IMPOSSIBLE")
