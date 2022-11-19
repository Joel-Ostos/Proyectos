'''Reto #2
 ¿ES UN ANAGRAMA?
 Fecha publicación enunciado: 03/01/22
 Fecha publicación resolución: 10/01/22
 Dificultad: MEDIA
 
 Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 NO hace falta comprobar que ambas palabras existan.
 Dos palabras exactamente iguales no son anagrama.'''

palabra_1 = str(input('Escriba la primera palabra: '))
palabra_2 = str(input('Escriba la segunda palabra: '))

estado = True
if palabra_1 == palabra_2:
    estado = False
else:
    for i in palabra_1:
        if i in palabra_2:
            estado =True
        else:
            estado= False
print(estado)

