def max_operations(t, test_cases):
    results = []
    
    for i in range(t):
        n, s = test_cases[i]
        b_count = 0  # Contador para las 'B'
        operations = 0  # Contador de operaciones exitosas
        
        # Recorremos la cadena de izquierda a derecha (no al revés)
        for j in range(n):
            if s[j] == 'B':  # Cuando encontramos una 'B'
                b_count += 1
            elif s[j] == 'A' and b_count > 0:  # Si encontramos una 'A' y hay 'B' antes
                operations += 1  # Realizamos una operación
                b_count -= 1  # Reducimos el número de 'B' disponibles para intercambio
        
        results.append(operations)  # Almacenamos el resultado para este caso
    
    return results

# Lectura de entrada
t = int(input())  # Número de casos de prueba
test_cases = []

# Leer cada caso de prueba
for _ in range(t):
    n = int(input())  # Longitud de la cadena
    s = input().strip()  # Cadena de caracteres
    test_cases.append((n, s))

# Ejecutar la función y obtener los resultados
results = max_operations(t, test_cases)

# Imprimir los resultados
for result in results:
    print(result)
