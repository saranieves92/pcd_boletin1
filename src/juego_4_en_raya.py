import pytest

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


# Código principal para generar y mostrar el tablero
if __name__ == "__main__":
    mov_jugador_1 = {}
    mov_jugador_2 = {}
    movimientos_jugadores=[mov_jugador_1, mov_jugador_2]
    t= generar_tablero(4, movimientos_jugadores)
    print(t, len(t))

  
n=4

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

def jugada_ganadora(movimientos_jugador):
    """
    Método que permite determinar si los movimientos de un jugador le permite ganar una partida.

    Parámetros:
        * movimientos_jugador: dict con el conjunto de movimientos de un jugador
    """
    #Comprobamos si hay 3 fichas en una fila
    for fila in movimientos_jugador:
        movimientos_columna = movimientos_jugador[fila]
        if len(movimientos_columna)==4:
            return True
    return False

def test_no_ganador():
    movimientos_jugador={2:[2,3,4]}
    assert False == jugada_ganadora(movimientos_jugador)

def test_ganador():
    movimientos_jugador={2:[1,2,3,4]}
    assert True == jugada_ganadora(movimientos_jugador)