def mininum_wait_time(a,b,c):
    t = 0
    while (a - b) * (c + t) > b * t:
        t += 1
    return t 

a, b, c = map(int, input().split())

print(mininum_wait_time(a,b,c))
