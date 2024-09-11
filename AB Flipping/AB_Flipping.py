def max_operations(t, test_cases):
    results = []
    
    # Iterar sobre cada caso de prueba
    for i in range(t):
        n, s = test_cases[i]
        count = 0
        j = 0
        
        # Recorrer el string buscando pares 'AB'
        while j < n - 1:
            if s[j] == 'A' and s[j+1] == 'B':
                count += 1
                j += 2  # Saltar después de realizar el swap
            else:
                j += 1  # Avanzar al siguiente par
        
        results.append(count)
    
    return results

# Leer el número de casos de prueba
t = int(input())
test_cases = []

# Leer los datos de cada caso de prueba
for _ in range(t):
    n = int(input())
    s = input().strip()
    test_cases.append((n, s))

# Obtener los resultados
results = max_operations(t, test_cases)

# Imprimir los resultados
for result in results:
    print(result)
