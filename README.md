# MinTIC2020 Ciclo 1
Bienvenido al repositorio que contiene el ejercicio de cierre del Ciclo 1 de MisiónTIC 2022 del Gobierno de Colombia.
En este ejercicio usted realizará un paso a paso en donde usando los conocimientos aprendidos en python, nuevas cosas que va a aprender, y algunos elementos previamente construidos por sus profesores, creara un versión bastante sencilla de una Tienda Virtual.
De esta manera, usted podrá ver de una forma directa como utilizar los conceptos que aprendió en este ciclo, además de evidenciar la importancia del trabajo en equipo con otros roles tradicionales (como el caso de los desarrolladores front-end) en la conformación de equipos de desarrollo de software.


## Pre-requisitos 
Para el presente ejercicio usted debe contar con una versión de Python >= 3.6. Si no es así, por favor, actualice su versión de Python.

Este ejercicio deberá correrse sobre un IDE (el presentado en el curso es VS Code), por lo cual se recomienda no intentar hacer el ejercicio en CoLAB o en Repl.it.

Adicionalmente, deben instalarse unos módulos de la galería de Python que son de bastante uso en el desarrollo de aplicaciones web.

En primera instancia, usted debe tener un entorno virtual construido, para evitar conflictos versiones de módulos y tecnologías que usted tenga en otros proyectos.
Siendo así, vaya a la ventana de comandos (terminal, powershell, o similar), y ejecute la siguiente instrucción:.
python -m venv nombre_entorno


Para este ejercicio, el nombre del entorno será "env"  (es conmún que los desarrolladores usen 'env'como nombre del entorno virtual). Para trabajar dentro del entorno virtual, primero debe activarse el mismo, lo cual puede hacer con la siguiente instrucción:
source env/bin/activate

si usted coloco un nombre distinto para el entorno virtual, deberá ajustar la instrucción anterior.

En este punto puede verificar la versión de python usada dentro del entorno virtual usando la instrucción:
python --version

Una vez tenga activo su entorno virtual, es momento  de crear un archivo en el cual usted coloque los módulos (y se recomienda también las versiones) que usted necesita para el desarrollo apropiado del proyecto. Estando en la raíz del proyecto, cree un archivo denominado 'requeriments.txt', y en él coloque el texto a continuación:
setuptools==50.3.0
Django==3.1.2
pymongo==3.11.0


De allí, se tienen la siguiente explicación:
Django - Framework ampliamente reconocimiento para el desarrollo de python en web, especialmente por la facilidad que brinda al momento de manejar MVC.
pymongo - módulo que permite la conexión y manipulación de información en el motor de base de datos de MongoDB.
setuptools - librería que ayuda a la gestión de otros módulos con python, mantener actualizaciones, entre otros.

Ahora, luego de guardar el archivo con los módulos requeridos, puede colocar la siguiente instrucción para instalar todo lo enlistado en el archivo:\
pip install -r requirements.txt

Si usted observa, tener un archivo como este es útil, primero porque puede instalar todos los módulos con una sola instrucción; segundo, porque cuando necesite recrear su entorno de desarrollo será mucho más rápido.

Para verificar la versión instalada de Django, puede usar la siguiente instrucción:
python -m django --version

Ahora, usted tiene su entorno de desarrollo configurado para el ejercicio de la Tienda Virtual. Ahora, es momento de entrar a trabajar con Django.

## Manejo Básico de Django
Django es un Framework que ayuda a mantener de manera simple y separada las vistas, las URLs, y los controladores de la lógica del negocio. Su manejo es muy sencillo, así que a continuación se hara la secuencia de instrucciones que permiten crear un proyecto en Django, y dentro de este proyecto una aplicación web para la creación de la Tienda Virtual.

Para crear un proyecto en Django, teniendo el entorno virtual activo y en la raíz de la carpeta del ejercicio, ejecute el siguiente comando:
django-admin startproject misiontic2020_ciclo1

Esto creará una carpeta llamada "misiontic_2020_ciclo1" puesto que es el nombre que se le dio al proyecto en Django. Dentro de esta carpeta se han auto-generado los archivos necesario para la gestión del proyecto: una carpeta con el mismo nombre del proyecto, y el archivo principal "manage.py".
Si usted quiere darle otro nombre a su proyecto, tendrá que cambiar la cadena de caracteres final de la instrucción utilizada. 

