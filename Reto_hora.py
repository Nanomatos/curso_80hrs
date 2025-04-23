import datetime

def mostrar_menu():

hora_actual = datetime.datetime.now().hour

if 6 <= hora_actual < 11:
    print(Desayuno)
    print("Platos: Huevos revueltos, Pan con mermelada, Avena con fruta")
    op = int(input("Que opción eliges?: "))
elif 12 <= hora_actual < 15:
    print(Comida)
    print("Platos: Pollo con arroz, Pasta a la boloñesa, Tacos al pastor")
    op = int(input("Que opción eliges?: "))
elif 16 <= hora_actual < 18:
    print(Merienda)
    print("Yogur con granola, Sándwich pequeño, Fruta picada")
    op = int(input("Que opción eliges?: "))
elif 19 <= hora_actual < 22:
    print(Cena)
    print("Platos: Sopa ligera, Ensalada, Tortilla española")
    op = int(input("Que opción eliges?: "))

#comentario


