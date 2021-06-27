arr = list(map(int, input().split()))
contestents = list(map(int, input().split()))
k = arr[1]


def rindex(lst, value):
    lst.reverse()
    i = lst.index(value)
    lst.reverse()
    return len(lst) - i - 1


def solve():
    if contestents[k-1] == 0:
        return 0
    else:
        return rindex(contestents, contestents[k-1]) + 1


print(solve())
