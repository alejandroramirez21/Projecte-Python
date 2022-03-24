import random
import os
import time


def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def tiro():
    dado = random.randrange(1, 6)
    return dado


def lista_mapa():
    lista = ["1", "2", "3", "4", "OCA", "PUENTE", "7", "8", "OCA", "10", "11", "PUENTE", "13", "OCA", "15", "16", "17",
             "OCA", "POSADA", "20", "21", "22", "OCA", "24", "25", "DADOS", "OCA", "28", "29", "30", "POZO", "OCA",
             "33",
             "34", "35", "OCA", "37", "38", "39", "40", "OCA", "LABERINTO", "43", "44", "OCA", "46", "47", "49", "OCA",
             "51", "52", "DADOS", "OCA", "55", "CARCEL", "57", "CALAVERA", "OCA", "60", "61", "62", "63"]
    return lista


def oca(posicion, turno):
    mod_oca = 0
    lista_tmp = lista_mapa()
    for i in lista_tmp:
        mod_oca += 1
        if i == "OCA":
            if mod_oca > posicion:
                posicion = mod_oca
                break
            else:
                continue
    print("Te ha tocado Oca..De oca a oca y tiro porque me toca")
    return posicion, turno


def puente(posicion, turno):
    if posicion == 6:
        posicion = 12
    elif posicion == 12:
        posicion = 6
    else:
        print("Ha habido un error")
        error = input("CUIDADO!!!")
    print("te ha tocado la puente---")
    print("Te ha tocado el puente..De puente a puente y tiro porque me lleva la corriente")
    return posicion, turno


def dados(turno):
    dado1, dado2 = tiro(), tiro()
    posc_final = (dado1 + dado2) + 3
    print("te ha tocado dados")
    print("Te ha tocado dados..De dados a dados y tiro porque son cuadrados")
    return posc_final, turno


def turno_jugador(posc_jugador, jugador, posc_maquina, turno, lista_tmp, dado):
    posada, pozo, carcel = "", "", ""

    if (posc_jugador + dado) > len(lista_tmp):
        turno = "maquina"
        print("te has pasado de valor, consigue el valor exacto")
        print("Te has pasado de valor, consigue el valor exacto")
        pass
    elif (posc_jugador + dado) == len(lista_tmp):
        posc_jugador += dado
        lista_tmp[posc_jugador - 1] = jugador.upper()
        lista_tmp[posc_maquina - 1] = "MAQUINA"
        print("%s te ha tocado el número %d" % (jugador, dado))
        print("%s Te ha tocado el número %d" % (jugador, dado))
        print("Este es el tablero")
        pass
    elif (posc_jugador + dado) < len(lista_tmp):
        posc_jugador += dado
        clear()
        print("%s te ha tocado el número %d" % (jugador, dado))
        print("%s Te ha tocado el número %d" % (jugador, dado))
        print("Este es el tablero")
        # Se comprueban las distintas casillas del jugador
        if lista_tmp[posc_jugador - 1] == "OCA":
            posc_jugador, turno = oca(posc_jugador, turno)
        elif lista_tmp[posc_jugador - 1] == "PUENTE":
            posc_jugador, turno = puente(posc_jugador, turno)
        elif lista_tmp[posc_jugador - 1] == "POSADA":
            posada = "jugador"
            turno = "maquina"
        elif lista_tmp[posc_jugador - 1] == "POZO":
            pozo = "jugador"
            turno = "maquina"
        elif lista_tmp[posc_jugador - 1] == "DADOS":
            posc_jugador, turno = dados(turno)
        elif lista_tmp[posc_jugador - 1] == "LABERINTO":
            posc_jugador = 31
            turno = "maquina"
        elif lista_tmp[posc_jugador - 1] == "CARCEL":
            carcel = "jugador"
            turno = "maquina"
        elif lista_tmp[posc_jugador - 1] == "CALAVERA":
            print("Te ha tocado la CALAVERA, vuelves a empezar")
            print("Te ha tocado la CALAVERA, vuelves a empezar desde la casilla de inicio")
            posc_jugador = 0
            turno = "maquina"
        else:
            turno = "maquina"
        # Aquí es donde se imprime el tablero
        if posc_jugador == posc_maquina:
            lista_tmp[posc_jugador - 1] = "MAQUINA + " + jugador.upper()
        elif posc_jugador != posc_maquina:
            lista_tmp[posc_jugador - 1] = jugador.upper()
            lista_tmp[posc_maquina - 1] = "MAQUINA"
        print(lista_tmp)
        # time.sleep(0.8)
        tmp = input("\n presiona la tecla enter: ")
    return posc_jugador, posc_maquina, turno, posada, pozo, carcel


