numero1 = int(input('Introduce el primer numero: '))
numero2 = int(input('Introduce el segundo numero: '))
def SumarMultiplicar(numero1, numero2):    
    return Sumar(numero1,numero2), Multiplicar(numero1,numero2)
def Sumar(suma1, suma2):
    return suma1 + suma2
def Multiplicar(multiplicando, multiplicador):    
    return multiplicando * multiplicador
print('el resultado de la suma es: ',Sumar(numero1,numero2))
print('el resultado de la multiplicacion es: ', Multiplicar(numero1,numero2))