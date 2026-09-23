"""
Módulo de datos para la arquitectura del proyecto y visualización de Pipeline al estilo Archify.
Define las etapas de procesamiento, flujos de datos, componentes y especificaciones técnicas.
"""

ARCHIFY_PIPELINE = {
    "project_name": "InvestigaLab - Architecture & Scientific Pipeline",
    "version": "1.0.0",
    "framework": "Flask 3.0.3 (Python 3.10+)",
    "architecture_pattern": "Modular App Factory + Data Provider Layer + Jinja2 Rendering",
    "repository_reference": "https://github.com/tt-a1i/archify.git",
    "summary": "Pipeline de ejecución y diseño de arquitectura modular que desacopla la lógica técnica de la lógica de dominio (Metodología de la Investigación Científica).",
    
    # Etapas del Pipeline de la Aplicación Web
    "app_pipeline_stages": [
        {
            "id": "stage-1",
            "number": 1,
            "name": "HTTP Request / Dispatcher",
            "component": "run.py -> app/__init__.py",
            "type": "Entrada & Enrutamiento",
            "status": "active",
            "description": "El servidor WSGI recibe la petición HTTP del cliente y la delega a la factoría de la aplicación Flask.",
            "inputs": ["Petición HTTP (GET / POST)", "Headers", "Parámetros URL"],
            "outputs": ["Contexto de Request Flask", "Enrutamiento al Blueprint/Handler"]
        },
        {
            "id": "stage-2",
            "number": 2,
            "name": "Controller & Business Logic",
            "component": "app/routes.py",
            "type": "Controlador",
            "status": "active",
            "description": "El controlador analiza la ruta solicitada, invoca los proveedores de datos y procesa la lógica de negocio o filtros.",
            "inputs": ["Identificador de nivel ('principiante', 'experto', etc.)", "Datos de formulario (Matriz)"],
            "outputs": ["Diccionario de datos estructurado", "Variables de contexto para plantillas"]
        },
        {
            "id": "stage-3",
            "number": 3,
            "name": "Data Provider / Knowledge Repository",
            "component": "app/data/levels_data.py & pipeline_data.py",
            "type": "Capa de Datos",
            "status": "active",
            "description": "Capa desacoplada que suministra el currículo científico de 5 niveles y los metadatos de arquitectura sin acoplarse al framework.",
            "inputs": ["Consultas por ID o llamadas get_all_levels()"],
            "outputs": ["Objetos JSON / Diccionarios de datos científicos y pipeline"]
        },
        {
            "id": "stage-4",
            "number": 4,
            "name": "Template Rendering Engine",
            "component": "Jinja2 (app/templates/)",
            "type": "Renderizado de Vistas",
            "status": "active",
            "description": "El motor Jinja2 fusiona las plantillas base (base.html, index.html, levels.html, pipeline.html, matriz.html) con los datos.",
            "inputs": ["Plantillas HTML5", "Variables de contexto", "Helpers URL (url_for)"],
            "outputs": ["Documento HTML5 dinámico completo"]
        },
        {
            "id": "stage-5",
            "number": 5,
            "name": "Static Asset Delivery & Client Execution",
            "component": "app/static/css & app/static/js",
            "type": "Frontend & UI/UX",
            "status": "active",
            "description": "El navegador descarga hojas de estilo CSS modernas y scripts JS para interacción dinámica (simulador de matriz, interactividad).",
            "inputs": ["style.css", "main.js", "Recursos gráficos"],
            "outputs": ["Experiencia de usuario fluida, reactiva y responsive"]
        }
    ],

    # Pipeline Metodológico de Investigación Científica (El Dominio)
    "scientific_pipeline_stages": [
        {
            "step": 1,
            "phase": "Fase 1: Observación & Problema",
            "level": "Principiante",
            "tool": "Árbol de Problemas & Matriz de Viabilidad",
            "deliverable": "Pregunta de Investigación Delimitada"
        },
        {
            "step": 2,
            "phase": "Fase 2: Fundamentación Teórica",
            "level": "Básico",
            "tool": "Operadores Booleanos, Zotero & Taxonomía de Bloom",
            "deliverable": "Estado del Arte + Hipótesis ($H_0 / H_1$) + Objetivos SMART"
        },
        {
            "step": 3,
            "phase": "Fase 3: Diseño Metodológico",
            "level": "Intermedio",
            "tool": "Muestreo Probabilístico & Matriz de Operacionalización",
            "deliverable": "Variables, Dimensiones e Indicadores Definidos"
        },
        {
            "step": 4,
            "phase": "Fase 4: Instrumentación & Estadística",
            "level": "Avanzado",
            "tool": "Alfa de Cronbach, Shapiro-Wilk, t-Student / Mann-Whitney",
            "deliverable": "Base de Datos Analizada y Contraste de Hipótesis ($p < 0.05$)"
        },
        {
            "step": 5,
            "phase": "Fase 5: Publicación & Divulgación",
            "level": "Experto",
            "tool": "Estructura IMRyD, Comités de Bioética & Journal Finder",
            "deliverable": "Artículo Científico Publicable y Carta de Respuesta a Revisores"
        }
    ],

    # Métricas del Proyecto
    "metrics": {
        "total_levels": 5,
        "total_modules": 15,
        "pipeline_stages": 5,
        "clean_architecture_score": "100%",
        "framework_decoupling": "Completo (Idea vs Técnica)"
    }
}


def get_pipeline_data():
    """Retorna la especificación completa del pipeline y arquitectura Archify."""
    return ARCHIFY_PIPELINE
