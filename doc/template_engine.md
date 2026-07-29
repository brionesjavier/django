# Django Template Engine - Guía Completa

## Introducción

El Template Engine de Django es un motor de plantillas potente que permite separar la lógica de presentación de la lógica de negocio. Proporciona una sintaxis segura y flexible para renderizar HTML dinámico.

https://jinja.palletsprojects.com/en/stable/templates/
jinja loop
---

## 1. Configuración Básica

### Configurar Django para usar templates

En `settings.py`:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### Estructura de carpetas recomendada

```
proyecto/
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── includes/
│   │   ├── navbar.html
│   │   └── footer.html
│   └── products/
│       └── list.html
└── manage.py
```

---

## 2. Variables y Expresiones Básicas

### Caso 1: Mostrar variables simples

**views.py:**
```python
from django.shortcuts import render

def home(request):
    contexto = {
        'nombre': 'Juan',
        'apellido': 'Pérez',
        'edad': 30,
    }
    return render(request, 'home.html', contexto)
```

**home.html:**
```html
<h1>Hola, {{ nombre }} {{ apellido }}</h1>
<p>Tienes {{ edad }} años</p>
```

**Salida:**
```html
<h1>Hola, Juan Pérez</h1>
<p>Tienes 30 años</p>
```

### Caso 2: Acceder a atributos de objetos

**views.py:**
```python
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

def perfil(request):
    usuario = Usuario('Maria', 'maria@example.com')
    return render(request, 'perfil.html', {'usuario': usuario})
```

**perfil.html:**
```html
<h1>{{ usuario.nombre }}</h1>
<p>Email: {{ usuario.email }}</p>
```

### Caso 3: Acceder a diccionarios

**views.py:**
```python
def datos(request):
    producto = {
        'nombre': 'Laptop',
        'precio': 999.99,
        'disponible': True
    }
    return render(request, 'producto.html', {'producto': producto})
```

**producto.html:**
```html
<h2>{{ producto.nombre }}</h2>
<p>Precio: ${{ producto.precio }}</p>
<p>Disponible: {{ producto.disponible }}</p>
```

---

## 3. Filters (Filtros)

Los filtros modifican variables en el template.

### Caso 1: Filtros de string

```html
<!-- UPPERCASE: convierte a mayúsculas -->
<h1>{{ titulo|upper }}</h1>

<!-- LOWERCASE: convierte a minúsculas -->
<p>{{ email|lower }}</p>

<!-- TITLE: primera letra mayúscula de cada palabra -->
<h2>{{ nombre|title }}</h2>

<!-- SLUGIFY: convierte a slug (para URLs) -->
<a href="/posts/{{ titulo|slugify }}/">Ver post</a>

<!-- TRUNCATEWORDS: corta después de N palabras -->
<p>{{ descripcion|truncatewords:10 }}</p>

<!-- LENGTH: obtiene la longitud -->
<p>Caracteres: {{ texto|length }}</p>
```

### Caso 2: Filtros de números y fechas

```html
<!-- FLOATFORMAT: formatea decimales -->
<p>Precio: ${{ precio|floatformat:2 }}</p>

<!-- DATE: formatea fechas -->
<p>Publicado: {{ fecha|date:"d/m/Y" }}</p>

<!-- TIME: formatea horas -->
<p>Hora: {{ hora|time:"H:i" }}</p>

<!-- ADD: suma un número -->
<p>Total: {{ cantidad|add:5 }}</p>

<!-- PLURALIZE: singularización/pluralización -->
<p>Tienes {{ total }} comentario{{ total|pluralize }}</p>
```

### Caso 3: Filtros condicionales

```html
<!-- DEFAULT: valor por defecto si está vacío -->
<p>{{ nombre|default:"Usuario Anónimo" }}</p>

<!-- DEFAULT_IF_NONE: solo si es None -->
<p>{{ valor|default_if_none:"No especificado" }}</p>
```

### Caso 4: Filtros encadenados

```html
<!-- Se pueden encadenar múltiples filtros -->
<h1>{{ titulo|lower|title|truncatewords:5 }}</h1>
```

---

## 4. Control de Flujo

