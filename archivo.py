import math

def fun(x):
    funcion=math.pi*(x**2)*((9-x)/(3))-30
    return funcion




def funcionGrafica():
    inicio = 1
    fin = 10
    suma = 1
    lista = []
    while inicio<=fin:
        valor = fun(inicio)
        lista.append(valor)
        print(F"EN {inicio} el valor fue de {fun(inicio)}")
        inicio+=suma

  
    print(lista)
    return lista




"""
definir la funcion 
luego se asigna un valor a la funcion
luego el resultado de esa funcion es la misma variable para correr dicha funcion 
la tolerancia : se debe sumar el valor actual de la funcion con el anterior 
si es menor a la tolerancia , se detiene
"""
# lista1=[1,2,3,4,4,5,5]
# print(lista1[-1])

def raiz_cubica(numero):
    return numero**(1. / 3.)


def f(x):
    funcion=raiz_cubica((90-9*math.pi*x**2)/(-math.pi))
    return funcion



def funcionPuntoFijo(n):
    suma = 1
    lista=[0]
    tolerancia = 0.00001
    while tolerancia<=suma:
        resultado = f(n)
        lista.append(resultado)
        suma=abs(lista[-2])-abs(lista[-1])
        suma=abs(suma)
        n=resultado
        print(suma)
    
    for n in lista:
        print(f"---[{n}]---")

    return lista

print(funcionPuntoFijo(2.01))
#funcionGrafica()





    