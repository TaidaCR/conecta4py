def crea_tablero(fila,columna):
    salida=[]
    for i in range(columna):
        lista2=[]
        for j in range(fila):
            lista2.append(0)
        salida.append(lista2)
    return salida

tablero=crea_tablero(6,7)
#crea 2 jugadores, a los que se asigna ficha

#ir jugando por turnos
#input columna
#jugar en la columna, jugador activo

def juega(matriz, jugador):
#"""ver si la columna tiene busca hueco
#si lo tiene en es hueco poner la ficha"""""
    for lista in matriz:
        ll=len(lista-1)   
        if lista[-1]==0:
            lista[-1]=='X'

        else:

    
    

def busca_hueco(columna):

    "buscar la ultima posicion vacia de la columna"



tablero=[
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]