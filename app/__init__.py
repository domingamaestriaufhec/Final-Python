"""
Factoría de la Aplicación Flask (App Factory Pattern).
Permite instanciar y configurar la aplicación de forma limpia y extensible.
"""
from flask import Flask


def create_app():
    """Crea y configura una instancia de la aplicación Flask."""
    app = Flask(__name__)
    
    # Configuración básica
    app.config["SECRET_KEY"] = "investigalab-secret-key-2026-educativa"
    app.config["JSON_AS_ASCII"] = False

    # Registro de Rutas / Controladores
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app


# Instancia por defecto expuesta a nivel de paquete para servidores WSGI (Render: gunicorn app:app)
app = create_app()

