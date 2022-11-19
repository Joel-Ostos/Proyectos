'''
Reto #0
EL FAMOSO "FIZZ BUZZ"
Fecha publicación enunciado: 27/12/21
Fecha publicación resolución: 03/01/22
Dificultad: FÁCIL
Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''
num = 1
while num <= 100:
    if num % 3 == 0 and num % 5 == 0:
        print('fizzbuzz')
        #num +=1

    elif  num % 3 == 0:
        print('fizz')
        #num +=1

    elif  num % 5 == 0:
        print('buzz')
        #num +=1
        
    else:
        print(num)
    num+=1
