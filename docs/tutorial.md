# 📖 Tutorial Paso a Paso: Ejecución del Proyecto desde Cero

¡Bienvenido/a! Si estás dando tus primeros pasos en Python o en el desarrollo web, este tutorial está diseñado para guiarte sin complicaciones ni tecnicismos confusos.

---

## 🎯 ¿Qué vamos a lograr?

Al finalizar esta guía tendrás:
1. Tu propio entorno virtual aislado de Python.
2. Todas las dependencias instaladas de forma segura.
3. El servidor web Flask ejecutándose en tu computadora.
4. La plataforma interactiva de **Metodología de la Investigación Científica** abierta en tu navegador.

---

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:
* **Python 3.10 o superior**: Puedes verificarlo abriendo tu terminal y escribiendo:
  ```bash
  python --version
  ```
* **Un editor de código** como VS Code, Cursor o PyCharm.

---

## 🚀 Paso 1: Abrir la Carpeta del Proyecto

Abre tu terminal (PowerShell en Windows o Terminal en macOS/Linux) y navega hasta el directorio del proyecto:

```bash
cd "ruta/hacia/tu/proyecto"
```

---

## 🐍 Paso 2: Crear el Entorno Virtual (`.venv`)

### ¿Por qué creamos un entorno virtual?
Un entorno virtual es como una "caja aislada" para este proyecto. Evita que las librerías que instalemos interfieran con otros proyectos o con el sistema operativo.

Ejecuta el siguiente comando:

```bash
python -m venv .venv
```

> **Nota:** Esto creará una carpeta oculta llamada `.venv` donde se guardará tu versión de Python y las librerías necesarias.

---

## ⚡ Paso 3: Activar el Entorno Virtual

Para que tu terminal utilice las herramientas de esa "caja aislada", debemos activarla:

### En Windows (PowerShell):
```powershell
.\.venv\Scripts\Activate.ps1
```

> 💡 *¿Te sale un error de políticas de ejecución en Windows?*
> Ejecuta en PowerShell como Administrador:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` y vuelve a activar.

### En Windows (Símbolo del sistema / CMD):
```cmd
.\.venv\Scripts\activate.bat
```

### En macOS / Linux:
```bash
source .venv/bin/activate
```

> ✅ **¿Cómo saber si está activo?**
> Verás `(.venv)` al inicio de la línea en tu terminal.

---

## 📦 Paso 4: Instalar las Dependencias

El archivo `requirements.txt` contiene la lista de herramientas que necesita la aplicación (como Flask y Jinja2). Instálalas con un solo comando:

```bash
pip install -r requirements.txt
```

Verás cómo se descargan e instalan los paquetes automáticamente.

---

## 🏃 Paso 5: Ejecutar la Aplicación Flask

Ahora que todo está listo, iniciamos el servidor web con Python:

```bash
python run.py
```

En tu terminal verás un mensaje similar a este:

```text
=======================================================
🚀 InvestigaLab: Curso de Metodología de la Investigación
📡 Servidor activo en: http://127.0.0.1:5000
🔬 Pestaña Pipeline Archify: http://127.0.0.1:5000/pipeline
📝 Matriz de Consistencia: http://127.0.0.1:5000/matriz
=======================================================
```

---

## 🌐 Paso 6: Abrir la Aplicación en tu Navegador

Abre tu navegador web favorito (Chrome, Edge, Firefox, Brave) e ingresa a:

👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)** (o `http://localhost:5000`)

¡Listo! Ya puedes explorar los **5 Niveles Científicos**, el **Generador de Matriz de Consistencia** y la visualización de arquitectura **Pipeline Archify**.

---

## 🛑 ¿Cómo detener el servidor?

Cuando quieras apagar la aplicación:
1. En tu terminal presiona: `Ctrl + C`.
2. Para desactivar el entorno virtual, escribe:
   ```bash
   deactivate
   ```
