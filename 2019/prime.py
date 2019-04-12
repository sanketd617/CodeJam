import math
import sys

mem = {}

def maxPrimeFactor(n):
    if n in mem:
        return mem[n]
    maxPrime = -1

    while n%2 == 0:
        maxPrime = 2
        n >>= 1

    for i in range(3, int(math.sqrt(n))+1, 2):
        while n%i == 0:
            maxPrime = i
            n = n/i

    if n > 2:
        maxPrime = n
    mem[n] = int(maxPrime)
    return int(maxPrime)

def isGood(seq):
    for s in seq:
        if s == -1:
            return False
    return True

if __name__ == "__main__":
    alphas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    T = int(input())
    for t in range(T):
        N, L = [int(x) for x in input().split(" ")]
        cipher = [int(x) for x in input().split(" ")]
        primes = []
        seq = [-1 for x in range(L+1)]
        factors = []

        for c in cipher:
            x = maxPrimeFactor(c)
            y = int(c/x)
            if x not in primes:
                primes.append(x)
            if y not in primes:
                primes.append(y)

        sPrimes = sorted(primes)
        index = 0
        mapping = {}
        for p in sPrimes:
            mapping[p] = alphas[index]
            index += 1
            
        for i in range(L-1):
            if cipher[i] == cipher[i+1]:
                continue
            x = maxPrimeFactor(cipher[i])
            y = int(cipher[i]/x)
            p = maxPrimeFactor(cipher[i+1])
            q = int(cipher[i+1]/p)

            if x == p or x == q:
                seq[i] = x
            else:
                seq[i] = y
        
        while not isGood(seq):
            for i in range(1, L):
                if seq[i] == -1 and seq[i+1] != -1 and int(cipher[i]/seq[i+1]) in mapping:
                    seq[i] = int(cipher[i]/seq[i+1])
                if seq[i] == -1 and seq[i-1] != -1 and int(cipher[i-1]/seq[i-1]) in mapping:
                    seq[i] = int(cipher[i]/seq[i-1])
            if seq[0] == -1 and seq[1] != -1 and int(cipher[0]/seq[1]) in mapping:
                seq[0] = int(cipher[0]/seq[1])
            if seq[L] == -1 and seq[L-1] != -1 and int(cipher[L-1]/seq[L-1]) in mapping:
                seq[L] = int(cipher[L-1]/seq[L-1])

        if int(cipher[0]/seq[0]) in mapping:
            seq = [int(cipher[0]/seq[0])] + seq
        
                        
        print("Case #"+str(t+1)+": "+("".join([str(mapping[x]) for x in seq[:-1]])))