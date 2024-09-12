def pair_programming(k, n, m, a, b):
    result = []
    current_lines = k
    i, j = 0, 0
    possible = True

    for _ in range(n + m):
        if i >= n:
            result.append(b[j])
            j += 1
        elif j >= m:
            result.append(a[i])
            i += 1
        elif a[i] == 0:
            result.append(a[i])
            i += 1
        elif b[j] == 0:
            result.append(b[j])
            j += 1
        elif a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
        
        if result[-1] == 0:
            current_lines += 1
        
        if result[-1] > current_lines:
            possible = False
            break

    if possible:
        return result
    else:
        return -1

t = int(input().strip())

for _ in range(t):
    input() 
    k, n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = pair_programming(k, n, m, a, b)

    if result == -1:
        print(-1)
    else:
        print(" ".join(map(str, result)))
