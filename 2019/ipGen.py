from random import randint
import math
import sys

def getPrimes(n):
    result = [2]
    for num in range(3,n,2):
        if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
            result.append(num)
    return result

ip = open("input", "w")
ip.write(sys.argv[1]+"\n")
p = open("pangrams", "w")
    
for t in range(int(sys.argv[1])):
    N = randint(101, 10000)
    L = randint(26, 100)
    n = L

    
    blankPos = [i for i in range(L)]
    selectedAlphas = [-1 for i in range(L)]
    alphas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    indices = []
    for i in range(26):
        idx = randint(0, len(blankPos)-1)
        indices.append(blankPos[idx])
        selectedAlphas[blankPos[idx]] = alphas[i]
        blankPos = blankPos[:idx] + blankPos[idx+1:]
    
    while len(blankPos) != 0:
        idx = randint(0, len(blankPos)-1)
        indices.append(blankPos[idx])
        selectedAlphas[blankPos[idx]] = alphas[randint(0, 25)]
        blankPos = blankPos[:idx] + blankPos[idx+1:]
    
    primes = getPrimes(N)
    selectedPrimes = []
    for i in range(26):
        idx = randint(0, len(primes)-1)
        selectedPrimes.append(primes[idx])
        primes = primes[:idx] + primes[idx+1:]
    
    mapping = {}
    sortedPrimes = sorted(selectedPrimes)
    for i in range(26):
        mapping[alphas[i]] = sortedPrimes[i]
    
    pangram = "".join([str(x) for x in selectedAlphas])
    code = []
    
    for i in range(len(pangram)-1):
        code.append(mapping[pangram[i]]*mapping[pangram[i+1]])
            
    cipher = " ".join([str(x) for x in code])

    p.write("Case #"+str(t+1)+": "+pangram+"\n")
    
    ip.write(str(N)+" "+str(len(code))+"\n")
    ip.write(cipher+"\n")

p.close()
ip.close()