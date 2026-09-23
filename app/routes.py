"""
Definición de rutas y controladores para la plataforma de Metodología Científica.
"""
from flask import Blueprint, render_template, abort, jsonify, request
from app.data.levels_data import get_all_levels, get_level_by_id
from app.data.pipeline_data import get_pipeline_data
from app.data.books_data import get_all_books, get_books_for_level

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    """Ruta principal: Landing Page educativa del proyecto."""
    levels = get_all_levels()
    pipeline_data = get_pipeline_data()
    books = get_all_books()
    return render_template("index.html", levels=levels, pipeline=pipeline_data, books=books)


@main_bp.route("/niveles")
@main_bp.route("/niveles/<level_id>")
def levels(level_id=None):
    """Ruta del curso: Muestra los 5 niveles de investigación científica paso a paso."""
    all_levels = get_all_levels()
    
    # Si no se especifica nivel, seleccionamos el primero por defecto
    if not level_id:
        selected_level = all_levels[0]
    else:
        selected_level = get_level_by_id(level_id)
        if not selected_level:
            abort(404)
            
    level_books = get_books_for_level(selected_level["id"])
    return render_template(
        "levels.html",
        levels=all_levels,
        selected_level=selected_level,
        level_books=level_books
    )


@main_bp.route("/biblioteca")
def biblioteca_view():
    """Ruta de la biblioteca bibliográfica con los libros clásicos de metodología."""
    books = get_all_books()
    return render_template("books.html", books=books)


@main_bp.route("/pipeline")
def pipeline_view():
    """Ruta de Arquitectura & Pipeline inspirada en Archify."""
    pipeline_data = get_pipeline_data()
    return render_template("pipeline.html", pipeline=pipeline_data)


@main_bp.route("/matriz")
def matriz_view():
    """Ruta de la herramienta interactiva: Matriz de Consistencia Metodológica."""
    levels = get_all_levels()
    return render_template("matriz.html", levels=levels)


@main_bp.route("/api/pipeline-data")
def api_pipeline_data():
    """API Endpoint para consultar la información de la arquitectura en JSON."""
    return jsonify(get_pipeline_data())


@main_bp.errorhandler(404)
def page_not_found(e):
    """Manejador amigable de página no encontrada."""
    return render_template("404.html"), 404

