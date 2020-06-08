# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 12:08:15 2020

@author: Edwin
"""
import numpy as np 
def leer ():
    return [x.split(' ') for x in open('laberinto.txt','r')]
def arreglada():
    #.replace('\n','')
    # se genera la matriz ya en forma matricial quedando para manejar de la siguiente manera matriz[i][j]
    return [[x.replace('\n','') for x in y] for y in leer()]
def posi(matriz):
    # se busca la posision en j donde se encuentre la x y se concatena la matriz para despues buscar la posision en i
    return [x.index("X") for x in matriz if "X" in x]+matriz
def posij(mat):
    # dado la posision en j y la matriz, se obtiene la posision en i de x,
    # y ya solo retorna el punto (i,j) donde esta la x
    return  [[x[mat[0]] for x in mat[1:]].index("X"),mat[0]]

#-------------------------- matriz[fila][columna] | fila= i , columna = j 
def der(matriz,pos):
    # se genera la nueva matriz con el x movido a la derecha, retornando la matriz modificada
    return [['0' if i==pos[0] and j== pos[1]  else 'X' if i== pos[0] and j== pos[1]+1 else matriz[i][j]  for j in range(len(matriz[i])) ]  for i in range(len(matriz)) ]
def down(matriz,pos):
    # se genera la nueva matriz con el x movido para abajo, retornando la matriz modificada 
    return [['0' if i==pos[0] and j== pos[1]  else 'X' if i== pos[0]+1 and j== pos[1] else matriz[i][j]  for j in range(len(matriz[i])) ]  for i in range(len(matriz)) ]

def izq(matriz,pos):
    # se genera la nueva matriz con el x movido a la izquierda, retornando la matriz modificada
    return [['0' if i==pos[0] and j== pos[1]  else 'X' if i== pos[0] and j== pos[1]-1 else matriz[i][j]  for j in range(len(matriz[i])) ]  for i in range(len(matriz)) ]

# rotar la matriz 180 grados
def rotard(matriz):
    return np.rot90(np.rot90(np.rot90(matriz))).tolist()

# rotar matriz hacia la izquierda
def rotari(matriz):
    return np.rot90(matriz).tolist()

# primero lo ubicamos a la pared mas cercana izquierda 
def ubicar(matriz,pos):
    
    if matriz[pos[0]][pos[1]-1]=='0':
        return ubicar(izq(matriz,pos),posij(posi(izq(matriz,pos))))
    else:
        print (np.array(matriz),pos ,'\n______________________________________________')
        return mover(rotari(matriz),posij(posi(rotari(matriz))))
    
# Se pretende siempre segir pegado a una pared que se ubique por debajo de la x y se valla moviendo hacia la derecha
# siempre y cuando este libre, y cuando abajo este libre se organize para que siga por esa misma pared, solo que del
# borde del costado de la pared y asi se valla arrastrando por toda la pared y a la derecha hasta hallar la y

def mover(matriz,pos):
    
    print(np.array(matriz),pos ,'\n______________________________________________')
    
    # ------------ si derecha libre y sobre piso "abajo ocupado", avanza a derecha 
    if matriz[pos[0]][pos[1]+1]=='0' and matriz[pos[0]+1][pos[1]]=='1' :
        return mover(der(matriz,pos), posij(posi(der(matriz,pos))))
    
    #------------si la izquierda esta libre y abajo libre, baja y gira la matriz hacia la izquierda para vorver 
    # a la pared que pasa a ser "piso" y seegir con la busqueda hacia la derecha
    elif matriz[pos[0]][pos[1]-1]=='0' and matriz[pos[0]+1][pos[1]]=='0':
        print ('no mas piso,baja y se gira'+'\n______________________________________________')
        return mover(rotari(down(matriz,pos)),posij(posi(rotari(down(matriz,pos)))))
    
    #------------si la derecha esta ocupada y sobre piso "abajo ocupado", gira para que la pared derecha
    # pase a ser el piso y continue con la busqueda a la derecha
    elif  matriz[pos[0]][pos[1]+1]=='1' and matriz[pos[0]+1][pos[1]]=='1' :
        print ('no mas derecha,se gira'+'\n______________________________________________')
        return mover( rotard(matriz), posij(posi( rotard(matriz))) )

    else:
        # ya sea porque o la pared o el pizo sea la y, indica que ya llego hasta el lado de la y,
        # y por ende acabo su busqueda
        print("Acabo"+'\n______________________________________________')
        return np.array(matriz)
     
print(ubicar(arreglada() , posij(  posi(  arreglada() ) )))
    