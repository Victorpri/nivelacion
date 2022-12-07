numero = int(input('Escoja un numero entero: '))
def paroImpar(num):
    if num%2 == 0:
        return 'El número es par'
    else:        
        return 'El número es impar'
print(paroImpar(numero))