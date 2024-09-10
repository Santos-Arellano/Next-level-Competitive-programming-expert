import sys

def love_math(y):
    low, high = 0, int(2 * (y ** 0.5)) + 1  # Un límite superior aproximado
    while low <= high:
        mid = (low + high) // 2
        sum_mid = mid * (mid + 1) // 2

        if sum_mid == y:
            return mid
        elif sum_mid < y:
            low = mid + 1
        else:
            high = mid - 1

    return "NAI"

# Lectura rápida de input y output
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])  # Número de casos de prueba
results = []

for i in range(1, T + 1):
    Y = int(data[i])
    result = love_math(Y)
    results.append(str(result))

sys.stdout.write("\\n".join(results) + "\\n")
