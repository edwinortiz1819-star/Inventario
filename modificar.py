from config import ARCHIVO_INVENTARIO


def modificar_producto():
    codigo_buscado = input("Ingrese código del producto a modificar: ").strip().upper()

    # 1. Cargamos todas las líneas a memoria
    archivo = open(ARCHIVO_INVENTARIO, "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    lista_actualizada = []
    for linea in lineas:
        campos = linea.strip().split("|")
        if len(campos) == 4 and campos[0].upper() == codigo_buscado:
            print(f"Producto actual: {campos[1]} (Precio actual: S/ {campos[2]}, Stock actual: {campos[3]})")
            nuevo_precio = float(input("Ingrese NUEVO precio en soles: ").strip())
            nuevo_stock = int(input("Ingrese NUEVO stock: ").strip())
            lista_actualizada.append(f"{campos[0]}|{campos[1]}|{nuevo_precio:.2f}|{nuevo_stock}\n")
        else:
            lista_actualizada.append(linea)  # Conservamos sin cambios

    # 2. Reescribimos el archivo completo con los datos actualizados
    archivo = open(ARCHIVO_INVENTARIO, "w", encoding="utf-8")
    archivo.writelines(lista_actualizada)
    archivo.close()
    print("3Producto actualizado c3orrectamente en disco!")
