import os

from dominio.Pelicula import Pelicula
from resource.file_modified import FileModified
from servicio.CatalagoPeliculas import CatalogoPeliculas as pelis


while True:
    print(f'''
    *CATALOGO DE PELICULAS*
    1. AGREGAR PELICULA
    2. LISTAR PELICULAS
    3. ELIMINAR ARCHIVO DE PELICULAS
    4. SALIR
    ''')
    opcion = int(input('Ingrese Opcion: '))

    if opcion == 1:
       txtNombre = input("Ingrese nombre de pelicula: ")
       pelicula = Pelicula(txtNombre)
       pelis.agregarPelicula(pelicula)
    elif opcion == 2:
        pelis.listarPelicula()
    elif opcion == 3:
        pelis.eliminarArchivo()
    elif opcion == 4:
        break;

    # Para DOS/Windows
    os.system('cls')

print('Gracias por usar el sistema de peliculas'.center(50,'-'))