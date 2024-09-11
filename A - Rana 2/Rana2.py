def min_cost(N, K, heights):
    # Tabla de DP para almacenar el costo mínimo para llegar a cada piedra
    dp = [float('inf')] * N
    dp[0] = 0  # El costo de estar en la primera piedra es 0

    # Iteramos sobre cada piedra
    for i in range(1, N):
        # Revisamos todas las piedras a las que podemos saltar desde 'i-K' hasta 'i-1'
        for j in range(max(0, i - K), i):
            dp[i] = min(dp[i], dp[j] + abs(heights[i] - heights[j]))

    # El valor en dp[N-1] es el costo mínimo para llegar a la última piedra
    return dp[N-1]

# Leer la entrada
N, K = map(int, input().split())
heights = list(map(int, input().split()))

# Llamar a la función para calcular el costo mínimo
print(min_cost(N, K, heights))
