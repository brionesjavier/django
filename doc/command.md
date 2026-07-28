#  preparando entorno de desarrollo

## instalando libreria de virtualenv  para trabajar en entorno separados 
```cmd
pip install virtualenv
```

otros metodos
```shell
<!-- instalando por medio del sistema -->
sudo apt-get install python3-virtualenv
sudo apt-get install python3-venv

<!-- por medio del modulo de pip -->
sudo python -m pip install virtualenv 

```
## creando entorno virtual

### virtualenv
```shell
virtualenv venv
```
### venv
```shell
python -m venv venv
```
## activando/desactivando el entorno de desarrollo

### activando el entorno de desarrollo
```shell
source venv/bin/activate
```
### desactivando el entorno de desarrollo

```shell
deactivate
```
# instalacion de la libreria de django
```shell
pip install django
```
# creando proyecto
crea la carpeta del proyecto y la carpeta de configuracion con el mismo nombre
```shell
django-admin  startproject mysite
```

se ocupa por defecto la carpeta que esta para proyecto y se crea la carpeta de configuracion como mysite en este ejemplo

```shell
django-admin startproject mysite .
```

crea la carpeta de configuacion  y la carpeta del proyecto
```shell
django-admin startproject mysite djangoproject 

```


# prerarando git 
## revisamos que git se encuentre instalado
```shell
git --version
```
## instalando git si no se encuentra
```
sudo apt-get install git
```

## inicializamos  el proyecto
```
git init
```
## creamos el archivo .gitignore
```shell
touch .gitignore
```

### agregamos por defectos esta configuracioon
```
<!--  -->
.vscode
.env

venv/

```
## agregamos los  archivo al stage
```
git add .
```

## agregamos una descripcion al commit
```
git commit -m "primer commit"
```

# corriendo servidor desarrollo

```
python manage.py runserver 
```

```
python manage.py runserver 8080
```

# creamos una app en el proyecto

```
python manage.py startapp myapp
```