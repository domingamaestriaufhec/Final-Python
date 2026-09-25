"""
Punto de entrada principal para ejecutar la aplicación web en Flask.
Ejecución: python run.py
"""
import os
import sys

# Asegurar codificación UTF-8 en la salida de consola de Windows
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from app import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print("\n" + "=" * 55)
    print("InvestigaLab: Curso de Metodologia de la Investigacion")
    print(f"Servidor activo en: http://127.0.0.1:{port}")
    print(f"Curso 5 Niveles: http://127.0.0.1:{port}/niveles")
    print(f"Matriz de Consistencia: http://127.0.0.1:{port}/matriz")
    print(f"Biblioteca de Autores: http://127.0.0.1:{port}/biblioteca")
    print("=" * 55 + "\n")
    app.run(host="0.0.0.0", port=port, debug=False)

