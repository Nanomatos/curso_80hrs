def main():
    amigos = []

    print("Vamos a hacer una lista de tus amigos")

    while True:
        nombre = input("Ingresa el nombre de un amigo: ")
        amigos.append(nombre)

        respuesta = input("¿Quieres agregar otro amigo? s/n: ").lower()

        if respuesta == "n":
            break

    print("\nLista de tus amigos:")
    for amigo in amigos:
        print(f"-{amigo}")

    print(f"\ntienes {len(amigos)} amigos en la lista")

main()