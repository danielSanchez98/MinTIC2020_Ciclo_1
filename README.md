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

Esto creará una carpeta llamada "misiontic_2020_ciclo1" puesto que es el nombre que se le dio al proyecto en Django. Dentro de esta carpeta se han auto-generado los archivos básicos de configuración del proyecto.
Si usted quiere darle otro nombre a su proyecto, tendrá que cambiar la cadena de caracteres final de la instrucción utilizada.

go to misiontic2020_ciclo1 folder, and open settings:
ALLOWED_HOSTS = ['localhost', '127.0.0.1]  # line 28

LANGUAGE_CODE = 'es-es'  # line 106
TIME_ZONE = 'America/Bogota'   # line 106

LAST-LINE
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

import os # line 14



Ahora, es necesario ingregar en dicha carpeta. Si lo está haciendo desde la terminar, puede usar la siguiente instr
cd misiontic2020_ciclo1
python manage.py runserver


create app
python manage.py startapp tienda_virtual

go to settings, in INSTALLED_APPS list add:
'tienda_virtual', line 41




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