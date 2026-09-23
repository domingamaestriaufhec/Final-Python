---
name: flask-docs-architect
description: Comprehensive documentation and best practices generator for modular Flask web applications, scientific architecture, and pedagogical Python platforms.
---

# Flask Docs Architect Skill

Esta skill proporciona pautas, estándares y generadores de documentación para aplicaciones web en Python construidas con **Flask**, asegurando una arquitectura limpia (*Clean Architecture*), desacoplamiento de capas y documentación técnica de nivel industrial.

## 🎯 Principios de Documentación en Flask

1. **Patrón Factoría de Aplicación (Application Factory):** Documentar siempre `create_app()`, el registro de Blueprints y la inyección de configuraciones.
2. **Separación Dominio vs Infraestructura (Idea vs Técnica):** Documentar cómo los datos de negocio (`app/data/`) están aislados del framework de transporte (Flask/HTTP).
3. **Docstrings Estándar (Google/Sphinx Style):** Todas las funciones y módulos deben incluir descripciones claras de parámetros, retornos y excepciones.
4. **Flujo de Peticiones y Pipeline (Estilo Archify):** Mapear el ciclo de vida: Dispatcher -> Router -> Controller -> Data Provider -> Jinja2 Engine -> Client.
5. **Entorno Aislado y Reproducibilidad:** Documentar detalladamente `.venv`, `requirements.txt` y configuración para Windows, macOS y Linux.

## 📚 Estructura de Documentación Recomendada (`docs/documentacion/`)

```text
docs/documentacion/
├── 01_arquitectura_y_patrones.md       # Factory pattern, Blueprints, Data Layer
├── 02_estructura_y_modulos.md          # Layout del proyecto, responsabilidades
├── 03_guia_desarrollo_flask.md         # Ciclo de vida Flask, buenas prácticas
├── 04_metodologia_cientifica_curriculo.md # Fundamentos epistemológicos y los 5 niveles
├── 05_despliegue_y_produccion.md       # WSGI, variables de entorno, seguridad
└── 06_pipeline_archify.md              # Mapeo de etapas, inputs, outputs y contratos
```
