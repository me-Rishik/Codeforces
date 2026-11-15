t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    if n % 2 == 1 or n < 2:
        print(count)
    elif n == 2:
        count = 1
        print(count)
    else:
        count = (n // 4) + 1
        print(count)