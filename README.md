# 🔬 InvestigaLab: Curso y Plataforma de Metodología de la Investigación Científica

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Flask 3.0](https://img.shields.io/badge/Framework-Flask_3.0-000000.svg?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Render Live](https://img.shields.io/badge/Render-Live_Deployment-46E3B7.svg?logo=render&logoColor=white)](https://investigalab-python.onrender.com)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717.svg?logo=github&logoColor=white)](https://github.com/domingamaestriaufhec/Final-Python)
[![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-Static_App-22c55e.svg?logo=github&logoColor=white)](https://domingamaestriaufhec.github.io/Final-Python/)
[![IDE](https://img.shields.io/badge/Environment-Google_Antigravity-orange.svg)](#)

> Una aplicación web completa, interactiva y pedagógica desarrollada en **Python con Flask**, diseñada para guiar a estudiantes e investigadores desde sus primeros pasos hasta la publicación científica indexada en **5 niveles progresivos**.

---

## 🌐 Enlaces Oficiales del Proyecto

| Recurso | Enlace Directo | Descripción |
| :--- | :--- | :--- |
| 🚀 **Aplicación en Vivo (Render)** | [https://investigalab-python.onrender.com](https://investigalab-python.onrender.com) | Despliegue funcional en producción con backend Flask |
| 🐙 **Repositorio Oficial en GitHub** | [https://github.com/domingamaestriaufhec/Final-Python](https://github.com/domingamaestriaufhec/Final-Python) | Código fuente completo, módulos y datos |
| 📄 **GitHub Pages (Versión Estática)** | [https://domingamaestriaufhec.github.io/Final-Python/](https://domingamaestriaufhec.github.io/Final-Python/) | Landing page interactiva standalone |
| 🎬 **Guión para Video de Sustentación** | [`docs/presentacion_sustentacion.md`](docs/presentacion_sustentacion.md) | Estructura y guión paso a paso de 5 a 8 minutos |
| 📓 **Cuaderno Jupyter con Modelos** | [`InvestigaLab_Metodologia_Cientifica.ipynb`](InvestigaLab_Metodologia_Cientifica.ipynb) | Modelos matemáticos (Muestreo, Cronbach, Cohen) |
| 📖 **Tutorial Paso a Paso (Principiantes)** | [`docs/tutorial.md`](docs/tutorial.md) | Guía de instalación y ejecución local desde cero |
| 📑 **Documento Oficial de Entrega (.docx)** | [`Documento_Entrega_y_Sustentacion_InvestigaLab.docx`](Documento_Entrega_y_Sustentacion_InvestigaLab.docx) | Informe formal académico para la maestría |
| 🤖 **Evidencia de Google Antigravity** | [`docs/evidencia_antigravity.md`](docs/evidencia_antigravity.md) | Registro del desarrollo agéntico asistido por IA |
| 🏛️ **Arquitectura del Sistema** | [`docs/arquitectura.md`](docs/arquitectura.md) | Diagrama modular y desacoplamiento de capas |

---

## 🎯 1. ¿Qué es este proyecto y qué problema resuelve?

La **Metodología de la Investigación** suele enseñarse mediante manuales abstractos y densos, generando confusión al formular hipótesis, alinear objetivos o seleccionar pruebas estadísticas.

**InvestigaLab** resuelve este problema ofreciendo:
* Un mapa de ruta interactivo en **5 niveles de especialización**:
  1. **Nivel 1 • Principiante:** Fundamentos epistemológicos (Karl Popper, Mario Bunge) y delimitación del problema con Sampieri.
  2. **Nivel 2 • Básico:** Búsqueda bibliográfica booleana (Scopus/SciELO), marco teórico en embudo, objetivos SMART e hipótesis ($H_0 / H_1$).
  3. **Nivel 3 • Intermedio:** Enfoques (cuanti/cuali/mixto), principio MAXMINCON de Kerlinger, fórmulas de cálculo muestral ($n$) y matriz de operacionalización de variables.
  4. **Nivel 4 • Avanzado:** Instrumentación psicométrica (Alfa de Cronbach $\alpha$, V de Aiken), árbol de decisión de normalidad (Shapiro-Wilk vs Kolmogorov-Smirnov) y tamaño del efecto ($d$ de Cohen).
  5. **Nivel 5 • Experto:** Redacción científica IMRyD, bioética institucional (Belmont/Helsinki), directrices COPE sobre IA, selección de revistas indexadas (Q1-Q4) y cartas de réplica (*Rebuttal letters*).
* **Generador de Matriz de Consistencia Científica** en tiempo real con validación y exportación a Markdown.
* **Biblioteca Canónica de Autores & Obras**, con fundamentación directa en Bunge, Popper, Sampieri, Kerlinger y Creswell.
* **Materiales, Plantillas y Fichas Descargables/Copiables** en cada uno de los 5 niveles del curso.

---

## 🏗️ 2. Arquitectura del Sistema

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
├── Procfile                    # Comando de inicio para despliegue en Render
├── InvestigaLab_Metodologia_Cientifica.ipynb # Cuaderno Jupyter interactivo
├── Documento_Entrega_y_Sustentacion_InvestigaLab.docx # Documento formal de entrega
├── .agents/
│   └── skills/
│       └── flask-docs-architect/ # Skill especializada de arquitectura y documentación Flask
│           └── SKILL.md
├── app/
│   ├── __init__.py             # Factoría de la aplicación Flask
│   ├── routes.py               # Controladores y rutas web
│   ├── data/
│   │   ├── levels_data.py      # Datos pedagógicos de los 5 niveles científicos, recursos y quizzes
│   │   └── books_data.py       # Catálogo de libros y autores clásicos de metodología
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css       # Estilos modernos, responsivos y modo oscuro
│   │   ├── js/
│   │   │   └── main.js         # Lógica interactiva (matriz, copiado, tabs, quizzes)
│   │   └── images/
│   │       ├── hero_scientific_vector.png
│   │       └── matrix_consistency_art.png
│   └── templates/
│       ├── base.html           # Layout común (Navbar, Footer)
│       ├── index.html          # Landing page principal dentro de Flask
│       ├── levels.html         # Vista detallada de los 5 niveles del curso con recursos y quizzes
│       ├── books.html          # Vista de la Biblioteca de Autores y Libros Clásicos
│       ├── matriz.html         # Generador de Matriz de Consistencia Metodológica
│       └── 404.html            # Manejador visual de error 404
└── docs/
    ├── tutorial.md             # Guía paso a paso para principiantes
    ├── presentacion_sustentacion.md # Guión oficial de presentación para el video
    ├── arquitectura.md         # Documentación detallada de arquitectura
    ├── evidencia_antigravity.md # Informe de desarrollo agéntico con Google Antigravity
    ├── images/
    │   └── arquitectura.png    # Imagen del diagrama de arquitectura
    └── documentacion/          # Manuales técnicos de buenas prácticas con Flask
        ├── 01_arquitectura_y_patrones.md
        ├── 02_estructura_y_modulos.md
        ├── 03_guia_desarrollo_flask.md
        ├── 04_metodologia_cientifica_curriculo.md
        └── 05_despliegue_y_produccion.md
```

---

## 🚀 4. Guía de Instalación y Ejecución Rápida

### 1. Clonar o abrir el repositorio
```bash
git clone https://github.com/domingamaestriaufhec/Final-Python.git
cd Final-Python
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

---

## 🤖 6. Evidencia de Uso de Google Antigravity

El proyecto fue concebido, estructurado y programado utilizando el entorno agéntico de **Google Antigravity IDE**, aprovechando:
* **Planificación Agéntica Formal (*Plan-First Approach*):** Desacoplamiento estricto de la capa de dominio vs infraestructura.
* **Sistema de Skills Personalizadas (`.agents/skills/`):** Creación e integración de la skill `flask-docs-architect` para normativas de arquitectura en Flask.
* **Automatización de Tareas en Segundo Plano:** Creación de entornos `.venv`, gestión de dependencias y despliegue por API REST en Render.
* **Protocolos MCP Integrados:** Configuración de herramientas y colaboración en `.mcp.json`.

---

## 📚 Enlaces a Documentación Completa

* 📖 [Tutorial Paso a Paso para Principiantes](docs/tutorial.md)
* 🎬 [Guión Oficial para el Video de Sustentación](docs/presentacion_sustentacion.md)
* 🤖 [Evidencia de Google Antigravity IDE](docs/evidencia_antigravity.md)
* 🏗️ [Documentación de Arquitectura](docs/arquitectura.md)
* 📓 [Cuaderno Jupyter con Modelos Matemáticos](InvestigaLab_Metodologia_Cientifica.ipynb)
* 📄 [Documento Word Oficial (.docx)](Documento_Entrega_y_Sustentacion_InvestigaLab.docx)
* 📊 [Diagrama Visual de Arquitectura](docs/images/arquitectura.png)
* 📁 [Manuales Técnicos de Buenas Prácticas con Flask](docs/documentacion/)
