# Ingrese una lista de compras: manzanas, plátanos, leche, pan
# Los productos en la lista de compras son: ['manzanas', 'plátanos', 'leche', 'pan']

def convertir_lista_a_tupla(lista):
    return tuple(lista)  # Convertir la lista a tupla

if __name__ == "__main__":
    compras = input("Ingrese una lista de compras: ")
    productos = compras.split(", ")
    print(f"Los productos en la lista de compras son: {productos}")
    productos_tupla = convertir_lista_a_tupla(productos)
