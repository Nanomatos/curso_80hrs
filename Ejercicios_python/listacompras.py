def lista_compras():
    compras = []

    print("Bienvenida a tu lista de compras")
    
    while True:
        producto = input("Agrega un productoa tu lista, escribe 'Fin' para terminar: ")
        if producto.lower() == 'fin':
            break
        else:
            compras.append(producto)
            print(f"Producto '{producto}' agregado a la lista.")

    print("Tu lista de compras tiene", len(compras), "productos:")
    for item in compras:
        print(f"- {item.capitalize()}")
lista_compras()
# Este programa permite al usuario crear una lista de compras