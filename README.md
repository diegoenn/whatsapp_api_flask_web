# whatsapp_api_flask_web
Este es un proyecto basado en la documentacion de developers de meta
en el cual se pueden enviar mensajes de whatsapp a trave del API de whatsapp
y se crea una aplicacion web en el cual por cada click que se hace se envia un mensaje a traves de whatsapp
link de documentacion oficial de meta
https://developers.facebook.com/blog/post/2022/10/24/sending-messages-with-whatsapp-in-your-python-applications/
para iniciar la aplicacion se debe correr este comando en la terminal
## flask run

# ####################################################################

## primeros pasos para activar el entorno virtual de python

para validar las versiones de python instaladas en el equipo
py --list
para validar el interprete que se esta usando
python3 --version
python --version

abrir consola en una terminal cmd o en la terminal de visual studio code
comando para ingresar a una carpeta en en computador llamada myproject
cd myproject
comando para validar la version de python
python3 --version
comando para instalar pip usando homebrew
python3 -m ensurepip
comando para validar la version de pip framework en python
pip3 --version en mac or pip --version en windows

# ####################################################################
## crear, habilitar y sincronizar el repositorio de git

### clonar el repositorio desde github a local se hace con 
git clone url_repositorio_remoto

### configura nombre y correo de la cuenta git
git config --global user.name "Diego"
git config --global user.email "diegoenn@gmail.com"

### luego dentro de la carpeta del proyecto iniciar un repositorio git
git init

### para hacer commits usar los siguientes comandos
git status
git branch
git checkout nombre_branch
git add .
git commit -m "mensaje del commit"
git push origin nombre_branch

### agrega un repositorio remoto de github a la consola local, debe hacerse dentro de la carpeta local
git remote add origin url_rositorio_github
git remote -v
git log



# ####################################################################
## crear un entorno virtual

comando para crear un entorno virtual dentro de la carpeta del proyecto
python3 -m venv env
o si se quiere configurar con una version especifica de python en el entorno virtual usar el siguiente comando
py -3.11 -m venv venv

comando para activar un entorno virtual dentro de la carpeta del proyecto
source env/bin/activate en mac or env/scripts/activate en windows
comando para desactivar un env virtual
deactivate
comando para listar librerias instaladas en python dentro del entorno
pip list en windows or pip3 list en mac
como saber en que ruta o entorno virtual estoy?
mirando la ruta y el nombre del entorno que aparece en parentesis

# ############################################################################
## instalando paquetes

comando para instalar flask
pip install flask[async] en windows or pip install flask async en mac pip install "Flask[async]"
comando para correr flask
flash run
comando para instalar aiohttp libreria para manejo de comunicaciones asyncronas como whatsapp
pip install aiohttp[speedups] en windows or pip install aiohttp en mac
comando para instalar psycopg2 que sirve para conectarse a db postgress
pip install psycopg2 en windows or pip install psycopg2-binary en mac
comando para instalar libreria para poder manejar variables globales en python
pip install python-dotenv

par instalar todas los paquetes requeridos desde el archivo requirements.txt lanzar el siguiente comando
para ello se debe tener el listado de paquetes escrito en ese archivo
`pip install -r requirements.txt`

# ############################################################################
## instalacion de base de datos

instalacion de db postgresql
descargar postgresql version 16 extension dmg de edb o superior de postgresql.org son como 360 megas
instalar la db en la laptop siguiendo el wizard
instalamos los 4 componentes (postgresql server, pgadmin, stack builder, command line tools)
default database name: postgres
pwd database: mondi 
port: 5432
al final de la instalacion unselect el checkbox de stack builder
despues de la instalacion aparecen 3 iconos(pgadmin, sql shell (psql) y psql 16)

# #############################################################
