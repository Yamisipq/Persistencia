import csv

list_aprendices_clave=["nombre","apellido","direccion","telefono", "ficha"]
list_aprendices=[]

x=int(input("Ingresa la cantidad de aprendices: "))

for i in range(x):
    e_actual={}
    print(f"Para el estudiante {i+1}")
    for clave in list_aprendices_clave:
        value= input(f"Ingresa la siguiente info: {clave}:" )

        e_actual[clave]=value

    list_aprendices.append(e_actual)


print("\n--- Información de Todos los Estudiantes ---")
for idx, estudiante in enumerate(list_aprendices):
    print(f"\nEstudiante {idx+1}:")
    for clave, valor in estudiante.items():
        print(f"  {clave.capitalize()}: {valor}")