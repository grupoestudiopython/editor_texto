#Proyecto "Editor de texto en consola".

Este es un proyecto con fines meramente educativos y prácticos, llevado a
cabo por algunos de los integrantes del
[Grupo Estudio Python](https://plus.google.com/u/0/communities/105786905874914734353)
con el ánimo de practicar algo de lo aprendido.

## Modo de uso
./editor.py -e /ruta/al/archivo/que/desea/editar.txt => Editar archivo<br />
./editor.py -h => Muestra los parámetros que acepta el script<br />
./editor.py -n /ruta/donde/quiere/guardar/el/archivo.txt => Crear nuevo archivo<br />
./editor.py -v => Muestra la versión actual del editor<br />
./editor.py => Se creará un archivo temporal hasta que el usuario decida guardarlo<br />


#TODOLIST

1. Crear archivo de configuración con valores por defecto, tales como:
    <del>- Codificación por defecto para todos los archivos</del>

    ###### Las siguientes variables se tendrán en cuenta para futuras versiones del editor
    - Ruta a las carpetas que contienen los archivos para el resaltado de sintaxis
    - Ruta a la carpeta que contiene los plugins, etc.
    - Usar espacios o tabuladores por defecto
    - Si son espacios, entonces cuántos espacios debe usar el 
      editor por defecto para reemplazar un tabulador

2. <del>Crear un archivo .py ejecutable que será el script del editor, que
    reciba parámetros al ser llamado. Ejemplo: editor.py -n filename.txt

	*Si no se pasa ningún parámetro al script al ser llamado, se creará
	un archivo temporal y la primera vez que el usuario quiera guardar
    los cambios, se le pedirá un nombre y una ruta para el archivo.*</del>


3. Manejo de archivos de texto (por ahora sólo archivos .txt)
    - Verificar que el archivo existe (si es que el usuario quiere abrir
      un archivo existente) y que la extensión sea .txt
    - Codificación a usar
    - Salto de línea (sólo Windows y Unix por ahora)
    - Abrir siempre los archivos en modo lectura y escritura, a menos que
      el usuario actual no posea permisos de escritura, en tal caso se
      intentará abrir en modo "sólo lectura"
    - Automatizar el guardado automático cada "x" tiempo transcurrido

4. Ingreso de información por teclado (mouse opcional)
    - Escribir en el archivo
    - Moverse por el texto con las flechas del teclado
    - Combinaciones de teclas
    - Búsqueda de texto dentro de la sesión actual
    - Deshacer la última acción
    - Ir a la línea n
    - Copiar y pegar

5. Una barra de información en la parte inferior del editor que muestre
	información básica, por ejemplo:
    - La línea actual del cursor
    - Ruta y nombre del nombre del archivo
    - Codificación del archivo
    - Número de caracteres que tiene el archivo (en tiempo real), es decir,
      a medida que se va escribiendo o borrando, este valor debe ir 
      aumentando o disminuyendo según el caso.
    - Errores si llegasen a ocurrir




## Copyright

Copyright (c) 2013 Grupo Estudio Python. See LICENSE for further details.
