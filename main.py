from registrar import registrar_producto
from buscar import buscar_por_codigo
from listar import listar
from modificar import modificar_producto
from eliminar import eliminar_producto


def main():
    opcion = 0

    while opcion != 6:
        print("\n=== MINIMARKET - INVENTARIO CON PIPE ===")
        print("1. Registrar producto")
        print("2. Buscar por codigo")
        print("3. Listar")
        print("4. Modificar")
        print("5. Eliminar")
        print("6. Salir")
        opcion = int(input("Opcion: ").strip())

        if opcion == 1:
            registrar_producto()
        elif opcion == 2:
            buscar_por_codigo()
        elif opcion == 3:
            listar()
        elif opcion == 4:
            modificar_producto()
        elif opcion == 5:
            eliminar_producto()
        elif opcion == 6:
            print("Saliendo del inventario...")
        else:
            print("Opcion no valida.")


main()
