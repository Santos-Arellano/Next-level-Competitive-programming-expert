# Función que calcula el costo mínimo
def min_cost(N, h):
    # Inicializar dp con valores grandes para poder minimizarlos luego
    dp = [float('inf')] * N
    dp[0] = 0  # El costo para estar en la primera piedra es cero
    
    # Costo para la segunda piedra
    if N > 1:
        dp[1] = abs(h[1] - h[0])
    
    # Aplicar la recurrencia
    for i in range(2, N):
        dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]), dp[i-2] + abs(h[i] - h[i-2]))
    
    # El resultado final es el costo mínimo para llegar a la última piedra
    return dp[N-1]

# Entrada
N = int(input())  # Número de piedras
h = list(map(int, input().split()))  # Alturas de las piedras

# Llamar a la función y mostrar el resultado
print(min_cost(N, h))
