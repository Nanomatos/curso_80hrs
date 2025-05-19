def agenda_contactos():
    contactos = {}
    print("Bienvenido a tu agenda de contactos")

    while True:
        nombre = input("Nombre del contacto (escribe Fin para salir). ").capitalize()
        if nombre == "Fin":
            break
        telefono = input(f"Ingrese el número de {nombre}:")
        contactos[nombre] = telefono
        print(f"Contacto '{nombre}' agregado a la agenda.")
    print("Tu agenda de contactos tiene", len(contactos), "contactos:")
    for nombre, telefono in contactos.items():
        print(f"- {nombre}: {telefono}")
agenda_contactos()
# Este programa permite al usuario crear una agenda de contactos