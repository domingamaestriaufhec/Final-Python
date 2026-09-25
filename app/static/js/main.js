/**
 * InvestigaLab - Lógica de Interactividad Frontend
 */

document.addEventListener("DOMContentLoaded", () => {
    // 1. Funcionalidad de Copiado al Portapapeles
    initCopyButtons();

    // 2. Simulador de Matriz de Consistencia Científica (si está en la página /matriz)
    initMatrixBuilder();

    // 3. Pestaña interactiva de Pipeline Archify (si está en la página /pipeline)
    initPipelineInspector();

    // 4. Explorador interactivo de los 5 Niveles (en Landing Page o vistas estáticas)
    initLevelsExplorer();

    // 5. Verificador universal de Quizzes de autoevaluación
    initQuizHandlers();
});

/**
 * Inicializa los botones de copiado rápido en bloques de código y terminal
 */
function initCopyButtons() {
    const copyButtons = document.querySelectorAll(".copy-btn");
    copyButtons.forEach((btn) => {
        btn.addEventListener("click", () => {
            const textToCopy = btn.getAttribute("data-copy") || btn.closest(".code-line").innerText.replace("$", "").trim();
            navigator.clipboard.writeText(textToCopy).then(() => {
                const originalHtml = btn.innerHTML;
                btn.innerHTML = '<i class="fa-solid fa-check" style="color: #10b981;"></i> Copiado!';
                btn.style.color = "#10b981";
                setTimeout(() => {
                    btn.innerHTML = originalHtml;
                    btn.style.color = "";
                }, 2000);
            });
        });
    });
}

/**
 * Constructor interactivo de la Matriz de Consistencia Metodológica
 */
function initMatrixBuilder() {
    const matrixForm = document.getElementById("matrixForm");
    if (!matrixForm) return;

    const inputTema = document.getElementById("temaInvestigacion");
    const inputProblema = document.getElementById("problemaGeneral");
    const inputObjetivo = document.getElementById("objetivoGeneral");
    const inputHipotesis = document.getElementById("hipotesisGeneral");
    const inputVarIndep = document.getElementById("varIndependiente");
    const inputVarDep = document.getElementById("varDependiente");
    const selectEnfoque = document.getElementById("enfoqueMetodologico");
    const selectDiseno = document.getElementById("disenoEstudio");

    const outTema = document.getElementById("outTema");
    const outProblema = document.getElementById("outProblema");
    const outObjetivo = document.getElementById("outObjetivo");
    const outHipotesis = document.getElementById("outHipotesis");
    const outVariables = document.getElementById("outVariables");
    const outMetodologia = document.getElementById("outMetodologia");

    function updatePreview() {
        if (outTema) outTema.textContent = inputTema.value.trim() || "Por definir...";
        if (outProblema) outProblema.textContent = inputProblema.value.trim() || "¿Cuál es la relación entre...";
        if (outObjetivo) outObjetivo.textContent = inputObjetivo.value.trim() || "Determinar la relación entre...";
        if (outHipotesis) outHipotesis.textContent = inputHipotesis.value.trim() || "Existe una relación significativa entre...";
        
        if (outVariables) {
            const vi = inputVarIndep.value.trim() || "Variable 1";
            const vd = inputVarDep.value.trim() || "Variable 2";
            outVariables.innerHTML = `<strong>VI:</strong> ${vi} <br><strong>VD:</strong> ${vd}`;
        }

        if (outMetodologia) {
            outMetodologia.textContent = `Enfoque: ${selectEnfoque.value} | Diseño: ${selectDiseno.value}`;
        }
    }

    // Escuchar cambios en todos los inputs
    [inputTema, inputProblema, inputObjetivo, inputHipotesis, inputVarIndep, inputVarDep, selectEnfoque, selectDiseno].forEach(el => {
        if (el) el.addEventListener("input", updatePreview);
    });

    // Cargar ejemplo predeterminado
    const btnCargarEjemplo = document.getElementById("btnCargarEjemplo");
    if (btnCargarEjemplo) {
        btnCargarEjemplo.addEventListener("click", () => {
            inputTema.value = "Impacto del Aprendizaje Basado en Proyectos (ABP) en el Rendimiento de Programación";
            inputProblema.value = "¿En qué medida la metodología ABP mejora la capacidad de resolución de algoritmos en estudiantes universitarios de primer año?";
            inputObjetivo.value = "Determinar la efectividad del método ABP en el rendimiento académico y la resolución de algoritmos en estudiantes universitarios.";
            inputHipotesis.value = "Los estudiantes sometidos al método ABP obtienen calificaciones significativamente superiores (p < 0.05) que aquellos bajo enseñanza tradicional.";
            inputVarIndep.value = "Metodología ABP (Intervención Pedagógica)";
            inputVarDep.value = "Rendimiento en Programación y Resolución Algorítmica";
            selectEnfoque.value = "Cuantitativo";
            selectDiseno.value = "Cuasi-experimental (Pretest-Postest con Grupo Control)";
            updatePreview();
        });
    }

    // Exportar a Markdown
    const btnExportarMd = document.getElementById("btnExportarMd");
    if (btnExportarMd) {
        btnExportarMd.addEventListener("click", () => {
            const mdContent = `# Matriz de Consistencia Científica\n\n` +
                `**Tema:** ${inputTema.value}\n\n` +
                `| Elemento Metodológico | Descripción |\n` +
                `| :--- | :--- |\n` +
                `| **Problema General** | ${inputProblema.value} |\n` +
                `| **Objetivo General** | ${inputObjetivo.value} |\n` +
                `| **Hipótesis General** | ${inputHipotesis.value} |\n` +
                `| **Variable Independiente (VI)** | ${inputVarIndep.value} |\n` +
                `| **Variable Dependiente (VD)** | ${inputVarDep.value} |\n` +
                `| **Enfoque** | ${selectEnfoque.value} |\n` +
                `| **Diseño** | ${selectDiseno.value} |\n\n` +
                `*Generado con InvestigaLab - Escuela de Metodología de la Investigación Científica.*`;

            navigator.clipboard.writeText(mdContent).then(() => {
                alert("✅ Matriz copiada en formato Markdown al portapapeles.");
            });
        });
    }
}

