import json

class DirectorioAprendices:
    def __init__(self, archivo="aprendices.json"):
        self.archivo = archivo
        self.aprendices = []
        self.cargar_datos()

    def cargar_datos(self):

        try:
            with open(self.archivo, "r", encoding="utf-8") as file:
                self.aprendices = json.load(file)
            print(f"Se cargaron {len(self.aprendices)} aprendices.")
        except FileNotFoundError:
            print("No se encontró archivo. Se creará uno nuevo.")
            self.aprendices = []
        except json.JSONDecodeError:
            print("Error al leer el archivo. Iniciando con lista vacía.")
            self.aprendices = []

    def guardar_datos(self):

        try:
            with open(self.archivo, "w", encoding="utf-8") as file:
                json.dump(self.aprendices, file, ensure_ascii=False, indent=2)
            print("Datos guardados exitosamente.")
        except Exception as e:
            print(f"Error al guardar: {e}")

    def crear(self):

        print("\n=== CREAR NUEVO(S) APRENDIZ(ES) ===")

        try:
            cantidad = int(input("¿Cuántos aprendices va a agregar? "))

            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0")
                return

            for i in range(cantidad):
                print(f"\n--- Aprendiz {i + 1} de {cantidad} ---")

                aprendiz = {
                    "id": self._generar_id(),
                    "nombre": input("Nombre: ").strip(),
                    "apellidos": input("Apellidos: ").strip(),
                    "direccion": input("Dirección: ").strip(),
                    "telefono": input("Teléfono: ").strip(),
                    "ficha": input("Ficha: ").strip()
                }

                self.aprendices.append(aprendiz)
                print(f"Aprendiz creado con ID: {aprendiz['id']}")

            self.guardar_datos()
            print(f"\nSe crearon {cantidad} aprendices exitosamente.")

        except ValueError:
            print("Cantidad inválida. Debe ser un número.")

    def listar(self):
        """Lista todos los aprendices"""
        print("\n=== LISTA DE APRENDICES ===")

        if not self.aprendices:
            print("No hay aprendices registrados.")
            return

        for aprendiz in self.aprendices:
            print(f"\n{'─'*60}")
            print(f"ID: {aprendiz['id']}")
            print(f"Nombre: {aprendiz['nombre']} {aprendiz['apellidos']}")
            print(f"Dirección: {aprendiz['direccion']}")
            print(f"Teléfono: {aprendiz['telefono']}")
            print(f"Ficha: {aprendiz['ficha']}")
        print(f"{'─'*60}")

    def actualizar(self):

        print("\n=== ACTUALIZAR APRENDIZ ===")

        if not self.aprendices:
            print("No hay aprendices para actualizar.")
            return

        self.listar()

        try:
            id_buscar = int(input("\nIngresa el ID del aprendiz a actualizar: "))
            aprendiz = self._buscar_por_id(id_buscar)

            if aprendiz:
                print(f"\nActualizando: {aprendiz['nombre']} {aprendiz['apellidos']}")
                print("(Presiona Enter para mantener el valor actual)\n")

                campos = ["nombre", "apellidos", "direccion", "telefono", "ficha"]

                for campo in campos:
                    valor_actual = aprendiz[campo]
                    nuevo_valor = input(f"{campo.capitalize()} [{valor_actual}]: ").strip()

                    if nuevo_valor:
                        aprendiz[campo] = nuevo_valor

                self.guardar_datos()
                print("Aprendiz actualizado exitosamente.")
            else:
                print("No se encontró un aprendiz con ese ID.")
        except ValueError:
            print("ID inválido.")

    def eliminar(self):

        print("\n=== ELIMINAR APRENDIZ ===")

        if not self.aprendices:
            print("No hay aprendices para eliminar.")
            return

        self.listar()

        try:
            id_buscar = int(input("\nIngresa el ID del aprendiz a eliminar: "))
            aprendiz = self._buscar_por_id(id_buscar)

            if aprendiz:
                confirmar = input(f"¿Eliminar a {aprendiz['nombre']} {aprendiz['apellidos']}? (s/n): ")

                if confirmar.lower() == 's':
                    self.aprendices.remove(aprendiz)
                    self.guardar_datos()
                    print("Aprendiz eliminado .")
                else:
                    print("Operación cancelada.")
            else:
                print("No se encontró un aprendiz con ese ID.")
        except ValueError:
            print("ID inválido.")

    def _generar_id(self):
        """Genera un ID único para un nuevo aprendiz"""
        if not self.aprendices:
            return 1
        return max(a['id'] for a in self.aprendices) + 1

    def _buscar_por_id(self, id_buscar):
        """Busca un aprendiz por ID"""
        for aprendiz in self.aprendices:
            if aprendiz['id'] == id_buscar:
                return aprendiz
        return None


def menu_principal():

    directorio = DirectorioAprendices()

    while True:
        print("\n" + "="*60)
        print("DIRECTORIO DE APRENDICES")
        print("="*60)
        print("1. Crear aprendiz")
        print("2. Listar aprendices")
        print("3. Actualizar aprendiz")
        print("4. Eliminar aprendiz")
        print("5. Salir")
        print("="*60)

        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "1":
            directorio.crear()
        elif opcion == "2":
            directorio.listar()
        elif opcion == "3":
            directorio.actualizar()
        elif opcion == "4":
            directorio.eliminar()
        elif opcion == "5":
            print("\n¡Hasta luego!")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu_principal()