Es momento de utilizar algún IDE y agregar la carpeta del ejercicio, para así poder modificar el código del mismo de una manera más sencilla (no vaya a cerrar la ventana de terminal, la va a utilizar de nuevo más adelante). 
Estando en el explorador de archivos del IDE, usted deberá ver en la raíz del ejercicio la carpeta "mision2020_ciclo1"; por favor, expanda esa carpeta. Al expandir, verá el archivo manage.py, y una carpeta llamada de nuevo "mision2020_ciclo1",
Al expandir esta segunda carpeta, observara varios archivos de python:
"_ _init_ _".py = Define el contenido de la carpeta como un módulo de python
asgi.py = permite manejar el módulo como una variable de Django
settings.py = Configuraciones generales del proyecto en Django
urls.py = Listado de urls definidas para ser accedidas por el usuario en el MVC
wsgi.py = permite asociar la aplicación para ser lanzada automáticamente con el servidor Apache

Por favor, dirígase al archivo de settings.py, en donde deberá realizar los siguientes cambios para ejecutar por primera vez la aplicación:
1) Djando define desde que dirección de servidor puede ser ubicado. Como va a correr en la máquina local, le recomendamos que modifique la siguiente línea de código:
ALLOWED_HOSTS = ['localhost', '127.0.0.1]  # linea 28

2) Es bueno configurar la zona del mundo, para un buen manejo de datos que tengan que ver con fecha, hora, e idioma para el usuario. Para ello, modifique las siguientes líneas de código:
LANGUAGE_CODE = 'es-es'  # línea 106
TIME_ZONE = 'America/Bogota'   # línea 108

3) Django maneja temas como imágenes o código de JavaScript en la categoría de "static". Para asegurar que no se tiene problema accediendo a las rutas de estos elementos, agregue al final del archivo la siguiente línea de código.
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

4) Finalmente, importe el módulo "os" que le da acceso a python a algunas funcionalidades propias del sistema operativo (como la creación y acceso a carpetas dentro del sistema de archivos):
import os # línea 14

Ahora, es momemnto de probar que todo anda funcionando correctamente. Claro, no se ha agregado nada del desarrollo web, pero se puede validar que la creación y configuración del proyecto de Django. Para ello, debe regresar a la ventana de comandos ó terminal, y ubicarse en la carpeta raíz del proyecto. Allí, acceda a la carpera del proyecto de Django usando el siguiente comando:
cd misiontic_2020_ciclo1"

estando allí, ejecute la siguiente instrucción que colocará el proyecto disponible para acceder desde cualquier navegador web:
python manage.py runserver

Ahora, usando cualquier navegador coloque la dirección: http://localhost:8000, y allí vera una ventana con un cohete que le indicará que el proyecto en Django está bien construido hasta ahora.

Para continuar, por favor regrese a la ventana de comandos o terminal, y haga la siguiente secuencia de teclas: Ctrl + C.

Es momento de crear la aplicación web dentro del proyecto de Django. Es importante mencionar que en Django se pueden tener varias aplicaciones web, en el caso de que quiera trabajar un proyecto por componentes interconectados. Para nuestro ejercicio, solo se tendrá una aplicación web, la cual será la tienda virtual; para crearla, utilice la siguiente instrucción (debe mantenerse ubicado en la raíz del proyecto de Django, donde está el archivo de "manage.py"):
python manage.py startapp tienda_virtual

En nuestro la app se llama "tienda_virtual", si usted quiere darle otro nombre, debe cambiar el final de la instrucción utilizada anteriormente. Una vez se haya ejecturado esta instrucción, se creará una carpeta con el mismo nombre de la app, y tendrá los archivos fundamentales para el manejo del MVC en Django.

Adicionalmente, debe ir al archivo de "settings.py", ese mismo que modifico hace un par de pasos atrás, y en la lista de INSTALLED_APPS agregue el siguiente elemento:
'tienda_virtual', #línea 41

Listo, usted ha creado su primer proyecto de Django con una definición inicial de una aplicación web embebida en el mismo.


## Vistas Web de la Tienda Virtual 
Inicio
Lista de Productos
Ver Carrito (incluyendo editar cantidad y eliminar)
Pagar
Historial de Compras


## Formularios a Desarrollar 
Agregar producto a carrito
Pagar productos del carrito


## Colecciones en Mongo 
Productos
Compras