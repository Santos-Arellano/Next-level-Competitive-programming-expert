def sereja_and_dima(cards):
    # Inicializamos los punteros para los extremos izquierdo y derecho
    left, right = 0, len(cards) - 1
    
    # Inicializamos las puntuaciones de ambos jugadores
    sereja_score, dima_score = 0, 0
    
    # Usamos una variable para alternar el turno: True para Sereja, False para Dima
    turn = True
    
    # Continuamos mientras haya cartas
    while left <= right:
        if cards[left] > cards[right]:
            chosen_card = cards[left]
            left += 1
        else:
            chosen_card = cards[right]
            right -= 1
        
        if turn:
            sereja_score += chosen_card  # Es turno de Sereja
        else:
            dima_score += chosen_card  # Es turno de Dima
        
        turn = not turn  # Cambiamos el turno
    
    return sereja_score, dima_score

# Leer la entrada
n = int(input())  # Número de cartas
cards = list(map(int, input().split()))  # Valores de las cartas

# Obtener las puntuaciones finales
sereja_score, dima_score = sereja_and_dima(cards)

# Imprimir el resultado
print(sereja_score, dima_score)
