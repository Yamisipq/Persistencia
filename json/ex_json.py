import json
import os

archivo_json = "aprendices.json"
aprendices = []

def cargar_datos():
    """Carga los aprendices desde el archivo JSON"""
    global aprendices

    if os.path.exists(archivo_json):  # ✅ Verifica si el archivo existe
        try:
            with open(archivo_json, "r", encoding="utf-8") as file:
                aprendices = json.load(file)
            print(f"Se cargaron {len(aprendices)} aprendices.")
        except json.JSONDecodeError:
            print("Error al leer el archivo. Iniciando con lista vacía.")
            aprendices = []
    else:
        print("No se encontró el archivo. Se creará uno nuevo.")
        aprendices = []


def guardar_datos():
    """Guarda los aprendices en el archivo JSON"""
    try:
        with open(archivo_json, "w", encoding="utf-8") as file:
            json.dump(aprendices, file, ensure_ascii=False, indent=2)
        print("Datos guardados exitosamente.")
    except Exception as e:
        print(f"Error al guardar: {e}")


def generar_id():
    """Genera un ID único para un nuevo aprendiz"""
    if not aprendices:
        return 1
    return max(a['id'] for a in aprendices) + 1


def buscar_por_id(id_buscar):
    """Busca un aprendiz por ID"""
    for aprendiz in aprendices:
        if aprendiz['id'] == id_buscar:
            return aprendiz
    return None


def crear():
    """Crea uno o varios aprendices"""
    print("\n=== CREAR NUEVO(S) APRENDIZ(ES) ===")

    try:
        cantidad = int(input("¿Cuántos aprendices va a agregar? "))

        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0")
            return

        for i in range(cantidad):
            print(f"\n--- Aprendiz {i + 1} de {cantidad} ---")

            aprendiz = {
                "id": generar_id(),
                "nombre": input("Nombre: ").strip(),
                "apellidos": input("Apellidos: ").strip(),
                "direccion": input("Dirección: ").strip(),
                "telefono": input("Teléfono: ").strip(),
                "ficha": input("Ficha: ").strip()
            }

            aprendices.append(aprendiz)
            print(f"Aprendiz creado con ID: {aprendiz['id']}")

        guardar_datos()
        print(f"\nSe crearon {cantidad} aprendices exitosamente.")

    except ValueError:
        print("Cantidad inválida. Debe ser un número.")


def listar():
    """Lista todos los aprendices"""
    print("\n=== LISTA DE APRENDICES ===")

    if not aprendices:
        print("No hay aprendices registrados.")
        return

    for aprendiz in aprendices:
        print(f"\n{'─'*60}")
        print(f"ID: {aprendiz['id']}")
        print(f"Nombre: {aprendiz['nombre']} {aprendiz['apellidos']}")
        print(f"Dirección: {aprendiz['direccion']}")
        print(f"Teléfono: {aprendiz['telefono']}")
        print(f"Ficha: {aprendiz['ficha']}")
    print(f"{'─'*60}")
    print(f"\nTotal: {len(aprendices)} aprendices")


def actualizar():
    """Actualiza un aprendiz existente"""
    print("\n=== ACTUALIZAR APRENDIZ ===")

    if not aprendices:
        print("No hay aprendices para actualizar.")
        return

    listar()

    try:
        id_buscar = int(input("\nIngresa el ID del aprendiz a actualizar: "))
        aprendiz = buscar_por_id(id_buscar)

        if aprendiz:
            print(f"\nActualizando: {aprendiz['nombre']} {aprendiz['apellidos']}")
            print("(Presiona Enter para mantener el valor actual)\n")

            campos = ["nombre", "apellidos", "direccion", "telefono", "ficha"]

            for campo in campos:
                valor_actual = aprendiz[campo]
                nuevo_valor = input(f"{campo.capitalize()} [{valor_actual}]: ").strip()

                if nuevo_valor:
                    aprendiz[campo] = nuevo_valor

            guardar_datos()
            print("Aprendiz actualizado exitosamente.")
        else:
            print("No se encontró un aprendiz con ese ID.")
    except ValueError:
        print("ID inválido.")


def eliminar():
    """Elimina un aprendiz"""
    print("\n=== ELIMINAR APRENDIZ ===")

    if not aprendices:
        print("No hay aprendices para eliminar.")
        return

    listar()

    try:
        id_buscar = int(input("\nIngresa el ID del aprendiz a eliminar: "))
        aprendiz = buscar_por_id(id_buscar)

        if aprendiz:
            confirmar = input(f"¿Eliminar a {aprendiz['nombre']} {aprendiz['apellidos']}? (s/n): ")

            if confirmar.lower() == 's':
                aprendices.remove(aprendiz)
                guardar_datos()
                print("Aprendiz eliminado exitosamente.")
            else:
                print("Operación cancelada.")
        else:
            print("No se encontró un aprendiz con ese ID.")
    except ValueError:
        print("ID inválido.")


def menu_principal():
    """Menú principal del sistema"""
    cargar_datos()

    while True:
        print("\n" + "="*60)
        print("          DIRECTORIO DE APRENDICES")
        print("="*60)
        print("1. Crear aprendiz")
        print("2. Listar aprendices")
        print("3. Actualizar aprendiz")
        print("4. Eliminar aprendiz")
        print("5. Salir")
        print("="*60)

        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "1":
            crear()
        elif opcion == "2":
            listar()
        elif opcion == "3":
            actualizar()
        elif opcion == "4":
            eliminar()
        elif opcion == "5":
            print("\n¡Hasta luego!")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu_principal()