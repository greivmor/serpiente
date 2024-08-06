import os
import random

def clear_terminal():
 
    if os.name == 'nt':
        os.system('cls')
    

def start_game():
    
    while True:
        try:
            n = int(input("\nIngrese un número mayor a 4 para el tamaño de la matriz: "))
            if n <= 4:
                print("\nPor favor, ingrese un número mayor a 4")
                continue
            break
        except ValueError:
            print("\nPor favor, ingrese un número entero válido.")

    max_obstaculos = (n // 2) * (n // 2)
    while True:
        try:
            num_obstaculos = int(input(f"Ingrese el número de obstáculos (máximo {max_obstaculos}): "))
            if num_obstaculos > max_obstaculos:
                print(f"\nPor favor, ingrese un número de obstáculos no mayor a {max_obstaculos}.")
                continue 
            break 
        except ValueError:
            print("\nPor favor, ingrese un número entero válido.")

    matriz = crear_matriz(n)
    
    generar_obstaculos(matriz, num_obstaculos)
   
    colocar_manzana(matriz)
    
    snake = inicializar_serpiente(matriz, n)

    
    while True:
        clear_terminal()
        mostrar_matriz(matriz)
        direccion = obtener_direccion()
        matriz, snake = mover_serpiente(matriz, snake, direccion)

def crear_matriz(n):
    
    return [['.' for _ in range(n)] for _ in range(n)]

def centro(n):
    
    centro_fila = n // 2
    centro_columna = n // 2
    return centro_fila, centro_columna

def generar_obstaculos(matriz, num_obstaculos):
    
    n = len(matriz)
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

def colocar_manzana(matriz):
    
    n = len(matriz)
    while True:
        fila = random.randint(0, n - 1)
        columna = random.randint(0, n - 1)

        if matriz[fila][columna] == '.':
            matriz[fila][columna] = 'A'
            break

def inicializar_serpiente(matriz, n):
    
    centro_fila, centro_columna = centro(n)
    snake = [(centro_fila, centro_columna + 2), (centro_fila, centro_columna + 1), (centro_fila, centro_columna)]
    for fila, columna in snake:
        matriz[fila][columna] = 'S'
        matriz[snake[0][0]][snake[0][1]] = 'H'
    return snake

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

def obtener_direccion():
    
    direccion = input('\nIngrese el movimiento que desea indicarle a la serpiente (w, a, s, d)' 
                           '\nW es arriba, A es izquierda, S es abajo D es derecha... ')
    return direccion

def mostrar_matriz(matriz):
    
    for fila in matriz:
        print(" ".join(fila))

start_game()
