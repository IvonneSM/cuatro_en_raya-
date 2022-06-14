from random import randint, shuffle #liberia de random.
from colorama import init,Fore #libreria de colorama le entrega color a las fichas.
from os import system #liberia para limpiar pantalla.
init()


def tablero(): #funcion tablero 
    tablero = [["-"]*8 for i in range(8)] #se crea el tablero con una matriz de 8x8.
    return tablero #retornando tablero

def mostrar_matriz(tablero):#funcion mostrar tablero con el parametro que representa la instancia del tablero.
    for i in range(8):#bucle for
        print("|",end="")
        for j in range(8):
            if tablero[i][j] == "x":
                ficha = Fore.BLUE+tablero[i][j]+Fore.RESET # se pinta la ficha de color azul
                print(ficha,end=" ")
            elif tablero[i][j] == "o":
                ficha = Fore.RED+tablero[i][j]+Fore.RESET # se pinta la ficha de color rojo
                print(ficha,end=" ")
            else:
                print(tablero[i][j],end=" ")
        print("|",end="")
        print()
    print("","--"*8) # es la base, sin el "" se ve chueco xd, por eso se agrega.
    print(" 1 2 3 4 5 6 7 8 ")

def verifica_diagonal_des(tablero,ficha,fila,col):
    contador = 0
    if col <= 4:
        for i in range(4):
            if tablero[fila+i][col+i] == ficha: # moviendome en escalera hacia abajo
                contador += 1
            elif tablero[fila+i][col+i] != ficha and contador != 4: # si 
                contador = 0
    if contador == 4:
        return True
    else:
        return False

def verifica_diagonal_asc(tablero,ficha, fila,col):
    contador = 0
    if col >= 3:
        for i in range(4):
            if tablero[fila+i][col-i] == ficha:# moviendome en escalere hacia arriba
                contador += 1
            elif tablero[fila+i][col-i] != ficha and contador != 4:
                contador = 0
    if contador == 4:
        return True
    else:
        return False

def verifica_horizontal(tablero,ficha,fila): #funcion que verifica las 4 fichas en horizontales.
    termino_columnas = len(tablero[0])
    contador = 0
    for columna in range(termino_columnas):
        if tablero[fila][columna] == ficha:
            contador += 1
        elif tablero[fila][columna] != ficha and contador != 4:
            contador = 0
    if contador == 4:
        return True
    else:
        return False

def verifica_vertical(tablero,ficha,col): #funcion que verifica 4 fichas en verticales.
    fin_col = len(tablero)
    contador = 0
    for fila in range(fin_col):
        if tablero[fila][col] == ficha:
            contador += 1
        elif tablero[fila][col] != ficha and contador != 4:
            contador = 0
    if contador == 4:
        return True
    else:
        return False

def validar_movimientos(tablero,ficha,fila,col): #funcion que verifica alguna jugada valida
    return verifica_horizontal(tablero,ficha,fila) or verifica_vertical(tablero,ficha,col) or \
        verfica_diagonal_asc(tablero,ficha,fila,col) or verfica_diagonal_des(tablero,ficha,fila,col)

def movimiento_ficha(t, col, fila, ficha): #funcion que coloca la ficha en el tablero segun indique cada jugador.
    if t[fila][col] == "-":
        t[fila][col] = ficha


def un_jugador(tablero):#funcion para jugar contra el computador (IA).
    jugador1 = input("Ingrese nombre Jugador 1: ") #input creado para permitir que los jugadores puedan acceder al juego con un nombre personalizado.
    if jugador1 == "":
        un_jugador(tablero)
    fichas_jg_1 = 32
    fichas_pc = 32
    filas_jugables = [-1]*8 
    c = len(tablero)
    jug1 = "x"
    pc = "o"
    jugadores = ["Pc",jugador1]
    ronda = 1
    turno = jugadores[ronda%2] # se va intercalando entreo 0 y 1, que son los indices de la lista "jugadores".
    while True: #bucle while de ejecucion del juego.
        mostrar_matriz(tablero)
        if turno == jugador1:
            print("Turno de {}\n".format(Fore.MAGENTA+turno+Fore.RESET))
            print("fichas restantes {}: {}".format(turno,fichas_jg_1))
            try:
                eleccion = int(input("Elija una columna: "))-1
            except ValueError:
                eleccion = -1
            if eleccion < c and eleccion >= 0:
                no_lleno = filas_jugables[eleccion] + 8 != -1 
                # cuando este lleno la suma entre las filas jugables y el largo de las filas es 0,
                #  si es mayor aun quedan espacios disponibles y si es menor ya se lleno.
            else:
                no_lleno = False

            if no_lleno and (eleccion <= c):
                movimiento_ficha(tablero,eleccion,filas_jugables[eleccion],jug1)
                if validar_movimientos(tablero,jug1,filas_jugables[eleccion],eleccion):#valida al menos uno de todos los movimientos posibles
                    print("{} ha ganado".format(turno))
                    mostrar_matriz(tablero)
                    break
                filas_jugables[eleccion] -= 1
                fichas_jg_1 -= 1
            else:
                print(Fore.RED+"movimiento invalido, elija una columna correcta"+Fore.RESET)
                turno = jugador1
                continue
            ronda += 1
        elif turno == "Pc":
            print("Turno de {}\n".format(Fore.GREEN+turno+Fore.RESET))
            print("fichas restantes {}: {}".format(turno,fichas_jg_1))
            eleccion = randint(0,7) # escoge un numero random entre 0 y 7
            if eleccion < c and eleccion >= 0:
                no_lleno = filas_jugables[eleccion] + 8 != -1
            else:
                no_lleno = False
            if no_lleno and (eleccion <= c):
                movimiento_ficha(tablero,eleccion,filas_jugables[eleccion],pc)
                if validar_movimientos(tablero,pc,filas_jugables[eleccion],eleccion):
                    print("El pc ha ganado")
                    mostrar_matriz(tablero)
                    break
                filas_jugables[eleccion] -= 1
                fichas_pc -= 1
            else:
                print(Fore.RED+"movimiento invalido, elija una columna correcta"+Fore.RESET)
                turno = jugador1
                continue
            ronda += 1
        turno = jugadores[ronda%2]
        if fichas_jg_1 < 0 or fichas_pc < 0:
            print("juego terminado, ya no quedan fichas")
            break
    


