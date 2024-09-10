def min_wait_time(a, b, c):
    t = 0
    while True:
        
        if b * (t + c) >= a * c:
            return t
        t += 1

a, b, c = map(int, input().split())

print(min_wait_time(a, b, c))
