tablero = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

simboloDelJugador= 'X'
simboloDeLaComputadora = 'O'

def imprimirTablero(tablero):
    print('   |   |')
    print(' ' + tablero[0] + ' | ' + tablero[1] + ' | ' + tablero[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[3] + ' | ' + tablero[4] + ' | ' + tablero[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[6] + ' | ' + tablero[7] + ' | ' + tablero[8])
    print('   |   |')

def estaVacio(tablero, index):
    return tablero[index] == ' '

def estaLleno(tablero):
    return not any(estaVacio(tablero, i) for i in range(9))

def verificarGanador(tablero, simbolo):
    return (
        (tablero[0] == simbolo and tablero[1] == simbolo and tablero[2] == simbolo) or
        (tablero[3] == simbolo and tablero[4] == simbolo and tablero[5] == simbolo) or
        (tablero[6] == simbolo and tablero[7] == simbolo and tablero[8] == simbolo) or
        (tablero[0] == simbolo and tablero[3] == simbolo and tablero[6] == simbolo) or
        (tablero[1] == simbolo and tablero[4] == simbolo and tablero[7] == simbolo) or
        (tablero[2] == simbolo and tablero[5] == simbolo and tablero[8] == simbolo) or
        (tablero[0] == simbolo and tablero[4] == simbolo and tablero[8] == simbolo) or
        (tablero[2] == simbolo and tablero[4] == simbolo and tablero[6] == simbolo)
    )

def listaCasillasVacias(tablero):
    return [i for i in range(9) if estaVacio(tablero, i)]

def minimax(tablero, profundidad, JugadorQueMaximiza):
    if verificarGanador(tablero, simboloDeLaComputadora):
        return 10
    elif verificarGanador(tablero, simboloDelJugador):
        return -10
    elif estaLleno(tablero):
        return 0

    if JugadorQueMaximiza:
        mejorPuntaje = -float('inf')
        for index in listaCasillasVacias(tablero):
            tablero[index] = simboloDeLaComputadora
            puntaje = minimax(tablero, profundidad + 1, False)
            tablero[index] = ' '
            mejorPuntaje = max(mejorPuntaje, puntaje)
        return mejorPuntaje

    else:
        mejorPuntaje = float('inf')
        for index in listaCasillasVacias(tablero):
            tablero[index] = simboloDelJugador
            puntaje = minimax(tablero, profundidad + 1, True)
            tablero[index] = ' '
            mejorPuntaje = min(mejorPuntaje, puntaje)
        return mejorPuntaje

def movimientDeLaComputadora(tablero):
    mejorPuntaje = -float('inf')
    best_index = None
    for index in listaCasillasVacias(tablero):
        tablero[index] = simboloDeLaComputadora
        puntaje = minimax(tablero, 0, False)
        tablero[index] = ' '
        if puntaje > mejorPuntaje:
            mejorPuntaje = puntaje
            best_index = index
    tablero[best_index] = simboloDeLaComputadora

def movimientoDelJugador(tablero):
    while True:
        index = int(input('Ingrese un número del 1 al 9 para hacer su movimiento: ')) - 1
        if estaVacio(tablero, index):
            tablero[index] = simboloDelJugador
            break
        else:
            print('Esa casilla ya está ocupada. Por favor ingrese otro número.')

def ejecutarJuego():
    print('¡Bienvenido al juego del tres en raya!')
    imprimirTablero(tablero)

    while True:
        movimientDeLaComputadora(tablero)
        print('La computadora ha hecho su jugada:')
        imprimirTablero(tablero)
        if verificarGanador(tablero, simboloDeLaComputadora):
            print('¡La computadora ha ganado!')
            break
        elif estaLleno(tablero):
            print('¡El juego ha terminado en empate!')
            break

        movimientoDelJugador(tablero)
        print('Ha hecho su movimiento:')
        imprimirTablero(tablero)
        if verificarGanador(tablero, simboloDelJugador):
            print('¡Felicidades, ha ganado!')
            break

ejecutarJuego()