def dos_jugadores(tablero): #funcion jugador contra jugador
    jugador1 = input("Ingrese nombre Jugador 1: ") #input creado para permitir que los jugadores puedan acceder al juego con un nombre personalizado.
    while jugador1 == "": # control de que el nombre no sea vacio
        jugador1 = input("Ingrese nombre Jugador 1: ")
    jugador2 = input("Ingrese nombre Jugador 2: ")
    while jugador2 == "":
        jugador2 = input("Ingrese nombre Jugador 2: ")

    fichas_jg_1 = 32
    fichas_jg_2 = 32
    filas_jugables = [-1]*8 
    c = len(tablero)
    jug1 = "x"
    jug2 = "o"
    jugadores = [jugador1,jugador2]
    shuffle(jugadores) #se desordena la lista, para elegir un judagor que inicie el juego al azar.
    ronda = 1
    turno = jugadores[ronda%2] # se va intercalando entre 0 y 1, que son los indices de la lista "jugadores".
    while True: #bucle while de ejecucion del juego.
        mostrar_matriz(tablero)
        if turno == jugador1:
            print("Turno de {}\n".format(Fore.MAGENTA+turno+Fore.RESET))
            print("fichas restantes {}: {}".format(turno,fichas_jg_1))
            eleccion = int(input("Elija una columna: "))-1
            if eleccion < c and eleccion >= 0:
                no_lleno = filas_jugables[eleccion] + 8 != -1 
                # cuando este lleno la suma entre las filas jugables y el largo de las filas es 0,
                #  si es mayor aun quedan espacios disponibles y si es menor ya se lleno.
            else:
                no_lleno = False

            if no_lleno and (eleccion <= c):
                movimiento_ficha(tablero,eleccion,filas_jugables[eleccion],jug1)
                if validar_movimientos(tablero,jug1,filas_jugables[eleccion],eleccion):
                    print("{} ha ganado".format(turno))
                    mostrar_matriz(tablero)
                    break
                filas_jugables[eleccion] -= 1
                fichas_jg_1 -= 1
            else:
                print(Fore.RED+"movimiento invalido, elija una columna correcta"+Fore.RESET)
                turno = jugador1
                continue
            ronda += 1
        elif turno == jugador2:
            print("Turno de {}\n".format(Fore.MAGENTA+turno+Fore.RESET))
            print("fichas restantes {}: {}".format(turno,fichas_jg_2))
            eleccion = int(input("Elija una columna: "))-1
            if eleccion < c and eleccion >= 0:
                no_lleno = filas_jugables[eleccion] + 8 != -1 
                # cuando este lleno la suma entre las filas jugables y el largo de las filas es 0,
                #  si es mayor aun quedan espacios disponibles y si es menor ya se lleno.
            else:
                no_lleno = False

            if no_lleno and (eleccion <= c):
                movimiento_ficha(tablero,eleccion,filas_jugables[eleccion],jug2)
                if validar_movimientos(tablero,jug2,filas_jugables[eleccion],eleccion): 
                    print("{} ha ganado".format(turno))
                    mostrar_matriz(tablero)
                    break
                filas_jugables[eleccion] -= 1
                fichas_jg_2 -= 1
            else:
                print(Fore.RED+"movimiento invalido, elija una columna correcta"+Fore.RESET)
                turno = jugador2
                continue
            ronda += 1
        turno = jugadores[ronda%2]
        if fichas_jg_1 < 0 or fichas_jg_2 < 0:
            print("juego terminado, ya no quedan fichas")
            break


def iniciar_juego(op):#funcion que contiene el flujo del juego completo.
    copia_tablero = tablero()
    
    if op == "1":
        un_jugador(copia_tablero)
    else:
        dos_jugadores(copia_tablero)



def main(): #funcion principal
    #menu para que el juego sea mas dinamico 
    system("cls")
    menu = """ 
1) iniciar con 1 jugador
2) iniciar con 2 jugadores
3) intrucciones de juego
4) salir
"""
    print(menu) 
    op = input("seleccione una opcion: ")
    if op == "1" or op == "2":
        iniciar_juego(op)
        while True:
            continuar = input("Desea iniciar un nuevo juego(si=s - no=n): ").lower()
            if continuar == "s":
                main()
            else:
                break
    elif op == "3":
        print("""
*El juego contiene un flujo de uno a uno (1 turno por cada jugador), contando con 32 fichas cada jugador.
*Para el lanzanmiento de la ficha se debera escoger el numero de columna (1 al 8), en su respectivo turno.
*Para determinar al ganador las fichas del mismo color deben estar posicionadas consecutivamente en vertical, horizontal o diagonal.
*El juego consiste en bloquear a tu oponente para que no este no logre conectar (diagonal, vetical y horizontal) 4 de sus fichas.
*Al no lograr obtener un ganador el juego quedara en un empate. 
""")
    else:
        quit()
    main()



if __name__ == '__main__':
    print()
    print("                                             CUATRO EN RAYA             ")
    print()
    main()






