# 🔬 InvestigaLab: Curso y Plataforma de Metodología de la Investigación Científica

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Flask 3.0](https://img.shields.io/badge/Framework-Flask_3.0-000000.svg?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Render Live](https://img.shields.io/badge/Render-Live_Deployment-46E3B7.svg?logo=render&logoColor=white)](https://investigalab-python.onrender.com)
[![Archify Pipeline](https://img.shields.io/badge/Architecture-Archify_Pipeline-6366f1.svg)](https://github.com/tt-a1i/archify.git)
[![IDE](https://img.shields.io/badge/Environment-Google_Antigravity-orange.svg)](#)

> Una aplicación web completa, interactiva y pedagógica desarrollada en **Python con Flask**, diseñada para guiar a estudiantes e investigadores desde sus primeros pasos hasta la publicación científica indexada en **5 niveles progresivos**.

---

## 🌐 Enlaces Oficiales de Entrega

* 🚀 **Despliegue Funcional en Vivo (Render):** [https://investigalab-python.onrender.com](https://investigalab-python.onrender.com)
* 🐙 **Repositorio Oficial en GitHub:** [https://github.com/domingamaestriaufhec/Final-Python](https://github.com/domingamaestriaufhec/Final-Python)
* 📓 **Cuaderno Jupyter con Modelos Matemáticos:** [`InvestigaLab_Metodologia_Cientifica.ipynb`](InvestigaLab_Metodologia_Cientifica.ipynb)
* 🎬 **Guión para el Video de Sustentación:** [`docs/presentacion_sustentacion.md`](docs/presentacion_sustentacion.md)
* 🛠️ **Entorno Agéntico de Desarrollo:** Google Antigravity IDE


---

## 🎯 1. ¿Qué es este proyecto y qué problema resuelve?

La **Metodología de la Investigación** suele enseñarse mediante manuales abstractos y densos, generando confusión al formular hipótesis, alinear objetivos o seleccionar pruebas estadísticas.

**InvestigaLab** resuelve este problema ofreciendo:
* Un mapa de ruta interactivo en **5 niveles de especialización**:
  1. **Principiante:** Curiosidad empírica, qué es la ciencia y formulación de la pregunta inicial.
  2. **Básico:** Búsqueda bibliográfica booleana, marco teórico, objetivos SMART e hipótesis ($H_0 / H_1$).
  3. **Intermedio:** Enfoques (cuanti/cuali/mixto), muestreo representativo y matriz de operacionalización de variables.
  4. **Avanzado:** Instrumentación (Alfa de Cronbach, V de Aiken), pruebas estadísticas (t-Student, ANOVA, Mann-Whitney) y triangulación.
  5. **Experto:** Redacción IMRyD, bioética, selección de revistas (Scopus/JCR) y respuesta a revisores (peer review).
* **Generador de Matriz de Consistencia Científica** en tiempo real con exportación a Markdown.
* **Pestaña interactiva de Pipeline & Arquitectura**, estructurada con las buenas prácticas del repositorio [Archify](https://github.com/tt-a1i/archify.git).

---

## 🏗️ 2. Arquitectura & Pipeline (Inspiración Archify)

La aplicación sigue una arquitectura limpia desacoplada:

```text
[Cliente / Navegador]
        │ (HTTP GET/POST)
        ▼
   [run.py] ───► [app/__init__.py (App Factory)]
                        │
                        ▼
                 [app/routes.py]
                 ┌──────┴──────┐
                 ▼             ▼
      [app/data/levels_data.py] [Jinja2 Templates: app/templates/]
                 │             │
                 └──────┬──────┘
                        ▼
              [Documento HTML5 + CSS/JS]
```

El diagrama de arquitectura completo se encuentra en [`docs/arquitectura.md`](docs/arquitectura.md) y [`docs/images/arquitectura.png`](docs/images/arquitectura.png).

---

## 📁 3. Estructura del Proyecto

```text
PYTHON/CURSOR/
├── index.html                  # Landing page raíz para GitHub Pages y navegación directa
├── .gitignore                  # Exclusión de entornos virtuales y temporales
├── requirements.txt            # Dependencias de Python (Flask, Jinja2, etc.)
├── README.md                   # Presentación y documentación general
├── run.py                      # Punto de entrada para ejecutar el servidor Flask
├── .agents/
│   └── skills/
│       └── flask-docs-architect/ # Skill especializada de arquitectura y documentación Flask
│           └── SKILL.md
├── app/
│   ├── __init__.py             # Factoría de la aplicación Flask
│   ├── routes.py               # Controladores y rutas web
│   ├── data/
│   │   ├── levels_data.py      # Datos pedagógicos de los 5 niveles científicos y quizzes
│   │   ├── books_data.py       # Catálogo de libros y autores clásicos de metodología
│   │   └── pipeline_data.py    # Datos del pipeline de arquitectura Archify
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css       # Estilos modernos, responsivos y modo oscuro
│   │   ├── js/
│   │   │   └── main.js         # Lógica interactiva (matriz, copiado, tabs, quizzes)
│   │   └── images/
│   │       ├── hero_scientific_vector.png
│   │       ├── pipeline_archify_art.png
│   │       └── matrix_consistency_art.png
│   └── templates/
│       ├── base.html           # Layout común (Navbar, Footer)
│       ├── index.html          # Landing page principal dentro de Flask
│       ├── levels.html         # Vista detallada de los 5 niveles del curso con quizzes
│       ├── books.html          # Vista de la Biblioteca de Autores y Libros Clásicos
│       ├── pipeline.html       # Pestaña interactiva de Pipeline Archify
│       ├── matriz.html         # Generador de Matriz de Consistencia Metodológica
│       └── 404.html            # Manejador visual de error 404
└── docs/
    ├── tutorial.md             # Guía paso a paso para principiantes
    ├── arquitectura.md         # Documentación detallada de arquitectura
    ├── images/
    │   └── arquitectura.png    # Imagen del diagrama de arquitectura
    └── documentacion/          # Manuales detallados de buenas prácticas con Flask
        ├── 01_arquitectura_y_patrones.md
        ├── 02_estructura_y_modulos.md
        ├── 03_guia_desarrollo_flask.md
        ├── 04_metodologia_cientifica_curriculo.md
        ├── 05_despliegue_y_produccion.md
        └── 06_pipeline_archify.md
```

---

## 🚀 4. Guía de Instalación y Ejecución Rápida

### 1. Clonar o abrir el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd <CARPETA_DEL_PROYECTO>
```

### 2. Crear y activar el entorno virtual
* **En Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```
* **En macOS / Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```bash
python run.py
```

### 5. Acceder en el navegador
Visita en tu navegador: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

Para más detalles, consulta la [Guía Paso a Paso en docs/tutorial.md](docs/tutorial.md).

---

## 🧠 5. Separación "Idea vs. Técnica"

Una de las ventajas clave de esta estructura es que la **Capa Técnica** y la **Capa de Idea** están 100% desacopladas:

| Capa | Componentes | Función |
|---|---|---|
| **Técnica** | Python, `.venv`, Flask, Rutas, Jinja2, CSS, Git | Infraestructura reutilizable para cualquier proyecto web. |
| **Idea** | `app/data/levels_data.py`, Textos pedagógicos | Contenido específico del curso de Metodología Científica. |

### 🔄 ¿Cómo transformar este proyecto a otra idea (ej. Sistema de Inventario)?
1. **Reemplaza la capa de datos:** Modifica `app/data/levels_data.py` por `app/data/inventory_data.py` (ej. Categorías, Productos, Stock).
2. **Actualiza las vistas:** En `app/templates/index.html` ajusta los títulos a "Sistema de Control de Stock".
3. **Mantén intacta toda la técnica:** El entorno `.venv`, las librerías, el enrutador de Flask y los estilos CSS funcionarán de inmediato sin reescribir la base del software.

---

## 📚 Documentación Adicional

* 📖 [Tutorial Paso a Paso para Principiantes](docs/tutorial.md)
* 🏗️ [Documentación de Arquitectura y Pipeline Archify](docs/arquitectura.md)
* 📊 [Diagrama Visual de Arquitectura](docs/images/arquitectura.png)
