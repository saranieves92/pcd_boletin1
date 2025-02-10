import pytest
import os

fichas= ['o','x']

def generar_tablero(n, movimientos_jugadores):
    tablero=[]
    for i in range(n):
        fila=['_' for i in range(n)]
        for j in range(n):
            casilla_vacia = True
            for k in range(len(movimientos_jugadores)):
                movimientos_jugador= movimientos_jugadores[k]

                if i in movimientos_jugador:
                    if j in movimientos_jugador[i]:
                        fila[j]=fichas[k]
        tablero.append(fila)
    return tablero

"""
Método que comprueba que un movimiento de un jugador es válido
* x: fila donde el jugador quiere colocar la ficha.
* y: columna donde el jugador quiere colocar su ficha.
* movimientos_otro_jugador: listado con las celdas ocupadas por el otro jugador.
"""
def movimiento_valido(x, y, movimientos_otro_jugador):
    if x > n or y > n:
        return False
    if x in movimientos_otro_jugador:
        movimientos_en_columna= movimientos_otro_jugador[x]
        if y in movimientos_en_columna:
            return False
    return True

def jugada_ganadora(movimientos_jugador):
    """
    Método que permite determinar si los movimientos de un jugador le permite ganar una partida.

    Parámetros:
        * movimientos_jugador: dict con el conjunto de movimientos de un jugador
    """
    #Comprobamos si hay 3 fichas en una fila
    for fila in movimientos_jugador:
        movimientos_columna = movimientos_jugador[fila]
        if len(movimientos_columna)==3:
            return True
    return False

def mostrar_tablero(tablero):
    """
        Método que muestra el estado actual del tablero
        Parámetros:
            * tablero: dict con el tablero a mostrar
    """
    for fila in tablero:
        for celda in fila:
            print(celda,end='')
        print('\n')

    
#Pedimos el tamaño del tablero en que se va a realizar el juego
n=int(input('Introduce el tamaño del tablero cuadrado:'))
casillas_libres = n*n
jugador_activo = 0
movimientos_jugador_1 = {}
movimientos_jugador_2 = {}
movimientos_jugadores = [movimientos_jugador_1, movimientos_jugador_2]
    
tablero= generar_tablero(n,movimientos_jugadores)
mostrar_tablero(tablero)
while casillas_libres > 0:
    casilla_jugador = input(f"JUGADOR {jugador_activo+1}: Introduce movimiento (x,y): ")
    casilla_jugador= casilla_jugador.strip()
    x= int(casilla_jugador.split(',')[0])-1
    y= int(casilla_jugador.split(',')[1])-1

    print(casilla_jugador,x,y)
    movimientos_jugador_activo= movimientos_jugadores[jugador_activo]
    movimientos_otro_jugador = movimientos_jugadores[(jugador_activo+1)%2]
    if movimiento_valido(x,y, movimientos_otro_jugador):
        mov_col= movimientos_jugador_activo.get(x,[])
        mov_col.append(y)
        movimientos_jugador_activo[x]= mov_col
        clear = lambda: os.system('cls')
        clear()
        tablero= generar_tablero(n,movimientos_jugadores)
        mostrar_tablero(tablero)
        if jugada_ganadora(movimientos_jugador_activo):
            print(F"ENHORABUENA EL JUGADOR {jugador_activo+1} HA GANADO")
            break
    else:
        frequency = 2000 # Set Frequency To 2500 Hertz
        duration = 1000 # Set Duration To 1000 ms == 1 second
        print('\a')
        print("Movimiento invalido. Turno para el siguiente jugador")

    casillas_libres= casillas_libres -1
    jugador_activo = (jugador_activo+1) % 2

#mov_jugador_1 = {}
#mov_jugador_2 = {}
#n=3
#movimientos_jugadores=[mov_jugador_1, mov_jugador_2]
#t= generar_tablero(n, movimientos_jugadores)
#print(t, len(t))

  
def test_generar_tablero():
    mov_jugador_1 = {}
    mov_jugador_2 = {}
    movimientos_jugadores=[mov_jugador_1, mov_jugador_2]
    t= generar_tablero(n, movimientos_jugadores)
    assert len(t)== n
    for f in t:
        assert len(f) == n

def test_movimiento_columna_fuera_tablero():
    movimientos_otro_jugador={}
    x= 1
    y= n+1
    assert False == movimiento_valido(x,y,movimientos_otro_jugador)

def test_movimiento_fila_y_columna_fuera_tablero():
    movimientos_otro_jugador={}
    x= n+1
    y= n+1
    assert False == movimiento_valido(x,y,movimientos_otro_jugador)

def test_movimiento_incorrecto():
    movimientos_otro_jugador={2:[3]}
    x= 2
    y= 3
    assert False == movimiento_valido(x,y,movimientos_otro_jugador)

def test_no_ganador():
    movimientos_jugador={2:[2,3]}
    assert False == jugada_ganadora(movimientos_jugador)

def test_ganador():
    movimientos_jugador={2:[1,2,3]}
    assert True == jugada_ganadora(movimientos_jugador)