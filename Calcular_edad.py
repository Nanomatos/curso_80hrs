def Calcular_edad():

    nombre = input("Cual es tu nombre?")
    año_nacimiento = int(input("En que año naciste?. "))
    año_actual = 2025
    edad = año_actual - año_nacimiento
    print(f"Hola {nombre}, tienes {edad} años. ")

Calcular_edad()