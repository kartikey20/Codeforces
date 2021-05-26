def solve():
    rowPos = 0
    columnPos = 0
    arr = [[]] * 5
    for i in range(5):
        arr[i] = list(map(int, input().split()))
        if 1 in arr[i]:
            rowPos = abs(2 - i)
            columnPos = abs(2 - arr[i].index(1))
    return abs(rowPos + columnPos)


print(solve())
