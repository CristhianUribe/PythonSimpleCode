import os
from resource.file_modified import FileModified

# while True:
#     print(f'''
#     *CATALOGO DE PELICULAS*
#     1. AGREGAR PELICULA
#     2. LISTAR PELICULAS
#     3. ELIMINAR ARCHIVO DE PELICULAS
#     4. SALIR
#     ''')
#     opcion = int(input('Ingrese Opcion: '))
#
#     if opcion==1:
#         print('Opcion 1')
#     elif opcion == 2:
#         print('Opcion 3')
#
#     # Para DOS/Windows
#     os.system('cls')

with FileModified('db.txt') as archivo:
    # archivo.write("Hola mundo")
    print(archivo.read())