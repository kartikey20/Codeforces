import os
import sys
from io import BytesIO, IOBase
from itertools import groupby

BUFSIZE = 8192


class FastIO(IOBase):
    newLines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.write = self.buffer.write if self.writable else None

    def readline(self):
        while self.newLines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newLines = b.count(b'\n') + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newLines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
def input(): return sys.stdin.readline().rstrip('\r\n')


_int = int
n = _int(input())
arr = []
for i in range(n):
    arr.append(_int(input()))
d = {}
for i, k in groupby(sorted(arr)):
    d.update({i: list(k)})
print(len(d.keys()))
