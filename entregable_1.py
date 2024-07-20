# b. Objetivos:
# i. Crear la matriz de 𝑛×𝑛, donde n>4.
# ii. Generar obstáculos de 2x2 en posiciones aleatorias.
# iii. Colocar una manzana en una posición aleatoria de la matriz.

import random

def start_game():
    n = int(input("\nIngrese un número mayor a 4 para el tamaño de la matriz: "))
    if n <= 4:
        print("\nPor favor, ingrese un número mayor a 4")
        return
    
    max_obstaculos = (n // 2) * (n // 2)
    num_obstaculos = int(input(f"Ingrese el número de obstáculos (máximo {max_obstaculos}): "))
    
    if num_obstaculos > max_obstaculos:
        print(f"\nPor favor, ingrese un número de obstáculos no mayor a {max_obstaculos}.")
        return

    matriz = [['.' for _ in range(n)] for _ in range(n)]
    
    def centro(n):
      centro_fila = n // 2
      centro_columna = n // 2
      return centro_fila, centro_columna

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
    
    centro_fila, centro_columna = centro(n)
    matriz[centro_fila][centro_columna] = 'H'
    matriz[centro_fila][centro_columna - 1] = 'S'
    matriz[centro_fila][centro_columna - 2] = 'S'

    def mover_serpiente(matriz, direccion):
        centro_fila, centro_columna = centro(n)
        head_fila = centro_fila
        head_columna = centro_columna + 2
     
        tail_fila = centro_fila
        tail_columna = centro_columna - 2

    
        for i in range(2, -1, -1):
            if direccion == 'arriba':
                if centro_fila - i > 0 and matriz[centro_fila - i][centro_columna] == '.':
                    matriz[centro_fila - i][centro_columna] = 'S'
                    if i == 2:
                        matriz[tail_fila][tail_columna] = '.'
            elif direccion == 'abajo':
                if centro_fila + i < n - 1 and matriz[centro_fila + i][centro_columna] == '.':
                    matriz[centro_fila + i][centro_columna] = 'S'
                if i == 2:
                    matriz[tail_fila][tail_columna] = '.'
            elif direccion == 'izquierda':
                if centro_columna - i > 0 and matriz[centro_fila][centro_columna - i] == '.':
                    matriz[centro_fila][centro_columna - i] = 'S'
                if i == 2:
                    matriz[tail_fila][tail_columna] = '.'
            elif direccion == 'derecha':
                if centro_columna + i < n - 1 and matriz[centro_fila][centro_columna + i] == '.':
                    matriz[centro_fila][centro_columna + i] = 'S'
                if i == 2:
                    matriz[tail_fila][tail_columna] = '.'

    
        if direccion == 'arriba':
            if centro_fila > 0 and matriz[centro_fila - 1][centro_columna] == '.':
                matriz[centro_fila - 1][centro_columna] = 'H'
            matriz[centro_fila][centro_columna] = 'S'
        elif direccion == 'abajo':
            if centro_fila < n - 1 and matriz[centro_fila + 1][centro_columna] == '.':
                matriz[centro_fila + 1][centro_columna] = 'H'
            matriz[centro_fila][centro_columna] = 'S'
        elif direccion == 'izquierda':
            if centro_columna > 0 and matriz[centro_fila][centro_columna - 1] == '.':
                matriz[centro_fila][centro_columna - 1] = 'H'
            matriz[centro_fila][centro_columna] = 'S'
        elif direccion == 'derecha':
            if centro_columna < n - 1 and matriz[centro_fila][centro_columna + 1] == '.':
                matriz[centro_fila][centro_columna + 1] = 'H'
            matriz[centro_fila][centro_columna] = 'S'

        return matriz

    while True:
        for fila in matriz:
            print(" ".join(fila))
        direccion = input('\nIngrese el movimiento que desea indicarle a la serpiente (arriba, abajo, izquierda, derecha)... ')
       
        matriz = mover_serpiente(matriz,direccion)
    
        for fila in matriz:
            print(' '.join(fila))
        
        while True:
            continuar = input("\n¿Desea continuar jugando? (s/n): ")
            if continuar.lower() == 's':
                break
            elif continuar.lower() == 'n':
                print("\nGracias por jugar!")
                return
            else:
                print("Por favor, ingrese 's' para continuar o 'n' para salir.")
            
start_game()
