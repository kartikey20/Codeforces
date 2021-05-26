n = int(input())
arr = []
for i in range(n):
    arr.append("".join(input()))


def solve(strs):
    numProblem = 0
    for i in strs:
        count = 0
        for j in i:
            if '1' == j:
                count += 1
            if count == 2:
                numProblem += 1
                break
    return numProblem


print(solve(arr))
