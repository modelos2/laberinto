def abrir():
    return open('texto.txt', 'r')


def leer(archivo):
    return [x.split(' ') for x in archivo]


def poss(matriz):
    print(matriz)
    for i in range(len(matriz)):
        if 'x' in matriz[i]:
            print("si")
            return (i, matriz[i].index('x'))


print(poss(leer(abrir())))
