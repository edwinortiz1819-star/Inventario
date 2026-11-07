from config import ARCHIVO_INVENTARIO


def listar():
    archivo = open(ARCHIVO_INVENTARIO, "r", encoding="utf-8")

    for linea in archivo:
        campos = linea.split("|")
        codigo = campos[0]
        nombre = campos[1]
        precio = float(campos[2])   
        stock = int(campos[3])     
        print(f" [{codigo}] {nombre} - Stock actual: {stock} - precio {precio:.2f} ");
    archivo.close()