### Caso 1: Condicionales IF/ELIF/ELSE

**views.py:**
```python
def estado_producto(request):
    contexto = {
        'stock': 5,
        'precio': 100,
        'usuario_premium': True,
    }
    return render(request, 'estado.html', contexto)
```

**estado.html:**
```html
{% if stock > 0 %}
    <p style="color: green;">Producto disponible</p>
{% elif stock == 0 %}
    <p style="color: red;">Agotado</p>
{% else %}
    <p>Estado desconocido</p>
{% endif %}

<!-- Condiciones múltiples -->
{% if usuario_premium and precio < 50 %}
    <p>¡Oferta especial para miembros premium!</p>
{% endif %}

<!-- Negar una condición -->
{% if not stock %}
    <p>Sin stock</p>
{% endif %}
```

### Caso 2: Bucles FOR

**views.py:**
```python
def lista_productos(request):
    productos = [
        {'nombre': 'Laptop', 'precio': 1000},
        {'nombre': 'Mouse', 'precio': 30},
        {'nombre': 'Teclado', 'precio': 80},
    ]
    return render(request, 'productos.html', {'productos': productos})
```

**productos.html:**
```html
<ul>
{% for producto in productos %}
    <li>
        {{ producto.nombre }} - ${{ producto.precio }}
    </li>
{% empty %}
    <li>No hay productos disponibles</li>
{% endfor %}
</ul>

<!-- Acceso a variables del bucle -->
<table>
{% for producto in productos %}
    <tr class="{% if forloop.counter|divisibleby:2 %}par{% else %}impar{% endif %}">
        <td>{{ forloop.counter }}</td>
        <td>{{ producto.nombre }}</td>
        <td>
            {% if forloop.first %}
                <span>Primer producto</span>
            {% elif forloop.last %}
                <span>Último producto</span>
            {% endif %}
        </td>
    </tr>
{% endfor %}
</table>
```

**Variables disponibles en bucles:**
- `forloop.counter`: posición actual (comienza en 1)
- `forloop.counter0`: posición actual (comienza en 0)
- `forloop.first`: True si es el primer elemento
- `forloop.last`: True si es el último elemento
- `forloop.length`: total de elementos

---

## 5. Herencia de Templates

### Caso 1: Template base

**templates/base.html:**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block titulo %}Mi Sitio{% endblock %}</title>
    <style>
        {% block estilos %}{% endblock %}
    </style>
</head>
<body>
    <header>
        <h1>Mi Sitio Web</h1>
        {% block navbar %}
            <nav>
                <a href="/">Inicio</a>
                <a href="/productos/">Productos</a>
                <a href="/contacto/">Contacto</a>
            </nav>
        {% endblock %}
    </header>

    <main>
        {% block contenido %}{% endblock %}
    </main>

    <footer>
        <p>&copy; 2024 Mi Sitio. Todos los derechos reservados.</p>
        {% block footer %}{% endblock %}
    </footer>
</body>
</html>
```

### Caso 2: Extender el template base

**templates/home.html:**
```html
{% extends "base.html" %}

{% block titulo %}Inicio - Mi Sitio{% endblock %}

{% block estilos %}
    <style>
        .banner { background: blue; color: white; padding: 20px; }
    </style>
{% endblock %}

{% block contenido %}
    <div class="banner">
        <h2>Bienvenido a nuestro sitio</h2>
        <p>{{ mensaje }}</p>
    </div>
{% endblock %}
```

### Caso 3: Herencia multinivel

**templates/admin/base.html:**
```html
{% extends "base.html" %}

{% block titulo %}Panel Admin - Mi Sitio{% endblock %}

{% block navbar %}
    <nav class="admin-nav">
        <a href="/admin/">Dashboard</a>
        <a href="/admin/usuarios/">Usuarios</a>
        <a href="/admin/productos/">Productos</a>
    </nav>
{% endblock %}
```

**templates/admin/usuarios.html:**
```html
{% extends "admin/base.html" %}

{% block titulo %}Gestión de Usuarios - Admin{% endblock %}

