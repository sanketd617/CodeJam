def solve(n, matrix):
    trace = 0

    for i in range(n):
        trace += matrix[i][i]

    r = 0
    c = 0

    for i in range(n):
        r_sorted = sorted(matrix[i])
        for j in range(n-1):
            if r_sorted[j] == r_sorted[j+1]:
                r += 1
                break

    for j in range(n):
        col = []
        for i in range(n):
            col.append(matrix[i][j])
        c_sorted = sorted(col)
        for i in range(n-1):
            if c_sorted[i] == c_sorted[i+1]:
                c += 1
                break

    return trace, r, c

T = int(input())
outputs = []

for t in range(T):
    n = int(input())
    matrix = []
    for i in range(n):
        row = [int(e) for e in input().strip().split(' ')]
        matrix.append(row)

    k, r, c = solve(n, matrix)
    outputs.append('Case #{}: {} {} {}'.format(t+1, k, r, c))

print('\n'.join(outputs))