import math

# Definir la función
def f(x, A, B, C):
    return A * x + B * math.sin(x) - C

# Implementación del método de bisección
def find_root(A, B, C, low, high, epsilon=1e-7):
    while high - low > epsilon:
        mid = (low + high) / 2
        if f(mid, A, B, C) * f(low, A, B, C) <= 0:
            high = mid
        else:
            low = mid
    return (low + high) / 2

# Leer el número de casos de prueba
T = int(input().strip())

for _ in range(T):
    A, B, C = map(int, input().split())

    # Verificar si A es mayor que B y C no es mayor a A para evitar división por cero
    if A == 0:
        print("No solution possible")
        continue

    # Iniciar la búsqueda de la raíz entre [0, C/A] o un valor más alto
    try:
        result = find_root(A, B, C, 0, C / A + 10)  # Aumentamos el rango para mayor precisión
        print(f"{result:.6f}")
    except Exception as e:
        print(f"Error: {e}")
