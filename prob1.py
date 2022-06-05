def suma(limite):
    suma = 0
    for i in range(1, limite):
        suma = i + suma
    return suma

print(suma(5))


def suma_pares(limite):
    suma = 0
    for i in range(1, limite):
        if i % 2 == 0:
            suma = i + suma
    return suma

print(suma_pares(5))

def suma_multi3y5(limite):
    suma = 0
    multip = [3.5]
    for i in range(limite):
        if i % 3 == 0 or  i % 5 == 0:
            suma = i + suma
    return suma

print(suma_multi3y5(1000))
