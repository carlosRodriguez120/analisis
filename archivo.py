import math

# def f(x):
#     funcion=2*(x**2)+5*(x)-20
#     return funcion


# inicio =  2.15036
# fin = 2.15037
# suma = 0.000001

# lista = []
# while inicio<=fin:
#     valor = f(inicio)
#     lista.append(valor)
#     print(F"EN {inicio} el valor fue de {f(inicio)}")
#     inicio+=suma

# print(lista)



"""
definir la funcion 
luego se asigna un valor a la funcion
luego el resultado de esa funcion es la misma variable para correr dicha funcion 
la tolerancia : se debe sumar el valor actual de la funcion con el anterior 
si es menor a la tolerancia , se detiene
"""
# lista1=[1,2,3,4,4,5,5]
# print(lista1[-1])




def f(x):
    funcion=(20)/(2*x-5)
    return funcion

def funcion(n):
    suma = 1
    lista=[0]
    tolerancia = 0.0001
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
print(funcion(10))





    