/**
 * Interacción y visualización de la vista Pipeline Archify
 */
function initPipelineInspector() {
    const stageCards = document.querySelectorAll(".stage-card");
    if (!stageCards.length) return;

    stageCards.forEach(card => {
        card.addEventListener("mouseenter", () => {
            card.style.borderColor = "#6366f1";
            card.style.boxShadow = "0 8px 30px rgba(99, 102, 241, 0.25)";
        });
        card.addEventListener("mouseleave", () => {
            card.style.borderColor = "";
            card.style.boxShadow = "";
        });
    });
}

/**
 * Lógica del Explorador interactivo de los 5 niveles en la Landing Page
 */
function initLevelsExplorer() {
    const tabButtons = document.querySelectorAll(".level-tab-btn");
    const levelPanels = document.querySelectorAll(".level-panel");
    const openLevelBtns = document.querySelectorAll(".open-level-btn");

    function activateLevel(targetLevelId) {
        if (!targetLevelId) return;

        // Actualizar botones de pestaña
        tabButtons.forEach(btn => {
            const btnTarget = btn.getAttribute("data-target-level");
            if (btnTarget === targetLevelId) {
                btn.classList.add("active");
                btn.classList.remove("btn-secondary");
                btn.classList.add("btn-primary");
            } else {
                btn.classList.remove("active");
                btn.classList.add("btn-secondary");
                btn.classList.remove("btn-primary");
            }
        });

        // Actualizar paneles de contenido
        levelPanels.forEach(panel => {
            if (panel.id === `panel-${targetLevelId}`) {
                panel.style.display = "block";
                panel.classList.add("active-panel");
            } else {
                panel.style.display = "none";
                panel.classList.remove("active-panel");
            }
        });
    }

    tabButtons.forEach(btn => {
        btn.addEventListener("click", (e) => {
            e.preventDefault();
            const target = btn.getAttribute("data-target-level");
            activateLevel(target);
        });
    });

    openLevelBtns.forEach(btn => {
        btn.addEventListener("click", (e) => {
            e.preventDefault();
            const target = btn.getAttribute("data-target-level");
            activateLevel(target);
            const explorerElement = document.getElementById("explorador-niveles");
            if (explorerElement) {
                explorerElement.scrollIntoView({ behavior: "smooth", block: "start" });
            }
        });
    });

    // Detectar si la URL tiene hash de nivel específico (#nivel-principiante, etc.)
    const hash = window.location.hash.replace("#", "");
    if (hash.startsWith("nivel-")) {
        const levelId = hash.replace("nivel-", "");
        activateLevel(levelId);
    }
}

/**
 * Manejador universal de respuestas en Quizzes interactivos
 */
function initQuizHandlers() {
    const checkButtons = document.querySelectorAll(".check-quiz-btn");
    checkButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            const levelId = btn.getAttribute("data-level");
            const qIdx = btn.getAttribute("data-qidx");
            const correctIdx = parseInt(btn.getAttribute("data-correct"), 10);
            const explanation = btn.getAttribute("data-explanation");
            const feedbackDiv = document.getElementById(`feedback_${levelId}_${qIdx}`);

            const selectedOption = document.querySelector(`input[name="quiz_${levelId}_${qIdx}"]:checked`);
            if (!selectedOption) {
                if (feedbackDiv) {
                    feedbackDiv.style.display = "block";
                    feedbackDiv.style.background = "rgba(245, 158, 11, 0.15)";
                    feedbackDiv.style.color = "#fbbf24";
                    feedbackDiv.style.border = "1px solid rgba(245, 158, 11, 0.3)";
                    feedbackDiv.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i> Por favor selecciona una opción antes de verificar.';
                }
                return;
            }

            const chosenIdx = parseInt(selectedOption.value, 10);
            if (feedbackDiv) {
                feedbackDiv.style.display = "block";
                if (chosenIdx === correctIdx) {
                    feedbackDiv.style.background = "rgba(16, 185, 129, 0.15)";
                    feedbackDiv.style.color = "#6ee7b7";
                    feedbackDiv.style.border = "1px solid rgba(16, 185, 129, 0.4)";
                    feedbackDiv.innerHTML = `<strong><i class="fa-solid fa-circle-check"></i> ¡Excelente y Correcto!</strong><br>${explanation}`;
                } else {
                    feedbackDiv.style.background = "rgba(239, 68, 68, 0.15)";
                    feedbackDiv.style.color = "#fca5a5";
                    feedbackDiv.style.border = "1px solid rgba(239, 68, 68, 0.4)";
                    feedbackDiv.innerHTML = `<strong><i class="fa-solid fa-circle-xmark"></i> Respuesta incorrecta.</strong><br>${explanation}`;
                }
            }
        });
    });
}
