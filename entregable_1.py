# b. Objetivos:
# i. Crear la matriz de 𝑛×𝑛, donde n>4.
# ii. Generar obstáculos de 2x2 en posiciones aleatorias.
# iii. Colocar una manzana en una posición aleatoria de la matriz.
import random
import os

def start_game():
    while True:  
        n = int(input("\nIngrese un número mayor a 4 para el tamaño de la matriz: "))
        if n > 4:
            break
        else:
            print("\nPor favor, ingrese un número mayor a 4")

    while True:  
        max_obstaculos = (n // 2) * (n // 2)
        num_obstaculos = int(input(f"Ingrese el número de obstáculos (máximo {max_obstaculos}): "))
        if num_obstaculos <= max_obstaculos:
            break
        else:
            print(f"\nPor favor, ingrese un número de obstáculos no mayor a {max_obstaculos}.")

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
    snake = [(centro_fila, centro_columna + 2), (centro_fila, centro_columna + 1), (centro_fila, centro_columna)]
    for fila, columna in snake:
        matriz[fila][columna] = 'S'
    matriz[snake[0][0]][snake[0][1]] = 'H'

    def mover_serpiente(matriz, snake, direccion):
        head_fila, head_columna = snake[0]
        new_head = None

        if direccion == 'w' and head_fila > 0:
            new_head = (head_fila - 1, head_columna)
        elif direccion == 's' and head_fila < len(matriz) - 1:
            new_head = (head_fila + 1, head_columna)
        elif direccion == 'a' and head_columna > 0:
            new_head = (head_fila, head_columna - 1)
        elif direccion == 'd' and head_columna < len(matriz) - 1:
            new_head = (head_fila, head_columna + 1)
        
        if new_head and matriz[new_head[0]][new_head[1]] == '.':
            snake.insert(0, new_head)
            tail = snake.pop()
            matriz[head_fila][head_columna] = 'S'
            matriz[new_head[0]][new_head[1]] = 'H'
            matriz[tail[0]][tail[1]] = '.'
        return matriz, snake
    
    while True:
        
        os.system('cls' if os.name == 'nt' else 'clear')   
        
        for fila in matriz:
            print(" ".join(fila))
        direccion = input('\nIngrese el movimiento que desea indicarle a la serpiente (w, a, s, d)' 
                           '\nW es arriba, A es izquierda, S es abajo D es derecha... ')
       
        matriz, snake = mover_serpiente(matriz, snake, direccion)
    
        os.system('cls' if os.name == 'nt' else 'clear')
        
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
