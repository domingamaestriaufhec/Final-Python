# 🔬 04. Currículo Pedagógico de Metodología de la Investigación Científica

Este documento sintetiza la fundamentación epistemológica, las fórmulas matemáticas y los objetivos de aprendizaje de los 5 niveles del curso en **InvestigaLab**.

---

## 🏛️ 1. Epistemología y Autores Clásicos

| Autor | Obra Principal | Aporte Epistemológico Central | Nivel del Curso |
|---|---|---|---|
| **Mario Bunge** | *La ciencia: su método y su filosofía* (1960) | Distinción de ciencias formales vs fácticas y las 15 características de la ciencia | Nivel 1 & 5 |
| **Karl R. Popper** | *La lógica de la investigación científica* (1934) | Principio de Falsabilidad como criterio de demarcación; crítica al inductivismo | Nivel 1 & 2 |
| **R. Hernández-Sampieri** | *Metodología de la investigación* (2018) | Rutas cuantitativa, cualitativa y mixta; operacionalización de variables | Nivel 1, 2, 3, 4 |
| **Fred N. Kerlinger** | *Investigación del comportamiento* (2002) | Principio MAXMINCON, varianza experimental y validez psicométrica | Nivel 3 & 4 |
| **John W. Creswell** | *Research Design* (2018) | Diseños metodológicos mixtos, tamaño del efecto y ética de la investigación | Nivel 3, 4, 5 |
| **Thomas S. Kuhn** | *La estructura de las revoluciones científicas* (1962) | Paradigmas, ciencia normal, anomalías y rupturas científicas | Nivel 1 & 5 |

---

## 📐 2. Fórmulas Matemáticas y Modelos Estadísticos del Curso

### A. Cálculo del Tamaño de Muestra para Poblaciones Finitas (Nivel 3)
Para estimar proporciones poblacionales con un nivel de confianza $Z$ y margen de error $e$:

$$n = \frac{N \cdot Z^2 \cdot p \cdot q}{e^2 \cdot (N - 1) + Z^2 \cdot p \cdot q}$$

* $N$: Tamaño de la población.
* $Z$: Valor crítico de la distribución normal ($Z = 1.96$ para 95% de confianza; $Z = 2.58$ para 99%).
* $p$: Probabilidad de ocurrencia esperada ($p = 0.5$ para máxima varianza).
* $q = 1 - p = 0.5$.
* $e$: Margen de error admisible (ej. $0.05$ para $\pm 5\%$).

---

### B. Coeficiente Alfa de Cronbach ($\alpha$) de Consistencia Interna (Nivel 4)
Para instrumentos psicométricos en escala de tipo Likert:

$$\alpha = \frac{K}{K - 1} \left( 1 - \frac{\sum s_i^2}{s_t^2} \right)$$

* $K$: Número de ítems del cuestionario.
* $s_i^2$: Varianza de las respuestas al ítem $i$.
* $s_t^2$: Varianza de la puntuación total de los encuestados.
* **Criterio de Aceptación:** $\alpha \ge 0.70$ (Aceptable), $\alpha \ge 0.80$ (Bueno), $\alpha \ge 0.90$ (Excelente).

---

### C. Coeficiente V de Aiken para Validez de Contenido por Jueces (Nivel 4)
$$V = \frac{S}{n(c - 1)} = \frac{\sum (r_i - l)}{n(c - 1)}$$

* $r_i$: Calificación asignada por el juez $i$.
* $l$: Calificación mínima posible en la escala.
* $c$: Número de valores posibles de la escala.
* $n$: Número total de jueces expertos.
* **Criterio:** $V > 0.80$ con significancia estadística $p < 0.05$.

---

### D. Tamaño del Efecto: $d$ de Cohen (Nivel 4)
$$d = \frac{\bar{X}_1 - \bar{X}_2}{s_{\text{agrupada}}}$$

* $d \approx 0.20$: Efecto pequeño.
* $d \approx 0.50$: Efecto mediano.
* $d \ge 0.80$: Efecto grande o sustantivo.
