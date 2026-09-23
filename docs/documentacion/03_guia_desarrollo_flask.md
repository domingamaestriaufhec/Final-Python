# 💻 03. Guía de Desarrollo y Buenas Prácticas con Flask

Esta guía describe el flujo de desarrollo diario, la gestión de entornos virtuales, las convenciones de código y el manejo adecuado de peticiones en Flask.

---

## 🐍 1. Flujo de Trabajo con el Entorno Virtual (`.venv`)

Para mantener el proyecto reproducible y aislado de otras aplicaciones de Python en el sistema operativo:

### Creación y Activación
* **Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```
* **macOS / Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### Instalación y Congelamiento de Dependencias
```bash
# Instalar dependencias exactas
pip install -r requirements.txt

# Si se agrega una nueva librería (ej. pytest):
pip install pytest
pip freeze > requirements.txt
```

---

## 🌐 2. Enrutamiento y Controladores en Flask

### Buenas Prácticas al Definir Rutas:
1. **Nombres Semánticos de Función:** El nombre de la función debe describir la acción o recurso (ej. `biblioteca_view()` o `levels()`).
2. **Uso de `url_for`:** Nunca escribir rutas URL hardcodeadas en plantillas; utilizar siempre `{{ url_for('main.index') }}` o `{{ url_for('static', filename='css/style.css') }}`.
3. **Manejo de Errores 404/500:** Siempre implementar manejadores de error con vistas personalizadas y código de estado HTTP explícito:

```python
@main_bp.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
```

---

## 🎨 3. Convenciones en Plantillas Jinja2

1. **Herencia de Plantillas:** Todas las vistas deben extender de `base.html`:
   ```jinja2
   {% extends "base.html" %}
   {% block title %}Título de la Vista{% endblock %}
   {% block content %}
     <!-- Contenido específico -->
   {% endblock %}
   ```
2. **Escape Automático:** Jinja2 aplica auto-escaping contra ataques XSS.
3. **Inyección Limpia de Contexto:** Pasar diccionarios o listas preparadas desde los controladores en lugar de computar lógica pesada dentro del HTML.

---

## 🧪 4. Pruebas Automatizadas con el Test Client de Flask

Flask incluye un cliente de pruebas que permite simular peticiones HTTP sin necesidad de levantar un servidor en un puerto real:

```python
# Ejemplo de test automatizado
from app import create_app

def test_routes_status_ok():
    app = create_app()
    client = app.test_client()
    
    rutas = ['/', '/niveles', '/biblioteca', '/pipeline', '/matriz']
    for ruta in rutas:
        response = client.get(ruta)
        assert response.status_code == 200, f"Fallo en {ruta}"
```
