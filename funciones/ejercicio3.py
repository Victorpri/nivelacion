def SumarMultiplicar(*numeros):    
    suma = 0    
    multiplicacion = 1    
    for i in numeros:        
        suma =+ i        
        multiplicacion *= i    
    return suma,multiplicacion
print('el resultado es: ',SumarMultiplicar(1,34,5,7,8,7,5,3,12,1,3,45,6,6))
