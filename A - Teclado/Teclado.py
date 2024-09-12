def find_working_buttons(s):
    n = len(s)
    working_buttons = set()

    i = 0

    while i < n:
        char = s[i]

        if i == n - 1 or s[i] != s[i + 1]:
            working_buttons.add(char)
            i += 1
        else:
            i += 2
    
    return ''.join(sorted(working_buttons))

t = int(input())

for _ in range(t):
    s = input().strip()
    print(find_working_buttons(s))