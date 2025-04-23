from datetime import datetime

def mostrar_menu():
    # Obtener la hora actual
    hora_actual = datetime.now().hour  # Usamos datetime directamente

    # Comprobamos las horas para determinar el momento del día
    if 6 <= hora_actual < 11:
        print("¡A desayunar! 🥐")
        print("1) Huevos revueltosn\n2) Pan con mermelada\n3) Avena con fruta")
        op = int(input("¿Qué opción eliges?: "))
        if op == 1:
            print("¡Huevitos revueltos! Buen desayuno 💪")
        elif op == 2:
            print("Pan y mermelada, clásico y delicioso 🍞")
        elif op == 3:
            print("Avena con fruta, ¡muy saludable! 🥣")
        else:
            print("Opción no válida 😕")
    
    elif 12 <= hora_actual < 15:
        print("¡Hora de la comida! 🍛")
        print("1) Pollo con arroz\n2) Pasta a la boloñesa\n3) Tacos al pastor")
        op = int(input("¿Qué opción eliges?: "))
        if op == 1:
            print("¡Pollo con arroz! Comida poderosa 🍗")
        elif op == 2:
            print("Pasta boloñesa... ¡ñam ñam! 🍝")
        elif op == 3:
            print("Tacos al pastor, ¡sabrosísimos! 🌮")
        else:
            print("Opción no válida 😕")
    
    elif 16 <= hora_actual < 18:
        print("¡Hora de la merienda! ☕")
        print("1) Yogur con granola\n2) Sándwich pequeño\n3) Fruta picada")
        op = int(input("¿Qué opción eliges?: "))
        if op == 1:
            print("¡Yogur y granola, excelente merienda! 🥣")
        elif op == 2:
            print("Un sándwich es justo lo que necesitas 🥪")
        elif op == 3:
            print("Fruta picada, energía natural 🍎")
        else:
            print("Opción no válida 😕")
    
    # CENA
    elif 19 <= hora_actual < 22:
        print("¡Hora de la cena! 🍽")
        print("1) Sopa ligera\n2) Ensalada\n3) Tortilla española")
        op = int(input("¿Qué opción eliges?: "))
        if op == 1:
            print("Una sopa ligera para cerrar el día 🍲")
        elif op == 2:
            print("Ensalada fresca, ¡muy bien! 🥗")
        elif op == 3:
            print("Tortilla española, ¡rico! 🇪🇸")
        else:
            print("Opción no válida 😕")

    # FUERA DE HORARIO
    else:
        print("No es hora de comer ahora 😴")

# Ejecutar el menú
mostrar_menu()