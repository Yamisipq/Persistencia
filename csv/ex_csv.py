import csv
from tabulate import tabulate

list_aprendices_clave = ["nombre", "apellido", "direccion", "telefono", "ficha"]
list_aprendices = []
archivo_csv = "aprendices.csv"


def cargar_aprendices():
    """Carga los aprendices desde el archivo CSV"""
    global list_aprendices
    try:
        with open(archivo_csv, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            list_aprendices = list(reader)
            """carga todos los aprendices"""
        print(f"Se cargaron {len(list_aprendices)} aprendices del archivo.")
    except FileNotFoundError:
        print("No se encontró archivo existente. Se creará uno nuevo.")
    except Exception as e:
        print(f"Error al cargar archivo: {e}")


def guardar_aprendices():
    """Guarda los aprendices en el archivo CSV"""
    try:
        with open(archivo_csv, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=list_aprendices_clave)
            writer.writeheader()
            """usa las claves"""
            writer.writerows(list_aprendices)
        print("Datos guardados exitosamente.")
    except Exception as e:
        print(f"Error al guardar: {e}")


def agregar_aprendiz():
    """Agrega uno o varios nuevos aprendices"""
    print("\n=== AGREGAR NUEVO APRENDIZ ===")

    x = int(input("Ingrese el número de aprendices: "))

    for i in range(x):
        print(f"\n--- Aprendiz {i + 1} ---")
        nuevo_aprendiz = {}
        for clave in list_aprendices_clave:
            valor = input(f"Ingrese {clave}: ").strip()
            nuevo_aprendiz[clave] = valor

        list_aprendices.append(nuevo_aprendiz)

    guardar_aprendices()
    print(f"{x} aprendiz(es) agregado(s) exitosamente.")


def ver_aprendices():
    """Muestra todos los aprendices"""
    print("\n=== LISTA DE APRENDICES ===")
    if not list_aprendices:
        print("No hay aprendices registrados.")
        return

    print(tabulate(list_aprendices, headers="keys", tablefmt="grid", showindex=range(1, len(list_aprendices) + 1)))

def actualizar_aprendiz():
    """Actualiza la información de un aprendiz"""
    print("\n=== ACTUALIZAR APRENDIZ ===")
    ver_aprendices()

    if not list_aprendices:
        return

    try:
        indice = int(input("\nIngresa el número del aprendiz a actualizar: ")) - 1

        if 0 <= indice < len(list_aprendices):
            aprendiz = list_aprendices[indice]
            print(f"\nActualizando: {aprendiz['nombre']} {aprendiz['apellido']}")
            print("(Presiona Enter para mantener el valor actual)")

            for clave in list_aprendices_clave:
                valor_actual = aprendiz[clave]
                nuevo_valor = input(f"{clave} [{valor_actual}]: ").strip()

                if nuevo_valor:
                    aprendiz[clave] = nuevo_valor

            guardar_aprendices()
            print("Aprendiz actualizado exitosamente.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def menu_principal():
    """Muestra el menú principal"""
    while True:
        print("     SISTEMA DE GESTIÓN DE APRENDICES - CRUD")
        print("\n")
        print("1. Agregar aprendiz")
        print("2. Ver todos los aprendices")
        print("3. Actualizar aprendiz")
        print("4. Salir")

        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            agregar_aprendiz()
        elif opcion == "2":
            ver_aprendices()
        elif opcion == "3":
            actualizar_aprendiz()
        elif opcion == "4":
            print("\n¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    cargar_aprendices()
    menu_principal()