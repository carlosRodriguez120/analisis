import math


""""

METODO  PUNTO FIJO
_________________________________________________________________________________________________________________________________________
"""


def raiz_cubica(numero):
    return numero**(1. / 3.)


def f(x):
    funcion = math.sqrt(((-2.5*x)-4.5)/(-0.5))
    return funcion


def funcionPuntoFijo(n):
    suma = 1
    lista = [0]
    tolerancia = 0.00001
    while tolerancia <= suma:
        resultado = f(n)
        lista.append(resultado)
        suma = abs(lista[-2])-abs(lista[-1])
        suma = abs(suma)
        n = resultado
        

    for n in lista:
        print(f"---[{n}]---")


"""
METODO DE BISECCION
____________________________________________________________________________________________________________________________________________
"""


def biseccion(a, b):

    tolerancia = 0.0001

    while tolerancia < fun(a):
        c = (a+b)/2
        if fun(a)*fun(c) < 0:
            b = c
        elif fun(a)*fun(c) > 0:
            a = c
        print(f"A: [{a}]- B:[{b}]- C:[{c}]")


"""
METODO GRAFICO
______________________________________________________________________________________________________________________________________
"""


def funcionGrafica():
    inicio = 5
    fin = 7
    suma = 0.000001
    lista = []
    while inicio <= fin:
        valor = fun(inicio)
        lista.append(valor)
        if fun(inicio)*fun(inicio+suma) < 0:
            print(F"EN {inicio} el valor fue de {fun(inicio)}")
        inicio += suma

    
    return lista


"""
________________________________________________________________________________________________________________________________________

"""


# _________________________________________________________________________________________________________________________________
# FUNCION PARA METODO GRAFICO Y METODO DE BISECCION

def fun(x):
    funcion = (-0.5*(x**2))+(2.5*x)+4.5
    return funcion
# __________________________________________________________________________________________________________________________________


print("\n METODO PUNTO FIJO")
print(funcionPuntoFijo(2))
print("\n METODO GRAFICO")
funcionGrafica()
print(" \n METODO BISECCION")
biseccion(0, 10)
