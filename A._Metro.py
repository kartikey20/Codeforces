import os
import sys
from io import BytesIO, IOBase


BUFSIZE = 8192


class FastIO(IOBase):
    newLines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = 'x' in file.mode or 'r' not in file.mode
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
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode('ascii'))
        self.readline = lambda: self.buffer.readline().decode('ascii')


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
def input(): return sys.stdin.readline().rstrip('\r\n')


n, s = map(int, input().split())
track1 = list(map(int, input().split()))
track2 = list(map(int, input().split()))


def solve(track1, track2, n, s):
    if track1[0] == 0:
        return 'NO'
    else:
        if track1[s - 1] == 1:
            return 'YES'
        else:
            for i in range(s - 1, n):
                if track1[i] == 1 and track2[i] == 1 and track2[s - 1] == 1:
                    return 'YES'
    return 'NO'


print(solve(track1, track2, n, s))
