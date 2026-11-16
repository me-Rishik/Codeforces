t = int(input())
count = 0
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    s = sum(a)
    if s==n:
        s -= 4
    elif any(a[j]+a[j+1]==-2 for j in range(n-1)):
        s += 4
    print(s)
