import os
import random
import time
import sys
import select

def encontrar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def start_game():
    try:
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

        puntos = 0
        direccion = obtener_direccion()

        while True:
            encontrar_terminal()
            mostrar_matriz(matriz)
            print(f"Puntos: {puntos}")
            
            matriz, snake, puntos = mover_serpiente(matriz, snake, direccion, puntos)
            time.sleep(0.5)  # Espera 0.5 segundos antes de mover la serpiente de nuevo

            if hay_input_disponible():
                nueva_direccion = obtener_direccion()
                if es_direccion_valida(direccion, nueva_direccion):
                    direccion = nueva_direccion

            guardar_puntos(puntos)
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")
        print("El juego terminará ahora.")

def hay_input_disponible():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def es_direccion_valida(direccion_actual, nueva_direccion):
    # Verifica que la nueva dirección no sea opuesta a la dirección actual
    direcciones_opuestas = {'w': 's', 's': 'w', 'a': 'd', 'd': 'a'}
    return nueva_direccion != direcciones_opuestas[direccion_actual]

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

def mover_serpiente(matriz, snake, direccion, puntos):
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

    if new_head:
        if matriz[new_head[0]][new_head[1]] == '.':
            # Mueve la serpiente
            snake.insert(0, new_head)
            tail = snake.pop()
            matriz[head_fila][head_columna] = 'S'
            matriz[new_head[0]][new_head[1]] = 'H'
            matriz[tail[0]][tail[1]] = '.'
        
        elif matriz[new_head[0]][new_head[1]] == 'A':
            # Come una manzana y crece
            snake.insert(0, new_head)
            matriz[head_fila][head_columna] = 'S'
            matriz[new_head[0]][new_head[1]] = 'H'
            colocar_manzana(matriz)
            puntos += 1
        
        elif new_head in snake:
            # Colisión con su propio cuerpo
            print("\nLa serpiente chocó consigo misma. ¡Juego terminado!")
            print(f"Puntos totales: {puntos}")
            return matriz, snake, puntos  # Usar return en lugar de exit()
        
        else:
            # Colisión con un obstáculo
            print("\nLa serpiente chocó con un obstáculo. ¡Juego terminado!")
            print(f"Puntos totales: {puntos}")
            return matriz, snake, puntos  # Usar return en lugar de exit()
        
        # Verifica si ha ganado el juego
        if verificar_victoria(matriz):
            print("\n¡Felicidades! Has ganado el juego.")
            print(f"Puntos totales: {puntos}")
            return matriz, snake, puntos  # Usar return en lugar de exit()

    return matriz, snake, puntos

def verificar_victoria(matriz):
    for fila in matriz:
        if '.' in fila:
            return False
    return True

def obtener_direccion():
    while True:
        direccion = input('\nIngrese el movimiento que desea indicarle a la serpiente (w, a, s, d): '
                            '\nW es arriba, A es izquierda, S es abajo, D es derecha... ')
        if direccion in ['w', 'a', 's', 'd']:
            return direccion
        else:
            print("Entrada inválida. Por favor, ingrese una dirección válida (w, a, s, d).")

def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join(fila))

def guardar_puntos(puntos):
    try:
        with open("puntos.txt", "w") as archivo:
            archivo.write(f"Puntos: {puntos}\n")
    except IOError:
        print("No se pudo guardar los puntos en el archivo.")

start_game()
