def get_fibonacci():
    f0 = 0
    f1 = 1
    f2 = f0 + f1
    suma = 0
    while f2 < 4000000:
        f0 = f1
        f1 = f2
        f2 = f0 + f1
        if f2 % 2 == 0:
            suma = suma + f2
    print(f'la suma de los terminos pares es {suma}')
    print(f'el último termino menor a 4000000 es {f1}')


get_fibonacci()
