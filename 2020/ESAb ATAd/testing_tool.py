#!/usr/local/bin/python3

import random
import sys

cc = 0

def randomOp(array):
    op = random.randint(1, 3)
    if op == 1:
        return array[::-1]
    if op == 2:
        array = array[::-1]
        for i in range(len(array)):
            if array[i] == 1:
                array[i] = 0
            else:
                array[i] = 1
        return array
    if op == 3:
        for i in range(len(array)):
            array[i] = 0 if array[i] == 1 else 1
        return array
    return array

def read_input(c, array):
    global cc
    cc += 1

    x = input()
    # raise Exception("Hello " + str(len(x) > 3))
    if len(x) > 3:
        y = [int(xx) for xx in list(x)]
        for i in range(len(array)):
            if array[i] != y[i]:
                print('N', flush=True)
                raise Exception((str(i)) + '\t' + (str(len(array))) + '\t' + (str(len(y))) + '\t' + ''.join([str(xx) for xx in array]) + '\t' + ''.join([str(xx) for xx in y]))
                sys.exit(0)
        print('Y', flush=True)
        return array, -1
        # raise Exception("")
    if c % 10 == 1:
        array = randomOp(array)

    i = int(x)
    return array, i

T = 100
B = 100

print(T, B, flush=True)

for _ in range(T):
    read_count = 0
    binary = [random.randint(0, 1) for _i in range(B)]
    # binary = list("1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
    # print(''.join(binary))
    while read_count < 150:
        read_count += 1
        binary, index = read_input(read_count, binary)
        if index == -1:
            break
        print(binary[index - 1], flush=True)