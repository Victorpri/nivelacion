lista=[2,4,5,7,8,9,9,0,3]

for i in range(len(lista)): 
    cambio = lista.pop()
    lista.insert(0,cambio)
    print(lista) 
