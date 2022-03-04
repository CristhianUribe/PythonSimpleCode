import os

from dominio.Pelicula import Pelicula
class CatalogoPeliculas(Pelicula):

    ruta_archivo = 'Peliculas.txt'

    @classmethod
    def agregarPelicula(cls,Pelicula):
        with open(cls.ruta_archivo,'a', encoding='utf8') as archivo:
            archivo.write(Pelicula.nombre)

    @classmethod
    def listarPelicula(cls):
        try:
            with open(cls.ruta_archivo,'r', encoding='utf8') as archivo:
                print('PELICULAS REGISTRADAS'.center(50, '*'))
                print(archivo.read())
                print('FIN'.center(50,'*'))
        except Exception as e:
                print(e)
                print('No se pudo recuperar ninguna pelicula.')
    @classmethod
    def eliminarArchivo(cls):
        os.remove(cls.ruta_archivo)
        print('Archivo Eliminado Correctamente.')






