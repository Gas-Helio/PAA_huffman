import sys

def criaMatriz(qtdLinhas, qtdColunas):
    mat = []
    for i in range(qtdLinhas):
        aux = []
        for j in range(qtdColunas):
            aux.append(0)
        mat.append(aux)
    return mat

def preencheMatriz(qtdLinhas, qtdColunas, listaPesos):
    mat = criaMatriz(qtdLinhas, qtdColunas)
    for i in range(1, qtdLinhas):
        for j in range(1, qtdColunas):
            if(listaPesos[i][0] <= j):
                #O peso cabe na mochila
                var = j - listaPesos[i][0] #peso
                mat[i][j] = mat[i][j] + mat[i-1][var] + listaPesos[i][1] #valor
            else:
                #Caso o peso não caiba na mochila
                mat[i][j] = mat[i-1][j]

    return mat

def printMatriz(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            sys.stdout.write('[' + str(mat[i][j]) + ']')
        print()

def pegarPesosResultantes(mat, listaPesos, capacidadeMax):
    lin = len(listaPesos)-1
    col = capacidadeMax
    val = 1
    pesos = []
    while(val != 0):
        if(mat[lin][col] != mat[lin-1][col]):
            pesos.append(listaPesos[lin][0])
        col = col - lin
        lin -= 1
        val = mat[lin][col]
    return pesos


listaPesos = [[0, 0], [3, 40], [5, 100], [2, 50]]
print('+--------------------------------------------------------------------------------------------------+')
txt = 'Matriz criada:'
x = txt.center(100)
print(x)
print('+--------------------------------------------------------------------------------------------------+')
mat = preencheMatriz(4, 21, listaPesos)
printMatriz(mat)
print('+--------------------------------------------------------------------------------------------------+')
print()
print('Pesos a serem inseridos na mochila:')
print(pegarPesosResultantes(mat, listaPesos, 20))
print('+--------------------------------------------------------------------------------------------------+')