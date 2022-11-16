from os import read
import re
import numpy as np 

def read_vects():
    f = open('vectores.txt')
    vectors = f.readlines()
    f.close()
    return vectors

def create_array_vects(vectores):
    vectors_list = [
            [int(unit) for unit in vector.split(',')] 
            for vector in vectores]
    return vectors_list

def GramSchmidt(V):
    tam = V.shape
    m = tam[0]
    n = tam[1]
    U = np.zeros((m,n))
    U[0]=V[0]

    for k in range(1,m):
        U[k]=V[k]
        for j in range(k):
            U[k]=U[k]-(np.dot(V[k],U[j]))/(np.dot(U[j],U[j]))*U[j]
    filas = len(U)
    print('Base Ortogonalizada: \n',U)

    print('Base Ortonormalizada: ')

    for i in range(filas):
        complete = U[i]/np.linalg.norm(U[i])
        print(complete)


if __name__ == '__main__':
    vectores = read_vects()
    V = np.array(create_array_vects(vectores))
    print('Vectores Iniciales: \n',V)
    GramSchmidt(V)
