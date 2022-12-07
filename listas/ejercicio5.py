lista = [2,3,4,6,7,89,9,6,4,3,2,12,4,7] 
print(lista) 
for i in range(len(lista)) : 
    element = lista.pop() 
    lista.insert(0,element) 
    print(lista) 