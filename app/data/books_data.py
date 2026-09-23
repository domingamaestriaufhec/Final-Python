"""
Catálogo exhaustivo de fuentes bibliográficas y libros clásicos de Metodología de la Investigación Científica.
Utilizados para fundamentar teórica y epistemológicamente cada nivel del curso.
"""

BOOKS_DATA = [
    {
        "id": "sampieri-2018",
        "title": "Metodología de la Investigación: Las Rutas Cuantitativa, Cualitativa y Mixta",
        "authors": "Roberto Hernández-Sampieri & Christian Paulina Mendoza Torres",
        "year": "2018",
        "publisher": "McGraw-Hill Interamericana",
        "isbn": "978-1-4562-6096-5",
        "cover_badge": "Referente Iberoamericano",
        "level_affinity": ["principiante", "basico", "intermedio", "avanzado"],
        "description": "La obra cumbre y más utilizada en universidades de habla hispana. Establece con claridad meridiana las tres rutas metodológicas (cuantitativa, cualitativa y mixta), la formulación de problemas, hipótesis, muestreo y análisis de datos.",
        "key_contributions": [
            "Definición de las rutas cuantitativa (deductiva/secuencial), cualitativa (inductiva/recurrente) y mixta (multimétodo).",
            "Criterios para el planteamiento del problema: Objetivos, Preguntas, Justificación, Viabilidad y Evaluación de deficiencias.",
            "Matriz de operacionalización de variables y clasificación de alcances (Exploratorio, Descriptivo, Correlacional, Explicativo)."
        ],
        "recommended_chapters": [
            {"chapter": "Capítulo 1", "topic": "Las tres rutas de la investigación científica"},
            {"chapter": "Capítulo 2", "topic": "La idea de investigación y el origen de los proyectos"},
            {"chapter": "Capítulo 4", "topic": "Desarrollo de la perspectiva teórica y revisión de la literatura"},
            {"chapter": "Capítulo 6", "topic": "Formulación de hipótesis y operacionalización de variables"},
            {"chapter": "Capítulo 8", "topic": "Muestreo en la ruta cuantitativa"},
            {"chapter": "Capítulo 10", "topic": "Análisis de los datos cuantitativos"}
        ]
    },
    {
        "id": "bunge-ciencia",
        "title": "La Ciencia: Su Método y su Filosofía",
        "authors": "Mario Bunge",
        "year": "1960 (Reimpresiones constantes: 2014)",
        "publisher": "Editorial Sudamericana / Siglo XXI",
        "isbn": "978-950-07-0131-0",
        "cover_badge": "Epistemología Fundamental",
        "level_affinity": ["principiante", "experto"],
        "description": "Ensayo epistemológico fundamental que define con precisión qué es la ciencia fáctica vs formal, la naturaleza del método científico, las pautas del conocimiento racional y la ética científica.",
        "key_contributions": [
            "Diferenciación estricta entre ciencias formales (lógica y matemática) y ciencias fácticas (ciencias naturales y sociales).",
            "Las 15 características del conocimiento científico: fáctico, trasciende los hechos, analítico, especializado, claro y preciso, comunicable, verificable, metódico, sistemático, general, legal, explicativo, predictivo, abierto y útil.",
            "El método científico como procedimiento autocorrectivo y contrastable empíricamente."
        ],
        "recommended_chapters": [
            {"chapter": "Parte 1", "topic": "¿Qué es la ciencia? Ciencias formales y fácticas"},
            {"chapter": "Parte 2", "topic": "¿Cuál es el método de la ciencia? Verificabilidad y prueba de hipótesis"},
            {"chapter": "Parte 3", "topic": "¿Qué es una ley científica? Enunciados nómicos"}
        ]
    },
    {
        "id": "popper-logica",
        "title": "La Lógica de la Investigación Científica (The Logic of Scientific Discovery)",
        "authors": "Karl R. Popper",
        "year": "1934 (Edición castellana: 1980 / Tecnos)",
        "publisher": "Editorial Tecnos",
        "isbn": "978-84-309-0711-3",
        "cover_badge": "Principio de Falsabilidad",
        "level_affinity": ["principiante", "basico", "experto"],
        "description": "Obra maestra que revolucionó la filosofía de la ciencia al derribar el inductivismo y proponer el criterio de falsabilidad o refutabilidad como criterio de demarcación científica.",
        "key_contributions": [
            "El problema de la inducción: No importa cuántos cisnes blancos hayamos observado, esto no justifica la conclusión de que todos los cisnes sean blancos.",
            "Criterio de falsabilidad: Una teoría sólo es científica si es susceptible de ser falsada (contrastada y potencialmente refutada) por la experiencia.",
            "El método deductivo de contrastación de hipótesis: La ciencia no acumula verdades absolutas, sino hipótesis provisionales corroboradas."
        ],
        "recommended_chapters": [
            {"chapter": "Capítulo I", "topic": "Panorama de algunos problemas fundamentales (El problema de la inducción)"},
            {"chapter": "Capítulo IV", "topic": "La falsabilidad como criterio de demarcación"},
            {"chapter": "Capítulo X", "topic": "La corroboración: De cómo sale indemne una teoría"}
        ]
    },
    {
        "id": "creswell-design",
        "title": "Research Design: Qualitative, Quantitative, and Mixed Methods Approaches",
        "authors": "John W. Creswell & J. David Creswell",
        "year": "2018 (5th Edition)",
        "publisher": "SAGE Publications",
        "isbn": "978-1-5063-8670-6",
        "cover_badge": "Estándar Global Mixto",
        "level_affinity": ["intermedio", "avanzado", "experto"],
        "description": "La guía de diseño de investigación más respetada a nivel internacional. Presenta de forma estructurada los paradigmas filosóficos (pospositivismo, constructivismo, transformador y pragmatismo) y los diseños de métodos mixtos (convergente, explicativo secuencial y exploratorio secuencial).",
        "key_contributions": [
            "Los cuatro marcos epistemológicos de la investigación moderna.",
            "Estructura del planteamiento del problema con el 'Deficiencies Model of an Introduction'.",
            "Tipologías de diseños metodológicos mixtos avanzados con diagramas de flujo de integración de datos."
        ],
        "recommended_chapters": [
            {"chapter": "Chapter 1", "topic": "The Selection of a Research Approach (Philosophical Worldviews)"},
            {"chapter": "Chapter 5", "topic": "The Introduction (The Five-Step Deficiencies Model)"},
            {"chapter": "Chapter 8", "topic": "Quantitative Methods (Experimental & Survey Design)"},
            {"chapter": "Chapter 9", "topic": "Qualitative Methods (Phenomenology, Grounded Theory, Case Study)"},
            {"chapter": "Chapter 10", "topic": "Mixed Methods Procedures (Convergent & Sequential Designs)"}
        ]
    },
    {
        "id": "kerlinger-lee",
        "title": "Investigación del Comportamiento: Métodos de Investigación en Ciencias Sociales",
        "authors": "Fred N. Kerlinger & Howard B. Lee",
        "year": "2002 (4ta Edición en español)",
        "publisher": "McGraw-Hill Interamericana",
        "isbn": "978-970-10-3070-7",
        "cover_badge": "Rigor Psicométrico & Experimental",
        "level_affinity": ["intermedio", "avanzado"],
        "description": "Texto clásico indispensable para entender la formulación rigurosa de constructos, variables independientes y dependientes, control experimental, varianza (principio MAXMINCON), y psicometría.",
        "key_contributions": [
            "Definición rigurosa de Constructos, Variables Constitutivas y Variables Operacionales.",
            "El principio MAXMINCON del diseño de investigación: MAXimizar la varianza sistemática, MINimizar el error de varianza y CONtrolar las variables extrañas.",
            "Teoría de la medición, validez de constructo, confiabilidad por consistencia interna y análisis multivariado."
        ],
        "recommended_chapters": [
            {"chapter": "Capítulo 2", "topic": "Problemas e hipótesis científicas"},
            {"chapter": "Capítulo 3", "topic": "Constructos, variables y definiciones"},
            {"chapter": "Capítulo 18", "topic": "Diseño de investigación: El principio MAXMINCON"},
            {"chapter": "Capítulo 27", "topic": "Confiabilidad y validez de las mediciones"}
        ]
    },
    {
        "id": "arias-proyecto",
        "title": "El Proyecto de Investigación: Introducción a la Metodología Científica",
        "authors": "Fidias G. Arias",
        "year": "2012 (6ta Edición)",
        "publisher": "Editorial Episteme",
        "isbn": "980-07-8529-9",
        "cover_badge": "Guía Práctica Universitaria",
        "level_affinity": ["principiante", "basico", "intermedio"],
        "description": "Manual práctico, directo y accesible centrado en la elaboración de proyectos y tesis de grado. Destaca por su claridad al definir niveles de investigación, tipos de diseño, población, muestra e instrumentos.",
        "key_contributions": [
            "Clasificación didáctica de la investigación: Documental, de Campo y Experimental.",
            "Niveles de investigación: Exploratorio, Descriptivo y Explicativo.",
            "Técnicas e instrumentos de recolección de datos y su correspondencia metodológica."
        ],
        "recommended_chapters": [
            {"chapter": "Capítulo 2", "topic": "El problema de investigación y su formulación"},
            {"chapter": "Capítulo 3", "topic": "Objetivos de investigación y justificación"},
            {"chapter": "Capítulo 7", "topic": "Metodología: Población, muestra e instrumentos"}
        ]
    },
    {
        "id": "kuhn-revoluciones",
        "title": "La Estructura de las Revoluciones Científicas",
        "authors": "Thomas S. Kuhn",
        "year": "1962 (Fondo de Cultura Económica)",
        "publisher": "Fondo de Cultura Económica (FCE)",
        "isbn": "978-968-16-0443-1",
        "cover_badge": "Paradigmas Científicos",
        "level_affinity": ["principiante", "experto"],
        "description": "Obra monumental que introdujo los conceptos de 'paradigma', 'ciencia normal', 'anomalías', 'crisis' y 'cambio de paradigma' (revolución científica), transformando la historia de la ciencia.",
        "key_contributions": [
            "Concepto de Paradigma: Matriz disciplinar compartida por una comunidad científica.",
            "El ciclo de la ciencia: Pre-ciencia -> Ciencia Normal -> Anomalías -> Crisis -> Revolución Científica -> Nuevo Paradigma.",
            "Inconmensurabilidad entre paradigmas rivales."
        ],
        "recommended_chapters": [
            {"chapter": "Capítulo II", "topic": "El camino hacia la ciencia normal"},
            {"chapter": "Capítulo VIII", "topic": "La respuesta a la crisis"},
            {"chapter": "Capítulo IX", "topic": "Naturaleza y necesidad de las revoluciones científicas"}
        ]
    }
]


def get_all_books():
    """Retorna el catálogo completo de libros de referencia metodológica."""
    return BOOKS_DATA


def get_books_for_level(level_id):
    """Filtra los libros recomendados para un nivel pedagógico específico."""
    return [book for book in BOOKS_DATA if level_id in book["level_affinity"]]
