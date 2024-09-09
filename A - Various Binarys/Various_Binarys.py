
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return 0

n = int(input())
arr = list(map(int, input().split()))
q = int(input())
queries = [int(input()) for _ in range(q)]

for query in queries:
    print(binary_search(arr, query))