def turno_maquina(posc_jugador, jugador, posc_maquina, turno, lista_tmp, dado):
    posada, pozo, carcel = "", "", ""

    if (posc_maquina + dado) > len(lista_tmp):
        turno = "jugador"
        print("la maquina se ha pasado de valor")
        print("La maquina se ha pasado de valor")
        pass
    elif (posc_maquina + dado) == len(lista_tmp):
        posc_maquina += dado
        lista_tmp[posc_jugador - 1] = jugador.upper()
        lista_tmp[posc_maquina - 1] = "MAQUINA"
        print("A la maquina le ha tocado el número %d" % (dado))
        print("Este es el tablero")
        pass
    elif (posc_maquina + dado) < len(lista_tmp):
        posc_maquina += dado
        clear()
        print("A la maquina le ha tocado el número %d" % (dado))
        print("Este es el tablero")
        # Se comprueban los distintos tipos de casilla para la maquina
        if lista_tmp[posc_maquina - 1] == "OCA":
            posc_maquina, turno = oca(posc_maquina, turno)
        elif lista_tmp[posc_maquina - 1] == "PUENTE":
            posc_maquina, turno = puente(posc_maquina, turno)
        elif lista_tmp[posc_maquina - 1] == "POSADA":
            posada = "maquina"
            turno = "jugador"
        elif lista_tmp[posc_maquina - 1] == "DADOS":
            posc_maquina, turno = dados(turno)
        elif lista_tmp[posc_maquina - 1] == "POZO":
            pozo = "maquina"
            turno = "jugador"
        elif lista_tmp[posc_maquina - 1] == "LABERINTO":
            posc_maquina = 31
            turno = "jugador"
        elif lista_tmp[posc_maquina - 1] == "CARCEL":
            carcel = "maquina"
            turno = "jugador"
        elif lista_tmp[posc_maquina - 1] == "CALAVERA":
            print("A la maquina le ha tocado la CALAVERA, vuelves a empezar")
            print("A la maquina le ha tocado la CALAVERA, vuelve a empezar desde la casilla de inicio")
            posc_maquina = 0
            turno = "jugador"
        else:
            turno = "jugador"
        # Imprimir tablero
        if posc_jugador == posc_maquina:
            lista_tmp[posc_jugador - 1] = "MAQUINA + " + jugador.upper()
        elif posc_jugador != posc_maquina:
            lista_tmp[posc_jugador - 1] = jugador.upper()
            lista_tmp[posc_maquina - 1] = "MAQUINA"
        print(lista_tmp)
        turno = "jugador"
        # çtime.sleep(0.8)
        # time.sleep(0.8)
        tmp = input("\n presiona la tecla enter: ")
    return posc_jugador, posc_maquina, turno, posada, pozo, carcel


def primer_turno(posc_jugador, dado, lista_tmp):
    clear()
    posc_jugador += dado
    print("%s te ha tocado el número %d" % (jugador, dado))
    print("%s Te ha tocado el número %d" % (jugador, dado))
    print("Este es el tablero")
    if lista_tmp[posc_jugador - 1] == "OCA":
        posc_jugador, turno = oca(posc_jugador, "jugador")
    else:
        turno = "maquina"
    #       time.sleep(0.8)
    lista_tmp[posc_jugador - 1] = jugador.upper()
    print(lista_tmp)
    tmp = input("\n presiona la tecla enter: ")
    return posc_jugador, turno


jugador = input("¿Como te llamas?: ")
posc_jugador, posc_maquina = 0, 0
maquina, turno, posada, pozo, carcel = "", "", "", "", ""
while True:
    lista_tmp = lista_mapa()
    dado = tiro()
    if turno == "jugador":
        # POSADA turno jugador
        if posada == "maquina":
            print("Has caido en la posada")
            for i in range(3):
                posc_jugador, posc_maquina, turno, posada, pozo, carcel = turno_jugador(posc_jugador, jugador, posc_maquina, turno, lista_tmp, dado)
            posada = ""
        # POZO turno jugador
        elif pozo == "maquina":
            print("Has caido en la pozo")
            for i in range(4):
                posc_jugador, posc_maquina, turno, posada, pozo, carcel = turno_jugador(posc_jugador, jugador, posc_maquina, turno, lista_tmp, dado)
            pozo = ""
        elif carcel == "maquina":
            print("Has caido en Carcel")
            for i in range(4):
                posc_jugador, posc_maquina, turno, posada, pozo, carcel = turno_jugador(posc_jugador, jugador, posc_maquina, turno, lista_tmp, dado)
        else:
            posc_jugador, posc_maquina, turno, posada, pozo, carcel = turno_jugador(posc_jugador, jugador, posc_maquina, turno, lista_tmp, dado)

    elif turno == "maquina":
        # POSADA turno maquina
        if posada == "jugador":
            print("Has caido en la posada")
            print("Has caido en la posada...pierdes 2 turnos")
            for i in range(3):
                posc_jugador, posc_maquina, turno, posada, pozo, carcel = turno_maquina(posc_jugador, jugador, posc_maquina, turno, lista_tmp, dado)
            posada = ""
        # POZO turno maquina
        elif pozo == "jugador":
            print("Has caido en la pozo")
            print("Has caido en la pozo...pierdes 3 turnos")
            for i in range(4):
                posc_jugador, posc_maquina, turno, posada, pozo, carcel = turno_maquina(posc_jugador, jugador, posc_maquina, turno, lista_tmp, dado)
            pozo = ""
        elif carcel == "jugador":
            print("Has caido en la Carcel")
            print("Has caido en la Carcel...pierdes 3 turnos")
            for i in range(4):
                posc_jugador, posc_maquina, turno, posada, pozo, carcel = turno_maquina(posc_jugador, jugador, posc_maquina, turno, lista_tmp, dado)
        else:
            posc_jugador, posc_maquina, turno, posada, pozo, carcel = turno_maquina(posc_jugador, jugador, posc_maquina, turno, lista_tmp, dado)
    else:
        posc_jugador, turno = primer_turno(posc_jugador, dado, lista_tmp)

    if posc_jugador == len(lista_mapa()):
        clear()
        print(lista_tmp)
        print("Has ganado---------")
        print("Has ganado ")
        break
    elif posc_maquina == len(lista_mapa()):
        clear()
        print(lista_tmp)
        print("Ha ganado la maquina---------")
        print("Ha ganado la maquina ")
        break
