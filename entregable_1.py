# b. Objetivos:
# i. Crear la matriz de 𝑛×𝑛, donde n>4.
# ii. Generar obstáculos de 2x2 en posiciones aleatorias.
# iii. Colocar una manzana en una posición aleatoria de la matriz.

import random

def start_game():
    n = int(input("Ingrese un número mayor a 4 para el tamaño de la matriz: "))
    if n <= 4:
        print("Por favor, ingrese un número mayor a 4")
        return
    
    max_obstaculos = (n // 2) * (n // 2)
    num_obstaculos = int(input(f"Ingrese el número de obstáculos (máximo {max_obstaculos}): "))
    
    if num_obstaculos > max_obstaculos:
        print(f"Por favor, ingrese un número de obstáculos no mayor a {max_obstaculos}.")
        return
    
    matriz = [['.' for _ in range(n)] for _ in range(n)]

    for _ in range(num_obstaculos):
        while True:
            fila = random.randint(0, n - 2)
            columna = random.randint(0, n - 2)
            
            if matriz[fila][columna] == '.' and matriz[fila][columna + 1] == '.' and \
               matriz[fila + 1][columna] == '.' and matriz[fila + 1][columna + 1] == '.':
                matriz[fila][columna] = 'o'
                matriz[fila][columna + 1] = 'o'
                matriz[fila + 1][columna] = 'o'
                matriz[fila + 1][columna + 1] = 'o'
                break

        while True:
            fila = random.randint(0, n - 1)
            columna = random.randint(0, n - 1)
            
            if matriz[fila][columna] == '.':
                matriz[fila][columna] = 'A'
                break

    for fila in matriz:
        print(' '.join(fila))
start_game()
