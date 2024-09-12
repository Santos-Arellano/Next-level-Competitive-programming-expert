def count_operations(x):
    count_2 = count_3 = count_5 = 0

    while x % 2 == 0:
        x //= 2
        count_2 += 1
    
    while x % 3 == 0:
        x //= 3
        count_3 += 1

    while x % 5 == 0:
        x //= 5
        count_5 += 1

    return (x, count_2, count_3, count_5)

def solve(a,b):
    a_factors = count_operations(a)
    b_factors = count_operations(b)

    if a_factors[0] != b_factors[0]:
        return -1
    
    operations = abs(a_factors[1] - b_factors[1]) + abs(a_factors[2] - b_factors[2]) + abs(a_factors[3] - b_factors[3])

    return operations

a,b = map(int, input().split())

print(solve(a,b))


    


