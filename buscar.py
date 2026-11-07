from config import ARCHIVO_INVENTARIO


def buscar_por_codigo():
    codigo_buscado = input("Ingrese codigo del producto a buscar: ").strip().upper()
    archivo = open(ARCHIVO_INVENTARIO, "r", encoding="utf-8")
    encontrado = False

    for linea in archivo:
        campos = [campo.strip() for campo in linea.split("|")]
        if len(campos) == 4 and campos[0].upper() == codigo_buscado:
            print(f"\n>> Producto encontrado: {campos[1]}")
            print(f"   Precio: S/ {campos[2]}")
            print(f"   Stock disponible: {campos[3]} unidades")
            encontrado = True
            break

    archivo.close()

    if encontrado==False:
        print("\nProducto no encontrado en el inventario.")
