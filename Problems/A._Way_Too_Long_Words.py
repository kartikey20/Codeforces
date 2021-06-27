n = int(input())
arr = [""] * n
for i in range(n):
    s = input()
    if len(s) > 10:
        arr[i] = f"{s[0]}{len(s) -2}{s[-1]}"
    else:
        arr[i] = s
for j in arr:
    print(j)
