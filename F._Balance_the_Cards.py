# TODO: Implement deque
import itertools
import os
import sys
from io import BytesIO, IOBase
from typing import OrderedDict

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = 'x' in file.mode or 'r' not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

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
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode('ascii'))
        self.read = lambda: self.buffer.read().decode('ascii')
        self.readline = lambda: self.buffer.readline().decode('ascii')


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
def input(): return sys.stdin.readline().rstrip('\r\n')


n = int(input())
d = OrderedDict(map(int, input().split()) for _ in range(2 * n))

print(d)


def isValid(nums):
    while len(nums) > 0:
        l = len(nums)
        for i, v in enumerate(nums):
            if i > 0:
                if abs(v) == abs(nums[i - 1]):
                    if v < 0:
                        nums.pop(i)
                        nums.pop(i - 1)
        if len(nums) == l:
            return False
    return True


def solve(dic):
    for i in itertools.permutations(d.keys(), len(dic)):
        front = list(i)
        back = [dic[x] for x in i]
        if isValid(front[:]) == True and isValid(back[:]) == True:
            return ['YES', front, back]
    return ['NO']


ans = solve(d)
if len(ans) > 1:
    print(ans[0])
    res = "\n".join("{} {}".format(x, y) for x, y in zip(ans[1], ans[2]))
    print(res)

else:
    print(ans[0])
