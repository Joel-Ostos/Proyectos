año_actual = int(input("Digite el año con el que desea empezar: "))
cant_años = 0

while cant_años <30:
    cant_años += 1
    año_actual += 1
    if (año_actual %4 == 0) or año_actual % 100 == 0:
        print(año_actual, "Es un año bisiesto")
    else:
        print(año_actual, 'No es un año bisiesto')

