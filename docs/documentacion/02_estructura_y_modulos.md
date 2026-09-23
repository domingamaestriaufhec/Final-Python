# 📁 02. Estructura del Proyecto y Responsabilidad de Módulos

Este documento describe la jerarquía del árbol de directorios de **InvestigaLab** y la responsabilidad única (*Single Responsibility Principle*) asignada a cada archivo.

---

## 🌳 Árbol Completo del Directorio

```text
PYTHON/CURSOR/
├── index.html                      # Landing Page raíz para GitHub Pages / navegación directa
├── run.py                          # Punto de entrada para el servidor Flask
├── requirements.txt                # Manifiesto oficial de dependencias de Python
├── .gitignore                      # Exclusiones de Git (entornos .venv, cachés, logs)
├── README.md                       # Documentación principal con badges y guía de inicio
│
├── .agents/
│   └── skills/
│       └── flask-docs-architect/   # Skill instalada de arquitectura y documentación Flask
│           └── SKILL.md
│
├── app/                            # Paquete principal de la aplicación Flask
│   ├── __init__.py                 # Factoría de la aplicación (create_app)
│   ├── routes.py                   # Enrutamiento, controladores y vistas web
│   │
│   ├── data/                       # Repositorio desacoplado de datos (Capa de Dominio)
│   │   ├── levels_data.py          # Currículo de los 5 niveles científicos y cuestionarios
│   │   ├── books_data.py           # Catálogo de libros y autores clásicos de metodología
│   │   └── pipeline_data.py        # Datos de arquitectura y pipeline estilo Archify
│   │
│   ├── static/                     # Recursos estáticos entregados al cliente
│   │   ├── css/
│   │   │   └── style.css           # Hoja de estilos con variables HSL, Dark Mode y Glassmorphism
│   │   ├── js/
│   │   │   └── main.js             # Interactividad (constructor de matriz, tabs, copiado)
│   │   └── images/                 # Ilustraciones vectoriales de alta resolución
│   │       ├── hero_scientific_vector.png
│   │       ├── pipeline_archify_art.png
│   │       └── matrix_consistency_art.png
│   │
│   └── templates/                  # Plantillas renderizadas con el motor Jinja2
│       ├── base.html               # Layout maestro (Navbar, Header, Footer)
│       ├── index.html              # Vista de la Landing Page dentro de Flask
│       ├── levels.html             # Vista del currículo interactivo de 5 niveles
│       ├── books.html              # Vista de la Biblioteca de Libros y Autores
│       ├── pipeline.html           # Vista de Arquitectura y Pipeline Archify
│       ├── matriz.html             # Herramienta interactiva de Matriz de Consistencia
│       └── 404.html                # Manejador visual de error 404
│
└── docs/                           # Documentación técnica y pedagógica
    ├── tutorial.md                 # Guía paso a paso para principiantes
    ├── arquitectura.md             # Especificación técnica del sistema
    ├── images/
    │   └── arquitectura.png        # Diagrama de arquitectura del software
    └── documentacion/              # Manuales detallados de buenas prácticas Flask
        ├── 01_arquitectura_y_patrones.md
        ├── 02_estructura_y_modulos.md
        ├── 03_guia_desarrollo_flask.md
        ├── 04_metodologia_cientifica_curriculo.md
        ├── 05_despliegue_y_produccion.md
        └── 06_pipeline_archify.md
```

---

## 🎯 Matriz de Responsabilidades

| Módulo / Archivo | Rol Principal | Dependencias Clave |
|---|---|---|
| `run.py` | Entrada de ejecución y configuración de consola UTF-8 | `app.create_app` |
| `app/__init__.py` | Configuración de la instancia Flask y registro de Blueprints | `flask.Flask` |
| `app/routes.py` | Mapeo de URLs a funciones controladoras | `flask.Blueprint`, `render_template` |
| `app/data/levels_data.py` | Suministro inmutable del currículo de 5 niveles | *Ninguna (Python Puro)* |
| `app/data/books_data.py` | Catálogo epistemológico de autores y capítulos recomendados | *Ninguna (Python Puro)* |
| `app/data/pipeline_data.py` | Especificación de fases y componentes de Archify | *Ninguna (Python Puro)* |
| `app/static/css/style.css` | Sistema de diseño visual y responsivo | CSS3 Moderno |
| `app/static/js/main.js` | Lógica de interactividad del navegador | JavaScript Vanilla (ES6+) |
