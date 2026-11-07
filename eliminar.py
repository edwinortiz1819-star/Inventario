from config import ARCHIVO_INVENTARIO


def eliminar_producto():
    print("\n--- ELIMINAR PRODUCTO DEL INVENTARIO ---")
    codigo_eliminar = input("Ingrese código del producto a eliminar: ").strip().upper()

    # 1. Cargamos todas las líneas a memoria
    archivo = open(ARCHIVO_INVENTARIO, "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    lista_filtrada = []
    for linea in lineas:
        campos = linea.strip().split("|")
        # Si NO es el código que queremos borrar, lo conservamos
        if len(campos) != 4 or campos[0].upper() != codigo_eliminar:
            lista_filtrada.append(linea)
        else:
            print(f"Eliminando el producto con código {codigo_eliminar}: {linea}")

    # 2. Reescribimos el archivo sin el registro eliminado
    archivo = open(ARCHIVO_INVENTARIO, "w", encoding="utf-8")
    archivo.writelines(lista_filtrada)
    archivo.close()