{% block contenido %}
    <h2>Usuarios registrados</h2>
    <table>
        {% for usuario in usuarios %}
            <tr>
                <td>{{ usuario.nombre }}</td>
                <td>{{ usuario.email }}</td>
            </tr>
        {% endfor %}
    </table>
{% endblock %}
```

---

## 6. Inclusión de Templates (include)

### Caso 1: Reutilizar componentes

**templates/includes/card.html:**
```html
<div class="card">
    <img src="{{ imagen }}" alt="{{ titulo }}">
    <h3>{{ titulo }}</h3>
    <p>{{ descripcion }}</p>
    <a href="{{ enlace }}">Leer más</a>
</div>
```

**templates/index.html:**
```html
{% extends "base.html" %}

{% block contenido %}
    <div class="cards-container">
        {% for articulo in articulos %}
            {% include "includes/card.html" with imagen=articulo.imagen titulo=articulo.titulo descripcion=articulo.descripcion enlace=articulo.url %}
        {% endfor %}
    </div>
{% endblock %}
```

### Caso 2: Include con variables

**templates/includes/pagination.html:**
```html
<div class="pagination">
    {% if pagina.has_previous %}
        <a href="?page=1">Primera</a>
        <a href="?page={{ pagina.previous_page_number }}">Anterior</a>
    {% endif %}

    <span>Página {{ pagina.number }} de {{ pagina.paginator.num_pages }}</span>

    {% if pagina.has_next %}
        <a href="?page={{ pagina.next_page_number }}">Siguiente</a>
        <a href="?page={{ pagina.paginator.num_pages }}">Última</a>
    {% endif %}
</div>
```

**views.py:**
```python
from django.core.paginator import Paginator

def lista_articulos(request):
    articulos = Articulo.objects.all()
    paginator = Paginator(articulos, 10)
    numero_pagina = request.GET.get('page', 1)
    pagina = paginator.get_page(numero_pagina)
    
    return render(request, 'articulos.html', {'pagina': pagina})
```

**templates/articulos.html:**
```html
{% extends "base.html" %}

{% block contenido %}
    {% for articulo in pagina %}
        <article>
            <h2>{{ articulo.titulo }}</h2>
            <p>{{ articulo.contenido|truncatewords:30 }}</p>
        </article>
    {% endfor %}
    
    {% include "includes/pagination.html" with pagina=pagina %}
{% endblock %}
```

---

## 7. Template Tags Personalizados

### Caso 1: Simple tag

**miapp/templatetags/misotags.py:**
```python
from django import template

register = template.Library()

@register.simple_tag
def precio_con_iva(precio, iva=0.21):
    """Calcula el precio con IVA"""
    return round(precio * (1 + iva), 2)

@register.simple_tag
def saludo(nombre):
    """Genera un saludo personalizado"""
    return f"¡Hola, {nombre}!"
```

**En el template:**
```html
{% load misotags %}

<p>Precio: ${{ precio }}</p>
<p>Con IVA: ${% precio_con_iva precio iva=0.19 %}</p>
<p>{{ saludo usuario.nombre }}</p>
```

### Caso 2: Filter personalizado

**miapp/templatetags/misotags.py:**
```python
@register.filter
def es_par(numero):
    """Retorna True si el número es par"""
    return numero % 2 == 0

@register.filter
def formato_dinero(cantidad, moneda='USD'):
    """Formatea cantidad como moneda"""
    simbolos = {'USD': '$', 'EUR': '€', 'CLP': '$'}
    simbolo = simbolos.get(moneda, moneda)
    return f"{simbolo} {cantidad:,.2f}"
```

**En el template:**
```html
{% load misotags %}

<p>{{ numero|es_par }}</p>
<p>{{ 1000.50|formato_dinero:"CLP" }}</p>
```

---

## 8. Casos de Uso Avanzados

### Caso 1: Blog con comentarios

**templates/blog/post.html:**
```html
{% extends "base.html" %}

{% block titulo %}{{ post.titulo }}{% endblock %}

