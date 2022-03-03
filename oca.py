import random
import os
import time

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def tiro():
    dado = random.randrange(1, 6)
    dado = str(dado)
    return dado

def lista_mapa():
    lista = ["1", "2", "3", "4", "OCA", "PUENTE", "7", "8", "OCA", "10", "11", "PUENTE", "13", "OCA", "15", "16", "17",
         "OCA", "POSADA", "20", "21", "22", "OCA", "24", "25", "DADOS", "OCA", "28", "29", "30", "POZO", "OCA", "33",
         "34", "35", "OCA", "37", "38", "39", "40", "OCA", "LABERINTO", "43", "44", "OCA", "46", "47", "49", "OCA",
         "51", "52", "DADOS", "OCA", "55", "CARCEL", "57", "CALAVERA", "OCA", "60", "61", "62", "63"]
    return lista
jugador = input("Â¿Como te llamas?: ")
maquina = ""

patata = 0
posc_jugador = 0
posc_maquina = 0
turno = ""


while True:
    lista_tmp = lista_mapa()
    dado = tiro()
    dado = int(dado)

    if turno == "jugador":
        posc_jugador += dado
        if posc_jugador > len(lista_mapa()):
            pass
        elif posc_jugador <= len(lista_mapa()):
            clear()
            print("%s te ha tocado el nÃºmero %d" % (jugador, dado))
            print("Este es el tablero")
            if posc_jugador == posc_maquina:
                lista_tmp[posc_jugador-1] = "MAQUINA + " + jugador
            elif posc_jugador != posc_maquina:
                    lista_tmp[posc_jugador-1] = jugador.upper()
                    lista_tmp[posc_maquina-1] = "MAQUINA"
            print(lista_tmp)
            turno = "maquina"
            time.sleep(0.8)
        
    elif turno == "maquina":
        posc_maquina += dado
        if posc_maquina > len(lista_mapa()):
            pass
        elif posc_maquina <= len(lista_mapa()):
            clear()
            print("A la maquina le ha tocado el nÃºmero %d" %(dado))
            print("Este es el tablero")
            if posc_jugador == posc_maquina:
                lista_tmp[posc_jugador-1] = "MAQUINA + " + jugador
            elif posc_jugador != posc_maquina:
                    lista_tmp[posc_jugador-1] = jugador.upper()
                    lista_tmp[posc_maquina-1] = "MAQUINA"
            print(lista_tmp)
            turno = "jugador"
            time.sleep(0.8)
    else:
        clear()
        posc_jugador += dado
        print("%s te ha tocado el nÃºmero %d" % (jugador, dado))
        print("Este es el tablero")
        lista_tmp[dado-1] = jugador.upper()
        print(lista_tmp)
        turno = "maquina"
        time.sleep(0.8)
    
    if posc_jugador >= len(lista_mapa()):
        clear()
        print(lista_tmp)
        print("Has ganado---------")
        break
    elif posc_maquina >= len(lista_mapa()):
        clear()
        print(lista_tmp)
        print("Ha ganado la maquina---------")
        break


