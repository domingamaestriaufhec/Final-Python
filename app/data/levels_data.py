"""
Datos pedagógicos y curriculares exhaustivos de los 5 niveles de Metodología de la Investigación Científica.
Fundamentados rigurosamente en las obras de:
- Mario Bunge (Epistemología y método de la ciencia fáctica)
- Karl Popper (Principio de falsabilidad y deducción)
- Roberto Hernández-Sampieri (Rutas cuantitativa, cualitativa y mixta)
- Fred N. Kerlinger (Constructos, varianza MAXMINCON y psicometría)
- John W. Creswell (Diseños metodológicos y modelos mixtos)
- Thomas S. Kuhn (Paradigmas científicos)
- Fidias G. Arias (Niveles y diseño del proyecto de investigación)
"""

LEVELS_DATA = [
    # =========================================================================
    # NIVEL 1: PRINCIPIANTE
    # =========================================================================
    {
        "id": "principiante",
        "number": 1,
        "badge": "Nivel 1",
        "title": "Fundamentos Epistemológicos y Planteamiento del Problema",
        "subtitle": "Descubre la naturaleza de la ciencia, el pensamiento crítico y la formulación del problema científico según Bunge, Popper y Sampieri.",
        "color": "#3b82f6",
        "icon": "fa-seedling",
        "duration": "12 Horas de estudio y práctica",
        "difficulty": "Principiante",
        "summary": "En este primer escalón aprenderás a distinguir el conocimiento empírico vulgar del conocimiento científico metódico y sistemático. Dominarás el criterio de falsabilidad de Popper, las 15 características de la ciencia según Mario Bunge y el método de delimitación de problemas de investigación propuesto por Hernández-Sampieri.",
        "book_references": [
            {
                "author": "Mario Bunge (1960)",
                "book": "La ciencia: su método y su filosofía",
                "chapter": "Cap. 1: ¿Qué es la ciencia?",
                "quote": "El conocimiento científico es fáctico, trasciende los hechos, es analítico, claro, preciso, comunicable, verificable, metódico y sistemático."
            },
            {
                "author": "Karl R. Popper (1934)",
                "book": "La lógica de la investigación científica",
                "chapter": "Cap. 1: El problema de la inducción y la demarcación",
                "quote": "No exigiré que un sistema científico pueda ser seleccionado de una vez para siempre, en un sentido positivo; pero sí que sea susceptible de selección en un sentido negativo por medio de contrastes o pruebas empíricas: ha de ser posible refutar por la experiencia un sistema científico empírico."
            },
            {
                "author": "Hernández-Sampieri & Mendoza (2018)",
                "book": "Metodología de la investigación: Las rutas cuantitativa, cualitativa y mixta",
                "chapter": "Cap. 2: El origen de un proyecto de investigación",
                "quote": "Las buenas ideas intrigan, alientan y excitan al investigador de manera personal; no son necesariamente nuevas, pero sí novedosas."
            }
        ],
        "modules": [
            {
                "title": "1.1 Epistemología, Tipos de Conocimiento y Falsacionismo",
                "description": "Comprende la evolución del pensamiento humano desde el mito y el sentido común hasta el método científico moderno.",
                "theoretical_deepening": "Mario Bunge clasifica las ciencias en Formales (ideales, como la lógica y las matemáticas, cuyo criterio de verdad es la coherencia deductiva) y Fácticas (materiales, como la física, biología y sociología, cuyo criterio de verdad es la contrastación empírica). Por su parte, Karl Popper demostró que la inducción ingenua ('todos los cisnes son blancos') es insuficiente; la ciencia avanza formulando conjeturas audaces y buscando activamente refutarlas (Falsacionismo).",
                "key_takeaways": [
                    "Diferencia entre creencia subjetiva, conocimiento empírico vulgar y ciencia sistemática",
                    "Criterio de Demarcación de Popper: Si una afirmación no puede ser sometida a prueba para demostrar su falsedad, no pertenece al dominio de la ciencia fáctica",
                    "El ciclo científico: Problema -> Hipótesis contrastable -> Prueba empírica -> Conclusiones autocorrectivas"
                ],
                "practical_activity": "Selecciona 3 afirmaciones de tu vida cotidiana o profesión y somételas a la 'Prueba de Popper': ¿Qué dato empírico observable demostraría que la afirmación es falsa?"
            },
            {
                "title": "1.2 Identificación de Vacíos de Conocimiento y Árbol de Problemas",
                "description": "Cómo pasar del asombro u observación empírica a la detección de una brecha en la literatura científica.",
                "theoretical_deepening": "Según Fidias Arias (2012) y Sampieri (2018), un problema de investigación no es un 'problema práctico' (como la falta de dinero en una empresa), sino un 'vacío de información': una pregunta cuya respuesta se desconoce en el estado actual de la ciencia. La técnica del Árbol de Problemas permite mapear: Raíces (Causas profundas), Tronco (Problema central o fenómeno) y Ramas (Efectos o consecuencias observadas).",
                "key_takeaways": [
                    "Fuentes de ideas de investigación: Experiencia profesional, lectura de artículos primarios, teorías existentes y vacíos prácticos",
                    "Criterios de pertinencia científica: Relevancia social, valor teórico y utilidad metodológica",
                    "Construcción del Árbol de Problemas: Relación Causa -> Efecto"
                ],
                "practical_activity": "Dibuja un árbol de problemas en tu cuaderno o documento definiendo: 3 causas raíz, 1 problema central delimitado y 3 consecuencias observables."
            },
            {
                "title": "1.3 La Formulación de la Pregunta de Investigación y Delimitación",
                "description": "Aprende a redactar preguntas científicas rigurosas evitando errores dicotómicos o ambigüedades.",
                "theoretical_deepening": "Kerlinger y Lee (2002) establecen 3 condiciones sine qua non para el planteamiento del problema: 1) Debe expresar una relación entre dos o más variables; 2) Debe formularse claramente y sin ambigüedades en forma de pregunta; 3) Debe implicar la posibilidad de someterse a una prueba empírica (observación y medición en la realidad). La delimitación debe ser Espacial (dónde), Temporal (cuándo) y Poblacional (en quiénes).",
                "key_takeaways": [
                    "Fórmula estructural: [Pregunta guía] + [Variable(s)] + [Unidad de análisis / Muestra] + [Contexto / Espacio] + [Tiempo]",
                    "Evitar preguntas de 'Sí/No' (dicotómicas) y preguntas morales o de juicio de valor ('¿Es bueno...?')",
                    "La regla de los 5 criterios de viabilidad: Recursos financieros, humanos, de tiempo, acceso al campo y éticos"
                ],
                "practical_activity": "Convierte una inquietud general en una pregunta formal de investigación aplicando los 5 elementos de la fórmula estructural."
            }
        ],
        "course_materials": [
            {
                "title": "Ficha de Trabajo: Plantilla del Árbol de Problemas & Preguntas Delimitadas",
                "type": "Plantilla Editable",
                "icon": "fa-file-lines",
                "description": "Formato estructurado para mapear causas raíces, problema central delimitado y efectos observables según los criterios de Kerlinger y Arias.",
                "action": "Descargar Ficha en Markdown / PDF"
            },
            {
                "title": "Checklist de Validación de Popper & Bunge",
                "type": "Lista de Verificación",
                "icon": "fa-square-check",
                "description": "Rúbrica de 10 puntos para verificar si tu propuesta cumple el criterio de falsabilidad, pertinencia fáctica y delimitación espacio-temporal.",
                "action": "Consultar Criterios de Demarcación"
            },
            {
                "title": "Guía de Epistemología: Las 15 Propiedades de la Ciencia",
                "type": "Guía de Lectura Rápida",
                "icon": "fa-book-open-reader",
                "description": "Resumen analítico del Capítulo 1 de Mario Bunge con cuadros comparativos entre ciencias formales y fácticas.",
                "action": "Abrir Resumen de Lectura"
            }
        ],
        "example_case": {
            "title": "Caso de Estudio Nivel 1: El Rendimiento Académico y el Sueño",
            "context": "Un docente observa que en el turno de la mañana los estudiantes universitarios muestran signos de fatiga y rinden menos.",
            "transformation": "Pregunta de Investigación Delimitada: '¿Cuál es la relación entre la calidad y duración del sueño (horas nocturnas) y el rendimiento en evaluaciones de álgebra lineal en estudiantes universitarios de ingeniería de primer semestre de la Universidad X durante el periodo 2026-I?'"
        },
        "quiz": [
            {
                "question": "¿Cuál es el criterio de demarcación científica propuesto por Karl Popper?",
                "options": [
                    "Una teoría es científica si puede demostrarse como una verdad absoluta e inmutable.",
                    "Una teoría es científica si formula hipótesis que pueden ser sometidas a pruebas empíricas capaces de refutarlas (falsabilidad).",
                    "Una teoría es científica sólo si utiliza fórmulas matemáticas y estadísticas avanzadas.",
                    "Una teoría es científica si ha sido aprobada por la mayoría de los investigadores de una universidad."
                ],
                "correct_index": 1,
                "explanation": "Karl Popper demostró que la ciencia avanza por refutación empírica (falsacionismo), no por verificación acumulativa indiscutible."
            },
            {
                "question": "Según Kerlinger y Hernández-Sampieri, ¿cuál de los siguientes enunciados representa un planteamiento de problema científico correcto?",
                "options": [
                    "¿Deberían las escuelas prohibir el uso de teléfonos móviles porque son perjudiciales?",
                    "¿Es bueno que los niños aprendan a programar computadoras a temprana edad?",
                    "¿En qué medida el tiempo de exposición a pantallas antes de dormir afecta la latencia del sueño profundo en adolescentes de 14 a 17 años?",
                    "¿Cómo solucionar la falta de recursos económicos en los laboratorios de química?"
                ],
                "correct_index": 2,
                "explanation": "La opción 3 relaciona variables empíricamente observables (tiempo de exposición y latencia de sueño), está delimitada poblacionalmente y no emite juicios de valor."
            }
        ]
    },

    # =========================================================================
    # NIVEL 2: BÁSICO
    # =========================================================================
    {
        "id": "basico",
        "number": 2,
        "badge": "Nivel 2",
        "title": "Marco Teórico, Estado del Arte e Hipótesis Científicas",
        "subtitle": "Estructura la base conceptual, domina la búsqueda booleana en bases indexadas y formula hipótesis con Hernández-Sampieri y Creswell.",
        "color": "#10b981",
        "icon": "fa-book-open",
        "duration": "16 Horas de estudio y práctica",
        "difficulty": "Básico",
        "summary": "Construye un marco teórico en embudo (de lo macro a lo micro), elabora estados del arte rigurosos con operadores booleanos en bases de datos científicas (Scopus, PubMed, SciELO), define objetivos de investigación con la Taxonomía de Bloom y formula hipótesis nulas ($H_0$) y alternativas ($H_1$).",
        "book_references": [
            {
                "author": "Hernández-Sampieri & Mendoza (2018)",
                "book": "Metodología de la Investigación",
                "chapter": "Cap. 4: Desarrollo de la perspectiva teórica & Cap. 6: Hipótesis",
                "quote": "El marco teórico no es un resumen de textos, sino una integración analítica de teorías, antecedentes e investigaciones previas que sustentan y encuadran el estudio."
            },
            {
                "author": "John W. Creswell (2018)",
                "book": "Research Design (5th Edition)",
                "chapter": "Chapter 5: The Introduction and The Deficiencies Model",
                "quote": "A rigorous theoretical framework establishes the rationale for the study, pointing out explicitly what previous literature has found and what deficiencies remain to be addressed."
            },
            {
                "author": "Fidias G. Arias (2012)",
                "book": "El Proyecto de Investigación",
                "chapter": "Cap. 4: Marco Teórico y Antecedentes",
                "quote": "Los antecedentes reflejan los avances y el estado actual del conocimiento en un área determinada y sirven de modelo o ejemplo para futuras investigaciones."
            }
        ],
        "modules": [
            {
                "title": "2.1 Estrategias de Búsqueda Bibliográfica y Estado del Arte",
                "description": "Dominio de operadores booleanos, descriptores controlados (MeSH/DeCS) y bases de datos indexadas.",
                "theoretical_deepening": "El 'Estado del Arte' (State of the Art) sintetiza el conocimiento existente sobre el problema en los últimos 3 a 5 años en revistas con revisión por pares (*peer-reviewed*). Para una búsqueda exhaustiva se emplean operadores booleanos: AND (intersección estricta), OR (sinónimos o variantes lingüísticas) y NOT (exclusión temática), combinados con comillas para frases exactas.",
                "key_takeaways": [
                    "Diferencia entre fuentes primarias (artículos de revistas indexadas), secundarias (libros de texto y revisiones) y literatura gris",
                    "Diseño de ecuaciones de búsqueda avanzadas: ej. `(\"gamification\" OR \"game-based learning\") AND (\"programming\" OR \"coding\") AND (\"higher education\")`",
                    "Gestión ética de bibliografía con gestores de referencias (Zotero, Mendeley) y estándares de citación (APA 7ma ed., IEEE, Vancouver)"
                ],
                "practical_activity": "Construye una ecuación de búsqueda en Google Académico o Scopus para tu tema, utilizando al menos 2 operadores booleanos y un descriptor en inglés, y descarga 5 artículos primarios."
            },
            {
                "title": "2.2 Redacción del Marco Teórico en Embudo y Matriz de Antecedentes",
                "description": "Estructura la teoría de soporte desde los postulados generales hasta el problema específico.",
                "theoretical_deepening": "Sampieri propone el 'Método del Mapeo Conceptual' y el 'Método por Índices' para estructurar el marco teórico en forma de embudo o pirámide invertida: 1) Teoría general que explica el fenómeno; 2) Antecedentes internacionales; 3) Antecedentes nacionales y locales; 4) Definición de términos básicos. Cada antecedente debe resumirse indicando: Autor, Año, Objetivo, Muestra, Metodología y Conclusión principal.",
                "key_takeaways": [
                    "Evitar el plagio y la copia textual mediante parafraseo crítico y síntesis conceptual",
                    "Construcción de la Matriz de Revisión de Literatura (Autor | País | Muestra | Instrumentos | Hallazgo Clave)",
                    "Alineación: Cada variable del problema debe tener un capítulo o acápite dedicado en el marco teórico"
                ],
                "practical_activity": "Completa una matriz de antecedentes comparando 3 investigaciones científicas publicadas en los últimos 5 años sobre tu tema."
            },
            {
                "title": "2.3 Objetivos SMART y Formulación de Hipótesis ($H_0$ y $H_1$)",
                "description": "Redacta objetivos de investigación con verbos de la Taxonomía de Bloom y formula hipótesis comprobables.",
                "theoretical_deepening": "Los Objetivos de Investigación guían el rumbo del estudio. Deben iniciar con un verbo en infinitivo (según la complejidad taxonómica: Describir -> Analizar -> Comparar -> Determinar -> Explicar). Las Hipótesis son explicaciones tentativas del fenómeno; se dividen en Hipótesis de Investigación ($H_1$) que predice la relación o diferencia esperada, e Hipótesis Nula ($H_0$) que postula la ausencia de relación o efecto ($H_0: \\mu_1 = \\mu_2$).",
                "key_takeaways": [
                    "Criterios SMART: Específicos (Specific), Medibles (Measurable), Alcanzables (Achievable), Relevantes (Relevant) y Temporales (Time-bound)",
                    "Correspondencia 1 a 1: A cada Objetivo Específico le corresponde una pregunta derivada y una hipótesis específica",
                    "Tipos de hipótesis: Descriptivas del valor de una variable, Correlacionales, De diferencia de grupos y Causales"
                ],
                "practical_activity": "Redacta el Objetivo General de tu proyecto, 3 Objetivos Específicos jerarquizados y formula la pareja de Hipótesis $H_0$ y $H_1$."
            }
        ],
        "course_materials": [
            {
                "title": "Matriz de Antecedentes & Ecuaciones Booleanas (Plantilla)",
                "type": "Plantilla de Búsqueda",
                "icon": "fa-table-list",
                "description": "Formato para registrar 10 antecedentes con operadores booleanos (AND, OR, NOT), filtros temporales y taxonomía de hallazgos.",
                "action": "Descargar Matriz de Antecedentes"
            },
            {
                "title": "Tabla Guía de Verbos Taxonómicos de Bloom para Objetivos",
                "type": "Guía de Redacción",
                "icon": "fa-spell-check",
                "description": "Desglose de verbos infinitivos clasificados según nivel de profundidad: Descriptivo, Analítico, Correlacional y Explicativo.",
                "action": "Consultar Tabla de Verbos"
            },
            {
                "title": "Fórmula y Sintaxis de Hipótesis Científicas (H0 vs H1)",
                "type": "Ficha Técnica",
                "icon": "fa-code-branch",
                "description": "Guía para plantear hipótesis estadísticas uniterales y bilaterales para diseños comparativos y correlacionales.",
                "action": "Abrir Ficha de Hipótesis"
            }
        ],
        "example_case": {
            "title": "Caso de Estudio Nivel 2: Gamificación en el Aprendizaje de Algoritmos",
            "context": "Se desea evaluar si una plataforma gamificada mejora la resolución de algoritmos frente a la enseñanza tradicional.",
            "transformation": "Objetivo General: 'Determinar el efecto del uso de una plataforma interactiva gamificada en el rendimiento académico en programación de algoritmos en estudiantes universitarios.'\nHipótesis Nula ($H_0$): 'No existen diferencias estadísticamente significativas en el rendimiento académico entre los estudiantes que utilizan la plataforma gamificada y los que reciben enseñanza tradicional ($H_0: \\mu_{\\text{exp}} = \\mu_{\\text{ctrl}}$).'\nHipótesis Alternativa ($H_1$): 'Los estudiantes que utilizan la plataforma gamificada obtienen un rendimiento académico significativamente superior al grupo tradicional ($H_1: \\mu_{\\text{exp}} > \\mu_{\\text{ctrl}}$).'"
        },
        "quiz": [
            {
                "question": "¿Cuál es la función principal de la Hipótesis Nula ($H_0$) en una investigación cuantitativa?",
                "options": [
                    "Es la hipótesis favorita del investigador que siempre busca ser comprobada.",
                    "Es la proposición que niega o refuta la existencia de una relación, efecto o diferencia entre las variables analizadas, y es la que se somete a prueba estadística.",
                    "Es una hipótesis que no tiene valor científico y debe eliminarse del documento final.",
                    "Es la hipótesis reservada exclusivamente para investigaciones cualitativas."
                ],
                "correct_index": 1,
                "explanation": "En inferencia estadística, las pruebas (como t-Student o ANOVA) contrastan la Hipótesis Nula ($H_0$) para determinar si la evidencia empírica permite rechazarla a favor de $H_1$."
            },
            {
                "question": "¿Cuál de los siguientes verbos es el más apropiado para un Objetivo General de alcance explicativo según la Taxonomía de Bloom?",
                "options": [
                    "Conocer la importancia de la educación virtual.",
                    "Determinar el impacto causal del uso de simuladores en la retención de conceptos físicos.",
                    "Opinar sobre los beneficios de las nuevas tecnologías.",
                    "Estudiar los factores que intervienen en el aula."
                ],
                "correct_index": 1,
                "explanation": "Verbos vagos como 'conocer', 'estudiar' u 'opinar' no son medibles ni evaluables; 'determinar el impacto causal' establece una acción concreta y verificable empíricamente."
            }
        ]
    },

    # =========================================================================
    # NIVEL 3: INTERMEDIO
    # =========================================================================
    {
        "id": "intermedio",
        "number": 3,
        "badge": "Nivel 3",
        "title": "Diseño Metodológico, Muestreo y Operacionalización",
        "subtitle": "Selecciona el paradigma epistemológico, diseña el muestreo probabilístico y operacionaliza variables con Kerlinger y Creswell.",
        "color": "#f59e0b",
        "icon": "fa-layer-group",
        "duration": "22 Horas de estudio y práctica",
        "difficulty": "Intermedio",
        "summary": "Domina la elección entre la ruta cuantitativa, cualitativa y mixta. Diseña experimentos con control de varianza (Principio MAXMINCON de Kerlinger), calcula tamaños muestrales con fórmulas matemáticas de precisión estadística y construye matrices completas de operacionalización de variables (dimensiones, indicadores y escalas de medición).",
        "book_references": [
            {
                "author": "Fred N. Kerlinger & Howard B. Lee (2002)",
                "book": "Investigación del Comportamiento",
                "chapter": "Cap. 18: Diseño de investigación & Cap. 3: Variables",
                "quote": "El diseño de investigación expresa tanto la estructura del problema de investigación como el plan de investigación utilizado para obtener evidencia empírica sobre las relaciones del problema. Se rige por el principio MAXMINCON."
            },
            {
                "author": "John W. Creswell (2018)",
                "book": "Research Design",
                "chapter": "Chapter 8: Quantitative Methods & Chapter 10: Mixed Methods",
                "quote": "Sampling procedures must specify whether the selection is probabilistic or non-probabilistic, justifying the sample size through statistical power analysis to minimize Type I and Type II errors."
            },
            {
                "author": "Hernández-Sampieri et al. (2014/2018)",
                "book": "Metodología de la Investigación",
                "chapter": "Cap. 5: Alcances de la investigación & Cap. 8: Muestra",
                "quote": "Operacionalizar una variable es transitar del concepto abstracto a la realidad observable mediante dimensiones e indicadores empíricamente cuantificables."
            }
        ],
        "modules": [
            {
                "title": "3.1 Enfoques, Alcances y Tipologías de Diseño de Investigación",
                "description": "Comprende la matriz de diseños experimentales vs no experimentales y sus alcances temporales.",
                "theoretical_deepening": "Los alcances se dividen en: 1) Exploratorio (fenómenos vírgenes o poco estudiados); 2) Descriptivo (medición de variables independientes); 3) Correlacional (evalúa el grado de asociación estadística entre variables); 4) Explicativo (determina relaciones de causa-efecto). Los diseños cuantitativos se dividen en: No experimentales (Transeccionales/Transversales o Longitudinales de tendencia, evolución o panel) y Experimentales (Pre-experimentales, Cuasiexperimentales con grupos intactos, y Experimentos Puros con aleatorización y grupo control).",
                "key_takeaways": [
                    "El Principio MAXMINCON de Kerlinger: MAXimizar la varianza sistemática primaria, MINimizar la varianza de error (medición) y CONtrolar las variables extrañas (confusoras)",
                    "Validez Interna (grado de certeza de que la variable independiente causó el efecto en la dependiente) vs Validez Externa (posibilidad de generalizar a otras poblaciones)",
                    "Amenazas a la validez interna: Historia, maduración, instrumentación, regresión estadística, mortalidad experimental"
                ],
                "practical_activity": "Elabora un diagrama metodológico justificando por qué tu investigación requiere un diseño experimental o no experimental, identificando 2 posibles variables extrañas y cómo las vas a controlar."
            },
            {
                "title": "3.2 Cálculo del Tamaño Muestral y Técnicas de Muestreo",
                "description": "Aprende las fórmulas matemáticas estadísticas para calcular la muestra representativa en poblaciones finitas e infinitas.",
                "theoretical_deepening": "La muestra ($n$) debe representar fielmente a la población ($N$). Para poblaciones finitas ($N < 100,000$), se utiliza la fórmula estadística clásica:\n\n$$n = \\frac{N \\cdot Z^2 \\cdot p \\cdot q}{e^2 \\cdot (N - 1) + Z^2 \\cdot p \\cdot q}$$\n\nDonde $Z$ es el nivel de confianza ($Z = 1.96$ para 95%), $p$ es la probabilidad de éxito ($p = 0.5$ por defecto para máxima varianza), $q = 1 - p = 0.5$, $e$ es el margen de error máximo admisible ($e = 0.05$ o 5%), y $N$ es el tamaño de la población.",
                "key_takeaways": [
                    "Muestreo Probabilístico: Aleatorio simple, Sistemático ($k = N/n$), Estratificado (proporcional al estrato) y Por conglomerados",
                    "Muestreo No Probabilístico: Por conveniencia, Por cuotas, Intencional/Juicio y Bola de nieve (sujetos de difícil acceso)",
                    "Criterios de elegibilidad: Inclusión (quiénes entran), Exclusión (quiénes se descartan por factores de confusión) y Eliminación (quiénes se retiran durante el estudio)"
                ],
                "practical_activity": "Aplica la fórmula matemática para calcular el tamaño de muestra de una facultad universitaria con $N = 2,400$ estudiantes, con 95% de confianza ($Z = 1.96$) y 5% de margen de error ($e = 0.05$). Muestra el cálculo paso a paso."
            },
            {
                "title": "3.3 Matriz de Operacionalización de Variables",
                "description": "Desglosa variables conceptuales en dimensiones, indicadores cuantificables y escalas de medición.",
                "theoretical_deepening": "Una variable es una propiedad que puede variar y cuya variación es susceptible de medirse u observarse (Sampieri). La operacionalización requiere: 1) Definición Conceptual (teórica de libro); 2) Definición Operacional (procedimiento de medición); 3) Dimensiones (facetas del constructo); 4) Indicadores (manifestaciones empíricas medibles); 5) Escala de Medición: Nominal (cualitativa sin orden, ej. género), Ordinal (cualitativa con jerarquía, ej. nivel socioeconómico), Intervalo (cuantitativa con cero relativo, ej. temperatura en °C o puntaje en test) y Razón (cuantitativa con cero absoluto, ej. edad, salario, tiempo en segundos).",
                "key_takeaways": [
                    "Variable Independiente ($X$): La presunta causa que se manipula o analiza",
                    "Variable Dependiente ($Y$): El efecto o resultado que se mide",
                    "Estructura estándar de la tabla: Variable | Definición Conceptual | Definición Operacional | Dimensiones | Indicadores | Escala | Ítems del Instrumento"
                ],
                "practical_activity": "Diseña una matriz de operacionalización completa para un constructo complejo como 'Competencia Digital Docente' o 'Calidad del Software Educativo' con al menos 2 dimensiones y 4 indicadores."
            }
        ],
        "course_materials": [
            {
                "title": "Calculadora & Formulario de Tamaño Muestral (Poblaciones Finitas e Infinitas)",
                "type": "Ficha Matemática / Calculadora",
                "icon": "fa-calculator",
                "description": "Fórmulas de muestreo probabilístico paso a paso con valores críticos Z (90%, 95%, 99%) y márgenes de error e.",
                "action": "Descargar Ficha de Muestreo"
            },
            {
                "title": "Plantilla de Matriz de Operacionalización de Variables",
                "type": "Plantilla Estructurada",
                "icon": "fa-table-cells",
                "description": "Cuadro estandarizado para definir variables, dimensiones, indicadores, niveles y escalas de medición (Nominal, Ordinal, Intervalo, Razón).",
                "action": "Descargar Matriz de Operacionalización"
            },
            {
                "title": "Guía del Principio MAXMINCON de Fred Kerlinger",
                "type": "Guía de Diseño Experimental",
                "icon": "fa-flask-vial",
                "description": "Estrategias para maximizar varianza sistemática, minimizar varianza de error y controlar variables extrañas.",
                "action": "Consultar Guía Experimental"
            }
        ],
        "example_case": {
            "title": "Caso de Estudio Nivel 3: Operacionalización de 'Usabilidad de Software Educativo'",
            "context": "Evaluación metodológica de una plataforma de aprendizaje en línea.",
            "transformation": "Variable: Usabilidad del Software (ISO/IEC 25010).\n- Dimensión 1: Eficiencia -> Indicador: Tiempo medio (en segundos) para completar una tarea algorítmica (Escala: Razón).\n- Dimensión 2: Eficacia -> Indicador: Porcentaje de tareas completadas sin error (Escala: Razón).\n- Dimensión 3: Satisfacción Subjetiva -> Indicador: Puntaje en la escala System Usability Scale (SUS) de 1 a 100 (Escala: Intervalo)."
        },
        "quiz": [
            {
                "question": "En la fórmula de cálculo de muestra para poblaciones finitas con 95% de confianza, ¿cuál es el valor estándar de Z?",
                "options": [
                    "Z = 1.00",
                    "Z = 1.96",
                    "Z = 2.58",
                    "Z = 0.05"
                ],
                "correct_index": 1,
                "explanation": "Para una distribución normal estándar con dos colas y un nivel de confianza del 95% ($1 - \\alpha = 0.95$), el valor crítico es $Z = 1.96$."
            },
            {
                "question": "¿Qué establece el principio MAXMINCON postulado por Fred N. Kerlinger?",
                "options": [
                    "Maximizar el número de participantes, minimizar los costos y controlar la duración del proyecto.",
                    "Maximizar la varianza sistemática primaria, minimizar la varianza de error de medición y controlar la varianza de las variables extrañas.",
                    "Maximizar el uso de computadoras, minimizar la teoría y concentrarse en el código.",
                    "Maximizar el número de hipótesis y minimizar el marco teórico."
                ],
                "correct_index": 1,
                "explanation": "El principio MAXMINCON es el pilar del diseño experimental: maximiza la varianza debida a la variable independiente, minimiza el error aleatorio y controla las variables confusoras."
            }
        ]
    },

    # =========================================================================
    # NIVEL 4: AVANZADO
    # =========================================================================
    {
        "id": "avanzado",
        "number": 4,
        "badge": "Nivel 4",
        "title": "Instrumentación, Psicometría y Estadística Inferencial",
        "subtitle": "Valida instrumentos con Alfa de Cronbach y V de Aiken, y aplica pruebas paramétricas/no paramétricas rigurosas.",
        "color": "#8b5cf6",
        "icon": "fa-chart-pie",
        "duration": "28 Horas de estudio y práctica",
        "difficulty": "Avanzado",
        "summary": "Construye instrumentos psicométricamente válidos, mide su consistencia interna con la fórmula del Alfa de Cronbach ($\\alpha$) y Coeficiente Omega ($\\omega$), calcula la validez de contenido por juicio de expertos (V de Aiken), ejecuta pruebas de normalidad (Shapiro-Wilk / Kolmogorov-Smirnov) y contrasta hipótesis mediante pruebas paramétricas (t-Student, ANOVA) y no paramétricas (Mann-Whitney, Wilcoxon, Chi-cuadrado).",
        "book_references": [
            {
                "author": "Fred N. Kerlinger & Howard B. Lee (2002)",
                "book": "Investigación del Comportamiento",
                "chapter": "Cap. 27: Confiabilidad & Cap. 28: Validez",
                "quote": "La validez responde a la pregunta: ¿Estamos midiendo realmente lo que creemos que estamos midiendo? La confiabilidad responde: Si medimos lo mismo otra vez con el mismo instrumento, ¿obtendremos los mismos resultados?"
            },
            {
                "author": "Hernández-Sampieri & Mendoza (2018)",
                "book": "Metodología de la Investigación",
                "chapter": "Cap. 9: Recolección de los datos cuantitativos & Cap. 10: Análisis cuantitativo",
                "quote": "Ningún análisis estadístico es confiable si los datos provienen de un instrumento sin validez demostrada de contenido, constructo y criterio."
            },
            {
                "author": "John W. Creswell (2018)",
                "book": "Research Design",
                "chapter": "Chapter 8: Quantitative Methods (Statistical Significance & Effect Size)",
                "quote": "Statistical significance (p-value) only tells us if an effect is likely not due to chance; researchers must always report Effect Size (Cohen's d or eta-squared) to convey the practical magnitude of the findings."
            }
        ],
        "modules": [
            {
                "title": "4.1 Validación Psicométrica de Instrumentos (V de Aiken y Alfa de Cronbach)",
                "description": "Mide el rigor psicométrico de cuestionarios y escalas de medición con fórmulas matemáticas.",
                "theoretical_deepening": "La validación consta de 3 ejes:\n1. **Validez de Contenido (Juicio de Expertos):** Se cuantifica mediante el Coeficiente V de Aiken:\n$$V = \\frac{S}{n(c - 1)} = \\frac{\\sum (r_i - l)}{n(c - 1)}$$\nDonde $r_i$ es la calificación del juez, $l$ es la calificación mínima, $n$ es el número de jueces y $c$ es el número de categorías. Se exige $V > 0.80$.\n2. **Confiabilidad / Consistencia Interna:** Para ítems en escala Likert se calcula el Alfa de Cronbach ($\\alpha$):\n$$\\alpha = \\frac{K}{K - 1} \\left( 1 - \\frac{\\sum s_i^2}{s_t^2} \\right)$$\nDonde $K$ es el número de ítems, $s_i^2$ es la varianza de cada ítem y $s_t^2$ es la varianza de la puntuación total. Se interpreta: $\\alpha \\ge 0.80$ (Bueno/Excelente).",
                "key_takeaways": [
                    "Validez de Constructo: Análisis Factorial Exploratorio (AFE) y Confirmatorio (AFC) para verificar que los ítems saturan en las dimensiones teóricas",
                    "Prueba Piloto: Aplicación preliminar a una muestra representativa pequeña (15-30 sujetos) antes del levantamiento masivo",
                    "Diferencia entre Alfa de Cronbach (asume tau-equivalencia) y Coeficiente Omega de McDonald (más robusto ante cargas factoriales desiguales)"
                ],
                "practical_activity": "Aplica una escala de 5 ítems a 10 personas piloto, calcula la varianza de cada ítem y determina el coeficiente Alfa de Cronbach utilizando la fórmula matemática."
            },
            {
                "title": "4.2 Pruebas de Normalidad y Selección de Pruebas Estadísticas",
                "description": "El árbol de decisión para elegir con precisión entre estadística paramétrica y no paramétrica.",
                "theoretical_deepening": "Antes de contrastar hipótesis, se debe verificar el supuesto de Normalidad de la distribución de los datos:\n- Para muestras pequeñas ($n < 50$): Prueba de Shapiro-Wilk.\n- Para muestras grandes ($n \\ge 50$): Prueba de Kolmogorov-Smirnov con corrección de Lilliefors.\n**Regla de Decisión:**\n- Si $p > 0.05$: Distribución Normal -> Se usan **Pruebas Paramétricas** (t-Student, ANOVA, Correlación de Pearson).\n- Si $p \\le 0.05$: Distribución No Normal -> Se usan **Pruebas No Paramétricas** (Mann-Whitney, Wilcoxon, Kruskal-Wallis, Correlación de Spearman, Chi-cuadrado).",
                "key_takeaways": [
                    "Comparación de 2 grupos independientes: t de Student (paramétrica) vs U de Mann-Whitney (no paramétrica)",
                    "Comparación de 2 grupos relacionados (Pretest-Postest): t de Student pareada vs Prueba de Rangos de Wilcoxon",
                    "Comparación de 3 o más grupos: ANOVA de un factor (con pruebas post-hoc Tukey/Bonferroni) vs Kruskal-Wallis",
                    "Asociación entre variables cuantitativas: Coeficiente de correlación de Pearson ($r$) vs Spearman ($\\rho$)"
                ],
                "practical_activity": "Dado un conjunto de datos pretest-postest de 30 estudiantes con distribución normal ($p = 0.35$), justifica qué prueba estadística debes aplicar y escribe la sintaxis de hipótesis correspondientes."
            },
            {
                "title": "4.3 Significación Estadística ($p < 0.05$) y Tamaño del Efecto ($d$ de Cohen)",
                "description": "Aprende a interpretar el valor p sin caer en trampas metodológicas y calcula la magnitud práctica del hallazgo.",
                "theoretical_deepening": "La significación estadística ($p < 0.05$) solo indica que la probabilidad de que el resultado se deba al azar es menor al 5%. Sin embargo, la Asociación Americana de Estadística (ASA) y la APA exigen reportar el **Tamaño del Efecto** (Effect Size), que cuantifica la fuerza o magnitud real de la intervención. Para diferencias de medias se usa la $d$ de Cohen:\n\n$$d = \\frac{\\bar{X}_1 - \\bar{X}_2}{s_{\\text{agrupada}}}$$\n\nInterpretación de Cohen: $d = 0.20$ (Efecto pequeño), $d = 0.50$ (Efecto mediano), $d \\ge 0.80$ (Efecto grande o potente).",
                "key_takeaways": [
                    "Error Tipo I ($\\alpha$): Rechazar una hipótesis nula que en realidad es verdadera (falso positivo)",
                    "Error Tipo II ($\\beta$): No rechazar una hipótesis nula que en realidad es falsa (falso negativo)",
                    "Potencia estadística ($1 - \\beta$): Probabilidad de detectar un efecto real (estándar aceptable: $\\ge 0.80$)",
                    "Intervalos de confianza al 95% (IC 95%): Estimación del rango donde se ubica el parámetro poblacional real"
                ],
                "practical_activity": "Calcula el tamaño del efecto $d$ de Cohen dados dos grupos: Grupo Experimental ($\bar{X}_1 = 17.5, s_1 = 1.8$) y Grupo Control ($\bar{X}_2 = 13.2, s_2 = 2.1$). Interpreta la magnitud pedagógica del resultado."
            }
        ],
        "course_materials": [
            {
                "title": "Árbol de Decisión Estadística Paramétrica vs No Paramétrica",
                "type": "Diagrama de Flujo / Ficha Guía",
                "icon": "fa-diagram-project",
                "description": "Esquema interactivo para seleccionar la prueba adecuada (t-Student, ANOVA, Mann-Whitney, Wilcoxon, Chi-Cuadrado) según supuestos de normalidad.",
                "action": "Consultar Árbol de Decisión"
            },
            {
                "title": "Formulario Psicométrico: V de Aiken y Alfa de Cronbach",
                "type": "Plantilla de Juicio de Expertos",
                "icon": "fa-chart-simple",
                "description": "Fichas de validación de contenido para jueces expertos y sintaxis de consistencia interna con escalas Likert.",
                "action": "Descargar Ficha Psicométrica"
            },
            {
                "title": "Tabla de Interpretación del Tamaño del Efecto (d de Cohen & Eta Cuadrado)",
                "type": "Guía de Análisis Cuantitativo",
                "icon": "fa-chart-pie",
                "description": "Criterios internacionales de la APA y ASA para reportar la magnitud sustantiva de los hallazgos experimentales.",
                "action": "Abrir Guía de Tamaño del Efecto"
            }
        ],
        "example_case": {
            "title": "Caso de Estudio Nivel 4: Contraste de Hipótesis y Tamaño del Efecto en Educación STEM",
            "context": "Evaluación de un método de robótica educativa en el pensamiento computacional ($n = 60$).",
            "transformation": "1. Normalidad evaluada con Kolmogorov-Smirnov: $p = 0.28$ (Normalidad confirmada).\n2. Prueba Paramétrica: t de Student para muestras independientes: $t(58) = 4.15, p = 0.0002$ ($p < 0.001$, estadísticamente muy significativo).\n3. Tamaño del Efecto: $d = 1.08$ (Efecto muy grande según criterios de Cohen).\n4. Conclusión científica: Se rechaza $H_0$ con un 99.9% de certeza y un impacto sustantivo de gran magnitud en el aprendizaje."
        },
        "quiz": [
            {
                "question": "Si una prueba de normalidad Shapiro-Wilk arroja un valor p = 0.012 en una variable de rendimiento, ¿qué tipo de estadística debes seleccionar?",
                "options": [
                    "Estadística Paramétrica (t de Student o ANOVA) porque p es menor a 0.05.",
                    "Estadística No Paramétrica (Mann-Whitney o Wilcoxon) porque p < 0.05 indica que los datos se desvían significativamente de la distribución normal.",
                    "Cualquier prueba es válida indistintamente de la distribución de los datos.",
                    "Se debe anular la investigación y recolectar los datos nuevamente."
                ],
                "correct_index": 1,
                "explanation": "En las pruebas de normalidad, la hipótesis nula postula que los datos son normales. Un valor $p < 0.05$ rechaza la normalidad, obligando al uso de pruebas no paramétricas."
            },
            {
                "question": "¿Qué valor mínimo de Alfa de Cronbach es considerado generalmente aceptable para la confiabilidad de un instrumento de medición psicométrica?",
                "options": [
                    "Alfa de Cronbach > 0.20",
                    "Alfa de Cronbach > 0.50",
                    "Alfa de Cronbach >= 0.70 (óptimo >= 0.80)",
                    "Alfa de Cronbach debe ser exactamente 1.00"
                ],
                "correct_index": 2,
                "explanation": "En literatura psicométrica (Kerlinger, Sampieri, George & Mallery), un Alfa de Cronbach $\\ge 0.70$ es el umbral mínimo aceptable, y $\\ge 0.80$ denota buena/excelente consistencia interna."
            }
        ]
    },

    # =========================================================================
    # NIVEL 5: EXPERTO
    # =========================================================================
    {
        "id": "experto",
        "number": 5,
        "badge": "Nivel 5",
        "title": "Publicación Científica, Bioética, Indexación y Peer Review",
        "subtitle": "Redacta artículos en formato IMRyD, domina la bioética institucional y publica en revistas Scopus/WoS (Q1-Q4).",
        "color": "#ec4899",
        "icon": "fa-award",
        "duration": "35 Horas de estudio y práctica",
        "difficulty": "Experto",
        "summary": "El nivel cumbre del investigador: redacción científica con la estructura estándar internacional IMRyD (Introducción, Métodos, Resultados y Discusión), bioética rigurosa (Declaración de Helsinki, directrices Belmont y uso ético de IA), selección estratégica de revistas indexadas (JCR, Scopus, SciELO) mediante cuartiles (Q1-Q4), y redacción de cartas de respuesta profesional punto por punto (*Rebuttal letters*) para superar la revisión por pares (*peer review*).",
        "book_references": [
            {
                "author": "John W. Creswell & J. David Creswell (2018)",
                "book": "Research Design",
                "chapter": "Chapter 4: Writing Strategies and Ethical Considerations",
                "quote": "Ethical research requires anticipating ethical issues throughout all phases of the research process, protecting participant confidentiality, obtaining informed consent, and transparently declaring conflicts of interest and funding."
            },
            {
                "author": "Mario Bunge (1960/2014)",
                "book": "La investigación científica",
                "chapter": "Cap. 15: La contrastación de las teorías y la comunicación científica",
                "quote": "La ciencia no es un monólogo, sino un diálogo crítico constante entre investigadores que someten sus hallazgos al escrutinio implacable de la comunidad de pares."
            },
            {
                "author": "Thomas S. Kuhn (1962)",
                "book": "La estructura de las revoluciones científicas",
                "chapter": "Cap. 2: El camino hacia la ciencia normal",
                "quote": "El consenso de la comunidad científica y los canales de publicación formalizados son los que definen las reglas del juego metodológico en un paradigma establecido."
            }
        ],
        "modules": [
            {
                "title": "5.1 Estructura Estándar del Artículo Científico (Formato IMRyD)",
                "description": "Dominio de cada sección de un paper científico de alto impacto para revistas indexadas.",
                "theoretical_deepening": "El formato IMRyD es el estándar adoptado por las principales editoriales científicas mundiales (Elsevier, Springer Nature, IEEE, Wiley):\n- **Título:** Preciso, informativo, sin abreviaturas (máximo 15 palabras) con palabras clave indexadas.\n- **Resumen (Abstract):** Síntesis de 200-250 palabras estructurada en: Background, Objectives, Methods, Results y Conclusions.\n- **Introducción ($I$):** ¿Cuál es el problema? (Embudo del Estado del Arte y vacíos de la literatura según Creswell).\n- **Métodos ($M$):** ¿Cómo se estudió el problema? (Diseño, muestra, instrumentos, procedimiento y análisis estadístico detallado para garantizar reproducibilidad).\n- **Resultados ($R$):** ¿Qué se encontró? (Tablas y figuras autoexplicativas sin redundancia con el texto narrativo).\n- **Discusión ($D$):** ¿Qué significan los hallazgos? (Contrastación con autores previos, limitaciones reconocidas con honestidad y líneas futuras de investigación).",
                "key_takeaways": [
                    "Diferencia crucial entre 'Resultados' (hechos estadísticos objetivos) y 'Discusión' (interpretación teórica y confrontación con la literatura)",
                    "Elaboración de tablas y figuras según normas APA 7ma ed. (sin líneas verticales, con notas explicativas y títulos claros)",
                    "Declaración de disponibilidad de datos (Data Availability Statement) y reproducibilidad computacional"
                ],
                "practical_activity": "Redacta el Resumen estructurado (Abstract) de tu investigación en exactamente 250 palabras en español e inglés, dividiéndolo en: Introducción, Método, Resultados y Conclusión."
            },
            {
                "title": "5.2 Bioética, Integridad Científica, Comités IRB y Uso de IA",
                "description": "Principios éticos de Helsinki, consentimiento informado, autoría responsable y directrices sobre Inteligencia Artificial.",
                "theoretical_deepening": "Toda investigación empírica con seres humanos o datos sensibles debe regirse por los principios del Informe Belmont (Respeto a las personas/Autonomía, Beneficencia, No maleficencia y Justicia) y la Declaración de Helsinki. Requiere aprobación previa de un Comité Institucional de Ética en Investigación (IRB). En cuanto a IA Generativa (ChatGPT, Claude, etc.), los lineamientos de COPE (Committee on Publication Ethics) y las revistas de prestigio establecen que los modelos de lenguaje **no pueden ser listados como autores** y su uso para redacción o asistencia debe declararse explícitamente en la sección de Métodos.",
                "key_takeaways": [
                    "Elaboración de Formatos de Consentimiento Informado (objetivo, riesgos, beneficios, anonimato y voluntariedad)",
                    "Tipos de faltas a la integridad científica: Plagio, Autoplagio/Doble publicación, Fabricación de datos y Falsificación de resultados",
                    "Criterios de autoría del ICMJE: 1) Contribución sustancial al diseño o análisis; 2) Redacción o revisión crítica; 3) Aprobación de la versión final; 4) Responsabilidad por todos los aspectos del trabajo"
                ],
                "practical_activity": "Redacta un protocolo de Consentimiento Informado formal para una investigación universitaria que contemple protección de datos, anonimato y cláusula de retiro voluntario."
            },
            {
                "title": "5.3 Selección de Revistas, Métricas de Impacto (Scopus/JCR) y Peer Review",
                "description": "Cómo elegir la revista adecuada, entender cuartiles (Q1-Q4), evitar revistas depredadoras y responder a revisores.",
                "theoretical_deepening": "Las revistas se clasifican en bases de datos indexadas según su impacto científico:\n- **Journal Citation Reports (JCR / Web of Science):** Journal Impact Factor (JIF).\n- **Scopus (Elsevier):** CiteScore y SCImago Journal Rank (SJR).\nSe dividen en **Cuartiles (Q1: top 25% más citado, Q2: 25-50%, Q3: 50-75%, Q4: 75-100%)**.\nEl proceso de **Revisión por Pares (Peer Review)** (generalmente Doble Ciego) culmina con veredictos: *Accept, Minor Revision, Major Revision, Reject*. Ante revisiones mayores, el autor debe redactar una **Carta de Respuesta (Rebuttal Letter)** respondiendo de forma cortés, exhaustiva y punto por punto cada observación de los revisores.",
                "key_takeaways": [
                    "Identificación de revistas depredadoras (*Predatory Journals*): Tiempos de aceptación inverosímiles (3 días), correos spam y cobros abusivos sin revisión real",
                    "Uso de herramientas de búsqueda de revistas: Elsevier JournalFinder, Springer Journal Suggester, IEEE Publication Recommender",
                    "Estructura de la Carta de Respuesta a Revisores: [Agradecimiento general] + [Resumen de cambios mayores] + [Tabla Punto por Punto: Comentario del Revisor -> Respuesta del Autor -> Modificación exacta con página y línea]"
                ],
                "practical_activity": "Simula la recepción de una crítica severa del 'Revisor 2' sobre la representatividad de tu muestra y redacta la respuesta profesional correspondiente para la carta de réplica al editor."
            }
        ],
        "course_materials": [
            {
                "title": "Estructura IMRyD y Plantilla de Artículo Científico (Manuscript Template)",
                "type": "Plantilla de Publicación",
                "icon": "fa-newspaper",
                "description": "Plantilla estándar en formato Word/LaTeX para estructurar Título, Abstract (250 palabras), IMRyD, Tablas APA 7ma ed. y disponibilidad de datos.",
                "action": "Descargar Plantilla IMRyD"
            },
            {
                "title": "Protocolo de Consentimiento Informado & Declaración COPE sobre IA",
                "type": "Formato Ético Institucional",
                "icon": "fa-shield-halved",
                "description": "Modelos para comités de bioética IRB, cláusulas de anonimato, no maleficencia y declaración explícita de herramientas de IA generativa.",
                "action": "Descargar Protocolo Bioético"
            },
            {
                "title": "Plantilla de Carta de Réplica Punto por Punto a Revisores (Rebuttal Letter)",
                "type": "Plantilla de Peer Review",
                "icon": "fa-envelope-open-text",
                "description": "Tabla formal para responder a dictámenes de revisión mayor/menor en revistas Scopus/JCR Q1-Q4 con cortesía y rigor.",
                "action": "Descargar Plantilla de Rebuttal"
            }
        ],
        "example_case": {
            "title": "Caso de Estudio Nivel 5: Carta de Réplica a Revisores (Scopus Q1 Journal)",
            "context": "El Revisor 1 solicita justificar por qué se utilizó un análisis de covarianza (ANCOVA) en lugar de un ANOVA simple.",
            "transformation": "Respuesta experta del Autor:\n'Agradecemos sinceramente la observación del Revisor 1 sobre el modelo estadístico. Hemos acogido su sugerencia y añadido una explicación explícita en la sección de Métodos (Página 9, Líneas 14-22). Se empleó un modelo ANCOVA controlando las calificaciones previas (Pretest) como covariable para neutralizar las diferencias basales entre los grupos intactos, aumentando así la precisión de la estimación del efecto del tratamiento ($F(1, 57) = 14.82, p < 0.001, \\eta_p^2 = 0.21$). Adjuntamos la nueva tabla comparativa en el manuscrito revisado.'"
        },
        "quiz": [
            {
                "question": "De acuerdo con el Comité Internacional de Editores de Revistas Médicas (ICMJE) y COPE, ¿puede un modelo de Inteligencia Artificial (ej. ChatGPT) figurar como coautor de un artículo científico?",
                "options": [
                    "Sí, siempre que haya escrito más del 50% del código o del texto.",
                    "No, porque las herramientas de IA no tienen personalidad jurídica, no pueden asumir responsabilidad ética sobre los datos ni declarar conflictos de interés; su uso debe declararse en la metodología.",
                    "Sí, siempre que la revista sea de acceso abierto.",
                    "Solo si se le paga una suscripción premium a la empresa desarrolladora."
                ],
                "correct_index": 1,
                "explanation": "Los organismos éticos internacionales establecen unánimemente que la autoría científica implica responsabilidad legal y ética intransferible, por lo que la IA no califica como autor."
            },
            {
                "question": "¿Qué representa que una revista científica esté clasificada en el Cuartil 1 (Q1) de Scopus o JCR?",
                "options": [
                    "Que es una revista nueva que sólo publica una vez al año.",
                    "Que se encuentra en el 25% superior con mayor impacto y número de citas recibidas dentro de su categoría temática internacional.",
                    "Que es una revista exclusiva para estudiantes de pregrado.",
                    "Que cobra una tarifa de publicación cuatro veces más alta que las demás."
                ],
                "correct_index": 1,
                "explanation": "Los cuartiles (Q1 a Q4) ordenan las revistas de una disciplina de mayor a menor impacto citacional; Q1 agrupa al 25% de revistas líderes en el mundo."
            }
        ]
    }
]


def get_all_levels():
    """Retorna la lista completa de niveles pedagógicos."""
    return LEVELS_DATA


def get_level_by_id(level_id):
    """Busca y retorna un nivel específico por su identificador."""
    for level in LEVELS_DATA:
        if level["id"] == level_id:
            return level
    return None