{% block contenido %}
    <article class="post">
        <h1>{{ post.titulo }}</h1>
        <small>Por {{ post.autor }} - {{ post.fecha|date:"d/m/Y H:i" }}</small>
        
        <div class="contenido">
            {{ post.contenido }}
        </div>

        {% if post.tags.all %}
            <div class="tags">
                <strong>Tags:</strong>
                {% for tag in post.tags.all %}
                    <a href="/tags/{{ tag.slug }}/">#{{ tag.nombre }}</a>
                {% endfor %}
            </div>
        {% endif %}
    </article>

    <!-- Sección de comentarios -->
    <section class="comentarios">
        <h2>Comentarios ({{ post.comentarios.count }})</h2>
        
        {% for comentario in post.comentarios.all %}
            <div class="comentario">
                <strong>{{ comentario.autor }}</strong>
                <small>{{ comentario.fecha|date:"d/m/Y" }}</small>
                <p>{{ comentario.texto }}</p>
            </div>
        {% empty %}
            <p>No hay comentarios aún.</p>
        {% endfor %}
    </section>
{% endblock %}
```

### Caso 2: Dashboard con usuario autenticado

**templates/dashboard.html:**
```html
{% extends "base.html" %}

{% block titulo %}Mi Dashboard{% endblock %}

{% block contenido %}
    {% if user.is_authenticated %}
        <h1>Bienvenido, {{ user.first_name|default:user.username }}!</h1>
        
        <div class="resumen">
            <div class="card">
                <h3>Mis Pedidos</h3>
                <p class="numero">{{ user.pedidos.count }}</p>
            </div>
            
            <div class="card">
                <h3>Total Gastado</h3>
                <p class="numero">
                    ${% for pedido in user.pedidos.all %}
                        {{ pedido.total|add:0 }}
                    {% endfor %}
                </p>
            </div>
        </div>

        {% if user.is_staff %}
            <div class="admin-panel">
                <h2>Panel de Administración</h2>
                <a href="/admin/">Ir a admin</a>
            </div>
        {% endif %}
    {% else %}
        <p>Por favor <a href="/login/">inicia sesión</a></p>
    {% endif %}
{% endblock %}
```

### Caso 3: Formulario dinámico

**views.py:**
```python
from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Procesar formulario
            pass
    else:
        form = ContactoForm()
    
    return render(request, 'contacto.html', {'form': form})
```

**templates/contacto.html:**
```html
{% extends "base.html" %}

{% block contenido %}
    <h1>Contacto</h1>
    
    <form method="post">
        {% csrf_token %}
        
        <div class="formulario">
            {% for field in form %}
                <div class="campo">
                    {{ field.label_tag }}
                    {{ field }}
                    {% if field.errors %}
                        <div class="errores">
                            {{ field.errors }}
                        </div>
                    {% endif %}
                </div>
            {% endfor %}
        </div>
        
        <button type="submit">Enviar</button>
    </form>
{% endblock %}
```

---

## 9. Buenas Prácticas

1. **Mantén la lógica en views**: Los templates no deben contener lógica compleja.
2. **Usa herencia**: Crea templates base para evitar repetición.
3. **Organiza tus templates**: Crea carpetas por aplicación o funcionalidad.
4. **Usa includes**: Para componentes reutilizables.
5. **Comenta tus templates**: Especialmente los bloques complejos.
6. **Valida en templates**: Verifica que los datos existan antes de acceder.
7. **Usa filtros**: Aprovecha los filtros built-in de Django.

---

## 10. Resumen de Sintaxis Útil

| Sintaxis | Uso |
|----------|-----|
| `{{ variable }}` | Mostrar variable |
| `{% if condicion %}...{% endif %}` | Condicional |
| `{% for item in lista %}...{% endfor %}` | Bucle |
| `{% extends "template.html" %}` | Heredar template |
| `{% block nombre %}...{% endblock %}` | Definir bloque |
| `{% include "template.html" %}` | Incluir template |
| `{{ variable\|filtro }}` | Aplicar filtro |
| `{% load mistagtags %}` | Cargar tags personalizados |
| `{% csrf_token %}` | Token CSRF en formularios |
| `{% url 'nombre-vista' %}` | Generar URL |

---

¡Ahora estás listo para dominar Django Template Engine! 🚀