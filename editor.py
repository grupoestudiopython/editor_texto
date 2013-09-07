#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-

import argparse

class Editor(object):
    """Editor de texto en consola"""

    def __init__(self):

        self.__version = '0.1' # versión actual del editor
        # Se declaran las variables para poder usarlas luego cuando se lea
        # el archivo de configuración
        self.encoding = ''
        # Carga las variables por defecto desde el archivo de configuración
        self.leer_configuracion()


    def version(self):
        """Muestra por pantalla la versión del editor"""
        return 'Editor v%s' % self.__version

    def leer_configuracion(self):
        """Lee el archivo de configuración para cargar las variables
        por defecto"""

        # archivo que contiene la configuración del editor
        with open('editor.conf') as config:
            for line in config:

            # itera sobre cada línea del archivo de configuración
            #for line in config.readlines():
                # mira si la línea empieza por "ENCODING"
                if line.startswith('ENCODING'):
                    # Las siguientes 2 variables almacenan el rango de posición
                    # donde se encuentra el valor de la variable
                    primer_apostrofe = line.find("'") + 1
                    segundo_apostrofe = line.find("'", primer_apostrofe)

                    # Se recupera el valor deseado en los rangos encontrados
                    self.encoding = line[primer_apostrofe:segundo_apostrofe]


    def nuevo(self, ruta):
        """Método para crear archivos nuevos, recibe el parámetro ruta que
        será donde se guardará el archivo. Después de verificar que se puede
        crear el archivo, se pasa el manejador al método main (self.main)."""
        pass


    def editar(self, ruta):
        """Método para abrir los archivos cuando existen y el usuario desea
        editarlos. Después de verificar que el archivo existe, lo abre y
        pasa el manejador al método "main" (self.main)."""
        pass


    def main(self, manejador):
        """Método principal del editor de texto por consola, es el método
        que controla el editor de texto por así decirlo. Recibe el manejador
        del archivo, ya sea un nuevo archivo de texto o uno existente"""
        pass




if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Editor de texto en consola')
    parser.add_argument('-e', '--edit', help='Editar archivo')
    parser.add_argument('-n', '--new', help='Crear archivo')
    parser.add_argument('-v', '--version', help='Muestra la versión del editor',
                        action='store_true')
    parametros = parser.parse_args()

    # Instancia de la clase Editor
    editor = Editor()

    # Muestra por pantalla la versión actual del editor
    if parametros.version:
        print(editor.version())

    # Cuando el usuario desea editar un archivo recién ejecuta el script
    if parametros.edit:
        editor.editar(parametros.edit)
    # Cuando el usuario desea crear un archivo nuevo cuando recién ejecuta
    # el script
    elif parametros.new:
        editor.nuevo(parametros.new)
    # si el usuario no pasó ninguna opción, entonces se crea un archivo
    # temporal
    else:
        from tempfile import mkstemp
        # Crea un archivo temporal
        archivo_temporal = mkstemp()[1]
        editor.nuevo(archivo_temporal)
