# django.http 
## from django.http import HttpResponse

### 1. Enviar HTML directo (como en tu ejemplo)
```python
from django.http import HttpResponse


def hello(request):
    return HttpResponse("<h2>Hello world</h2>")

```

### 2. Cambiar el tipo de contenido (content_type)
```python
from django.http import HttpResponse


def plain_text(request):
    # El navegador mostrará "<h2>Hello world</h2>" con las etiquetas visibles, sin procesar HTML
    return HttpResponse(
        "<h2>Hello world</h2>", content_type="text/plain"
    )

```
### 3. Pasar estados HTTP personalizados
```python
from django.http import HttpResponse

def error_custom(request):
    return HttpResponse("Recurso no encontrado", status=404)

```


---

## from django.http import JsonResponse
### Opción 1: Extraer solo los campos que necesitas con .values() (La más rápida)
```python
from django.http import JsonResponse
from myapp.models import Project


def projects(request):
    # .values() convierte cada objeto en un diccionario: [{'id': 1, 'name': 'Proy 1'}, ...]
    projects = list(Project.objects.values())

    # Como 'projects' es una LISTA y no un diccionario, requerimos safe=False
    return JsonResponse(projects, safe=False)

```
### Opción 2: Sin usar safe=False (Encapsulando la lista en un diccionario)
```python
from django.http import JsonResponse
from myapp.models import Project


def projects(request):
    projects_data = list(Project.objects.values())

    # Al ser un diccionario con la clave 'projects', ya NO necesitas safe=False
    return JsonResponse({'projects': projects_data})
```

### Opción 3: Usar el serializador nativo de Django
```python
from django.core.serializers import serialize
from django.http import HttpResponse
from myapp.models import Project


def projects(request):
    projects_qs = Project.objects.all()
    # serialize() convierte el QuerySet directamente a una cadena de texto en formato JSON
    data = serialize('json', projects_qs)

    # Retornamos HttpResponse indicando el tipo de contenido (mimetype)
    return HttpResponse(data, content_type='application/json')
```
---

## from django.shortcuts import get_object_or_404

```python
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from myapp.models import Task


def tasks(request, id):
    # Obtienes la instancia de Task
    task = get_object_or_404(Task, id=id)

    # Armas un diccionario con los datos que quieres enviar
    data = {
        'id': task.id,
        'title': task.title,
        'completed': task.completed,
    }

    # Como 'data' es un diccionario, JsonResponse lo acepta directamente
    return JsonResponse(data)
```




## from django.forms.models import model_to_dict
```python
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from myapp.models import Task


def tasks(request, id):
    task = get_object_or_404(Task, id=id)

    # Convierte el objeto 'task' a un diccionario de Python de un solo paso
    data = model_to_dict(task)

    return JsonResponse(data)
```