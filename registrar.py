from config import ARCHIVO_INVENTARIO


def registrar_producto():
    codigo = input("Ingrese codigo del producto (Ej: P10): ").strip().upper()
    nombre = input("Ingrese nombre o descripcion: ").strip()
    precio = float(input("Ingrese precio en soles (Ej: 4.50): ").strip())
    stock = int(input("Ingrese stock disponible: ").strip())

    registro = f"{codigo}|{nombre}|{precio:.2f}|{stock}\n"
    archivo = open(ARCHIVO_INVENTARIO, "a", encoding="utf-8")
    archivo.write(registro)
    archivo.close()
    print(">> Producto registrado con exito con formato PIPE.")
