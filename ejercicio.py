# Ingrese una lista de compras: manzanas, plátanos, leche, pan
# Los productos en la lista de compras son: ['manzanas', 'plátanos', 'leche', 'pan']

compras = input("Ingrese una lista de compras: ")
productos = compras.split(", ")
print(f"Los productos en la lista de compras son: {productos}")

def convertir_lista_a_tupla(lista):
    return tuple(lista)  # Convertir la lista a tupla

productos_tupla = convertir_lista_a_tupla(productos)

