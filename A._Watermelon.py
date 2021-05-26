import sys

n = int(sys.stdin.readline())


def solve(n):
    if n <= 2:
        return 'NO'
    elif n % 2 == 0:
        return 'YES'
    else:
        return 'NO'


print(solve(n))
