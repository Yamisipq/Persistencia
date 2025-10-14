lineas_a_escribir = ["Manzanas\n", "Peras\n", "Naranjas\n"]

l_p = {
    "Manzanas": "= 4500)",
    "Peras": "= 6000)",
    "Naranjas": "= 3700)",
}

with open("lista_compras.txt", "w") as archivo:
    archivo.writelines(lineas_a_escribir)

    encabezado = ("--- Mi Lista de Compras ---\n")

contenido = []

with open("lista_compras.txt", "r") as archivo:
    # Leer el archivo línea por línea
    if contenido != encabezado:
        contenido.append(encabezado)
    for linea in archivo:
        producto = linea.strip()

        if producto in l_p:
            nueva_linea = linea.strip() + l_p[producto] + "\n"
        else:
            nueva_linea = linea

        contenido.append(nueva_linea)

# 3. Reescribir el Archivo (Write 'w')
with open("lista_compras.txt", "w") as archivo:
    archivo.writelines(contenido)

print("Se actualizó")