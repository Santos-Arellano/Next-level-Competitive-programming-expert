# Función que calcula el máximo de felicidad
def max_happiness(N, activities):
    # Inicializamos una tabla dp de tamaño N x 3
    dp = [[0] * 3 for _ in range(N)]
    
    # Condición inicial: el primer día, podemos hacer cualquier actividad
    dp[0][0] = activities[0][0]  # Felicidad si hace A el día 1
    dp[0][1] = activities[0][1]  # Felicidad si hace B el día 1
    dp[0][2] = activities[0][2]  # Felicidad si hace C el día 1
    
    # Llenamos la tabla dp para los días siguientes
    for i in range(1, N):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + activities[i][0]  # Si hace A el día i
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + activities[i][1]  # Si hace B el día i
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + activities[i][2]  # Si hace C el día i
    
    # El resultado final es el máximo valor en el último día
    return max(dp[N-1][0], dp[N-1][1], dp[N-1][2])

# Entrada
N = int(input())  # Número de días
activities = [list(map(int, input().split())) for _ in range(N)]

# Imprimimos el resultado de la función
print(max_happiness(N, activities))
