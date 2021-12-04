# Neo:
# Proposito:
# Decodifica un script de una matriz que es dada de la siguiente forma:
# Se inserta primero dos valores, el primero representa el número de filas
# El segundo el número de columnas, por ejemplo: 7 3 indica que haremos una matriz
# de 7 filas y 3 columnas.
# Después se ubican los valores alfanúmericos deseados por el usuario.
# Ejemplo
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

print("Ingrese el script de matriz:")

#Creo un compilador para que detecte un patron
compiler = re.compile("\d+")

#Encuentro los caracteres con el patron del compilador y los guardo en un array
matrixDimension = compiler.findall(input())

#Saco los valores del array y los guardo en dos variables
rows = int( matrixDimension[0] )
cols = int( matrixDimension[1] )

#Está será la matriz
matrix = []

#Esta será la salida
output = str()

#acá se van guardando los valores que asignemos a cada fila
for _ in range(rows):
    rowValue = input()
    matrix.append(rowValue)

#guardamos el script decodificado acá
for n in range(cols):
    for word in matrix:
        output += word[n]

#se modifica de tal forma que se borren los valores que no son alfanuméricos
#entre valores alfanuméricos
regex = '\W*\w'
regex2 = '((\W*|\w*)\w)'
compiler = re.compile(regex)
result = compiler.findall(output)
result2 = re.sub('\W', ' ', ''.join(result))
result3 = re.sub(regex2, '', output)
output = ''.join(result2) + ''.join(result3)

#Elimina espacios en blanco que sobran
output = re.sub('\s\s+', ' ', output)

# Resultado
print(output)