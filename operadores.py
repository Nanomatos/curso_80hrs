# Operadores lógicos en Python
# Los operadores lógicos en Python son utilizados para combinar expresiones booleanas y evaluar condiciones.
Megustapizza = False
negacion =  not Megustapizza
print(f"Proposicion original. Me gusta la pizza: { Megustapizza}")
print(f"Negacion de la proposicion original. Me gusta la pizza: {negacion}")
"""
proposicion1 = True
proposicion2 = False

conjuncion = proposicion1 and proposicion2

print(f"proposicion1: {proposicion1}")
print(f"proposicion2: {proposicion2}")
print(f"conjuncion de las preoposiciones: {conjuncion}")


proposicion1 = True
proposicion2 = False

disyuncion = proposicion1 or proposicion2

print(f"proposicion1: {proposicion1}")
print(f"proposicion2: {proposicion2}")
print(f"conjuncion de las preoposiciones: {disyuncion}")


# Ejemplo 1: "Si llueve, entonces llevaré un paraguas"
llueve = False
llevar_paraguas = llueve  # Implicación: si llueve implica llevar paraguas
print(f"Si llueve ({llueve}), entonces llevaré un paraguas: {llevar_paraguas}")


# Ejemplo 2: "Si estudio, entonces aprobaré el examen"
estudio = False
aprobar_examen = estudio or not estudio  # Implicación: si estudio implica aprobar o no estudiar equivale a aprobar
print(f"Si estudio ({estudio}), entonces aprobaré el examen: {aprobar_examen}")

# Ejemplo 3: "Si como chocolate, entonces estaré feliz"
come_chocolate = True
feliz = come_chocolate  # Implicación: comer chocolate implica estar feliz
print(f"Si como chocolate ({come_chocolate}), entonces estaré feliz: {feliz}")
"""
