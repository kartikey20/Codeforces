# TODO: Implement deque
import os
import sys
from io import BytesIO, IOBase
import collections

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.write = self.buffer.write if self.writable else None

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b'\n') + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.write = lambda s: self.buffer.write(s.encode('ascii'))
        self.readline = lambda: self.buffer.readline().decode('ascii')


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
def input(): return sys.stdin.readline().rstrip('\r\n')


dic = collections.OrderedDict()
n = int(input())

for i in range(n):
    dic[i] = list(map(int, input().split()))


def solve(animals):
    initialOrder = list(animals.keys())
    countWin = 0
    index = 0
    while countWin < 3:
        iterator = iter(dic)
        firstKey = next(iterator)
        secondKey = next(iterator)
        if animals[firstKey][countWin] < animals[secondKey][0]:
            animals.move_to_end(firstKey, last=True)
            countWin = 1
        elif animals[firstKey][countWin] > animals[secondKey][0]:
            animals.move_to_end(secondKey, last=True)
            countWin += 1
        index += 1
        if initialOrder == list(animals.keys()):
            return [-1, -1]
    return [next(iter(animals)), index]


print(*solve(dic))
