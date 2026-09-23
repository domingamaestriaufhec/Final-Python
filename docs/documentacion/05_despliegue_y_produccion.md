# 🚀 05. Guía de Despliegue, Producción y Publicación en GitHub

Este documento describe cómo desplegar la aplicación **InvestigaLab** en entornos de producción y cómo publicar la landing page en **GitHub Pages**.

---

## 🌐 1. Publicación de la Landing Page en GitHub Pages

El proyecto incluye un archivo `index.html` en la raíz del repositorio, lo que permite publicarlo instantáneamente en **GitHub Pages**:

1. Sube tu código al repositorio en GitHub:
   ```bash
   git add .
   git commit -m "feat: plataforma completa investigalab con landing y documentacion"
   git push origin main
   ```
2. En tu repositorio de GitHub, ve a **Settings** -> **Pages**.
3. En **Build and deployment** -> **Branch**, selecciona la rama `main` y la carpeta `/(root)`.
4. Haz clic en **Save**. En un par de minutos tu landing page estará disponible en:
   `https://<tu-usuario>.github.io/<nombre-del-repo>/`

---

## ⚙️ 2. Servidores WSGI de Producción para Python / Flask

El servidor de desarrollo que incluye Flask (`app.run()`) no está diseñado para soportar concurrencia o tráfico masivo. Para producción se debe usar un servidor WSGI:

### En Linux / Servidores Cloud (Gunicorn):
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"
```

### En Windows (Waitress):
```bash
pip install waitress
waitress-serve --port=5000 --call "app:create_app"
```

---

## 🔒 3. Variables de Entorno y Seguridad

Para producción, asegúrate de:
1. Definir `SECRET_KEY` desde una variable de entorno segura (ej. `os.environ.get("SECRET_KEY")`).
2. Mantener `debug=False`.
3. Configurar encabezados de seguridad HTTP (CSP, X-Content-Type-Options, X-Frame-Options).
