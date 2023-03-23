# PROYECTO GRAPHQL VS REST API

# Pasos de instalación

##### 1) Clonar el proyecto del repositorio

```bash
git clone https://github.com/wdavilav/Project_GRAPHQL_REST-API.git
```

##### 2) Crear un entorno virtual para posteriormente instalar las librerias del proyecto

Para windows:

```bash
python3 -m venv venv 
```

Para linux:

```bash
virtualenv venv -ppython3 
```

##### 3) Activar el entorno virtual de nuestro proyecto

Para windows:

```bash
cd venv\Scripts\activate.bat 
```

Para Linux:

```bash
source venv/bin/active
```

##### 4) Instalar todas las librerias del proyecto que se encuentran en la carpeta deploy

```bash
pip install -r requirements.txt
```

##### 5) Crear la base de datos con las migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

##### 6) Insertar información inicial en la base de datos 

```bash
- `python manage.py shell --command='from core.init import *'`
```