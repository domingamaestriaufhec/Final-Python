# 🎬 Guión y Estructura para el Video de Sustentación del Proyecto

Este documento contiene la estructura formal de diapositivas, los tiempos recomendados y el **guión textual paso a paso** para grabar tu video de sustentación de forma clara, fluida y profesional.

---

## ⏱️ Estructura General del Video (Duración estimada: 5 a 7 minutos)

```text
┌────────────────────────────────────────┬─────────────┐
│ Sección / Diapositiva                  │ Tiempo Est. │
├────────────────────────────────────────┼─────────────┤
│ 1. Portada, Presentación y Contexto    │ 0:00 - 0:45 │
│ 2. El Problema o Necesidad Abordada    │ 0:45 - 1:45 │
│ 3. La Solución Desarrollada            │ 1:45 - 2:45 │
│ 4. Framework Elegido (Flask) y Por Qué │ 2:45 - 3:30 │
│ 5. Principales Funcionalidades         │ 3:30 - 4:30 │
│ 6. Demostración en Vivo (Demo)         │ 4:30 - 6:00 │
│ 7. Repositorio, Despliegue y Conclusión│ 6:00 - 7:00 │
└────────────────────────────────────────┴─────────────┘
```

---

## 🎙️ Guión Paso a Paso para la Grabación

### 📌 1. Portada y Presentación (0:00 - 0:45)
* **Qué mostrar en pantalla:** Diapositiva de portada con el título del proyecto, tu nombre, maestría (UFHEC) y fecha.
* **Lo que debes decir:**
> *"Saludos cordiales, estimados profesores y evaluadores. Mi nombre es [Tu Nombre] y a continuación presento la sustentación del proyecto final de la asignatura Programación en Educación de la Maestría en Inteligencia Artificial de la Universidad UFHEC. El proyecto desarrollado se titula: **InvestigaLab: Escuela y Plataforma Interactiva de Metodología de la Investigación Científica**, desarrollada en Python con Flask y desplegada en producción en la nube."*

---

### 📌 2. El Problema o Necesidad Abordada (0:45 - 1:45)
* **Qué mostrar en pantalla:** Diapositiva del Problema (Metodología rígida, incongruencia de hipótesis, miedo a la estadística).
* **Lo que debes decir:**
> *"En el ámbito universitario y de posgrado, la metodología de la investigación suele enseñarse de forma abstracta, densa y desarticulada. Los estudiantes enfrentan graves obstáculos: incongruencia entre objetivos e hipótesis, dificultad para operacionalizar variables, confusión al seleccionar pruebas estadísticas adecuadas y bloqueos al redactar artículos científicos bajo normas internacionales. Existe una necesidad real de contar con herramientas interactivas que guíen al investigador paso a paso, desde su primera idea hasta la publicación indexada."*

---

### 📌 3. La Solución Desarrollada: InvestigaLab (1:45 - 2:45)
* **Qué mostrar en pantalla:** Diapositiva con la estructura de los 5 niveles y los autores clásicos (*Bunge, Popper, Sampieri, Kerlinger, Creswell*).
* **Lo que debes decir:**
> *"Para resolver esta problemática, construimos **InvestigaLab**, una plataforma web modular que estructura el aprendizaje en 5 niveles progresivos: **Principiante, Básico, Intermedio, Avanzado y Experto**. Cada nivel está rigurosamente fundamentado en obras canónicas de la ciencia: el falsacionismo de Karl Popper, la epistemología de Mario Bunge, las rutas de Roberto Hernández-Sampieri, el principio MAXMINCON de Fred Kerlinger y los diseños mixtos de John Creswell. Además, incluye herramientas vivas como el Generador de Matriz de Consistencia y la visualización de arquitectura de software y pipeline al estilo Archify."*

---

### 📌 4. Framework Seleccionado y Justificación Técnica (2:45 - 3:30)
* **Qué mostrar en pantalla:** Diapositiva técnica con los logos de Python, Flask, Jinja2, Render y Archify.
* **Lo que debes decir:**
> *"Como lenguaje obligatorio se utilizó **Python**, y como framework web se eligió **Flask**. Elegimos Flask porque implementa el patrón **Application Factory (`create_app`)**, permitiendo un desacoplamiento total entre la infraestructura técnica y la lógica de dominio científico. Esta arquitectura limpia asegura que el proyecto sea modular, extensible mediante Blueprints, ligero para entornos educativos y altamente reproducible con entornos virtuales `.venv` y servidores WSGI como Gunicorn."*

---

### 📌 5. Principales Funcionalidades de la Aplicación (3:30 - 4:30)
* **Qué mostrar en pantalla:** Resumen de funcionalidades clave.
* **Lo que debes decir:**
> *"Las funcionalidades centrales de InvestigaLab son:
> 1. **Currículo de 5 Niveles con Autoevaluación:** Módulos detallados, fórmulas matemáticas (muestreo, Alfa de Cronbach, $d$ de Cohen) y cuestionarios interactivos con retroalimentación inmediata.
> 2. **Biblioteca Epistemológica:** Catálogo de libros clásicos con capítulos recomendados e ISBN.
> 3. **Generador de Matriz de Consistencia Metodológica Viva:** Formulación de problema, objetivos, hipótesis y variables con exportación instantánea a Markdown.
> 4. **Pipeline Archify:** Documentación interactiva del flujo de procesamiento de software y fases de investigación."*

---

### 📌 6. Demostración en Vivo del Funcionamiento (4:30 - 6:00)
* **Qué mostrar en pantalla:** Abre tu navegador y navega por la aplicación desplegada en **https://investigalab-python.onrender.com**.
* **Lo que debes decir y hacer:**
  * *(Muestra la Landing Page)*: *"Aquí observamos la landing page con la estética dark tech, las métricas y la justificación pedagógica."*
  * *(Entra a `/niveles`)*: *"Al navegar por los 5 niveles, vemos el desarrollo teórico profundo, las citas de Sampieri y Popper, las fórmulas matemáticas y los cuestionarios interactivos con verificación inmediata."*
  * *(Entra a `/matriz`)*: *"En la Matriz Científica podemos cargar un ejemplo académico, editar las variables y copiar la matriz estructurada en Markdown."*
  * *(Entra a `/pipeline`)*: *"En la vista de Pipeline Archify se documenta el ciclo de vida de cada petición y el flujo de los entregables de investigación."*

---

### 📌 7. Repositorio de GitHub, Despliegue y Conclusión (6:00 - 7:00)
* **Qué mostrar en pantalla:** Muestra tu repositorio de GitHub `https://github.com/domingamaestriaufhec/Final-Python` y el cuaderno Jupyter `InvestigaLab_Metodologia_Cientifica.ipynb`.
* **Lo que debes decir:**
> *"El código fuente está organizado y publicado en GitHub bajo el repositorio `Final-Python`. Incluye su `README.md` completo, el archivo `requirements.txt`, la carpeta `docs/documentacion/` con manuales de buenas prácticas de Flask, el `Procfile` para Render, y el cuaderno Jupyter con la implementación matemática en Python. Todo el desarrollo se realizó en el entorno agéntico de **Google Antigravity**, garantizando una arquitectura industrial limpia y verificada. La aplicación se encuentra 100% activa en internet en `https://investigalab-python.onrender.com`. Muchas gracias por su atención."*
