# Neo:
# Proposito:
# Decodifica un script de una matriz que es dada de la siguiente forma:
# Se inserta primero dos valores, el primero representa el número de filas
# El segundo el número de columnas, por ejemplo: 7 3 indica que haremos una matriz
# de 7 filas y 3 columnas.
# Después se ubican los valores alfanúmericos deseados por el usuario.
# Ejemplo:
# Input:
# 7 3
# Tsi
# h%x
# i #
# sM
# $a
# #t%
# ir!
# Output:
# 'This is Matrix# %!'

#Importo la libreria para exp. regulares
import re
from typing import final

print("Input:")

#Creo un compilador para que detecte un patron
compiler = re.compile("\d+")

#Encuentro los caracteres con el patron del compilador y los guardo en un array
matrixDimension = compiler.findall(input())

#Saco los valores del array y los guardo en dos variables
try:
    rows = int( matrixDimension[0] )
    cols = int( matrixDimension[1] )
except Exception:
    print('Error!, no insertaste dos números para la dimensión de la matriz.')
    quit()

#Está será la matriz
matrix = []

#Esta será la salida
output = str()

def mk_Matrix():
    matrix = []
    output = str()

    #Acá se van guardando los valores que asignemos a cada fila
    for _ in range(rows):
        rowValue = input()
        while(len(rowValue) != cols):
            print('Insertaste alguna linea de digitos diferente a la permitida: ' + str(cols))
            print('Intentalo de nuevo!')
            rowValue = input()
        matrix.append(rowValue)

    #Guardamos el script decodificado acá
    for n in range(cols):
        for word in matrix:    
            output += word[n]

    return output

output = mk_Matrix()

#Se va a partir el output en 3 partes y se reemplazaran los simbolos por un espacio:
#Primera parte:
regex = '[a-zA-Z0-9]+.+'
firstPart = re.sub(regex, '', output)
regex = '\s+'
part1 = re.sub(regex, ' ', ''.join(firstPart))
#Tercera parte:
regex = '.+[a-zA-Z0-9]+'
thirdPart = re.sub(regex, '', output)
regex = '\s+'
part3 = re.sub(regex, ' ', ''.join(thirdPart))
#Segunda parte:
regex = part1 + '|' + part3
secondPart = re.sub(regex, '', output)
regex = '(\W|_)+'
part2 = re.sub(regex, ' ', ''.join(secondPart))

finalOutput = part1 + part2 + part3

#Resultado
print("Output: " + finalOutput)