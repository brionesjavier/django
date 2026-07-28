
## cargando libreria
```python
from myapp.models import Project, Task
```

## creando un objetos project
```python
p = Project(name = "aplicacion movil")
```

## revisando que muestra
```python
print(p) #  Project object 
```

## guardando en la base de datos

```python
p.save()
```

## creando otro oobjeto Project y lo guardamos
```python
p = Project(name = "aplicacion web usando django")
p.save()
```

## obteniendo todo los objetos de la bd del objeto Project

```python
Project.objects.all()   # <QuerySet [<Project: Project object (1)>, <Project: Project object (2)>]>
```

## obteniendo un objeto  objeto  project por id
```python
Project.objects.get(id=1) # <Project: Project object (1)>
```

## obteniendo un objeto project por campo name

```python
Project.objects.get(name = "aplicacion movil") # <Project: Project object (1)>

```

## obteniendo el objeto project y guardandolo en una variable

```python
p = Project.objects.get(id=1)
```
## obteniendo las tareas que estan asociada en project como estaba en el modelo

```python
p.task_set.all() # <QuerySet []>
```

## creando una tarea en proyecto

```python
p.task_set.create(title="descargar IDE") # <Task: Task object (1)>
p.task_set.create(title="desarrollar login") # <Task: Task object (2)>
```
## viendo todas las tarea asociadas

```python
p.task_set.all() # <QuerySet [<Task: Task object (1)>, <Task: Task object (2)>]>
```
## obteniendo una tarea
da error si no encuentra el objeto
```python
p.task_set.get(id=1) # <Task: Task object (1)>
```
## buscar por medio del filtro
```python
Project.objects.filter(name__startswith="aplicacion") 
# <QuerySet [<Project: Project object (1)>, <Project: Project object (2)>]>
```

