# Predicción de Resultados en League of Legends con Inteligencia Artificial

Este proyecto tiene como objetivo predecir la victoria del equipo azul en partidas clasificatorias de **League of Legends**, utilizando algoritmos de aprendizaje automático sobre estadísticas recolectadas durante los primeros 10 minutos de juego.

## 📊 Dataset

Se utilizó el dataset **[League of Legends Diamond Ranked Games (10 min)](https://www.kaggle.com/datasets/bobbyscience/league-of-legends-diamond-ranked-games-10-min)**, que contiene estadísticas detalladas de 9,879 partidas de la liga Diamante.

- 📂 `data/high_diamond_ranked_10min.csv`: Dataset original.
- 📂 `data/data_normalizado_limpio.csv`: Dataset limpio y normalizado (tras preprocesamiento en R).

### Características del dataset

- **Variables:** 40
- **Muestra:** 9,879 partidas
- **Estadísticas por equipo:** asesinatos, asistencias, oro acumulado, monstruos derrotados, objetivos estructurales, entre otras.
- **Variable objetivo:** `blueWins` (1 si el equipo azul gana, 0 si pierde)

## 🧪 Proceso de Desarrollo

### 1. Preprocesamiento de Datos

- Normalización y limpieza del dataset usando R.
- 📂 `code/Normalizacion.R`: Código de limpieza y normalización.

### 2. Entrenamiento y Evaluación de Modelos

Se entrenaron tres modelos de clasificación para predecir el resultado:

- **Red Neuronal Artificial (RNA)**  
- **Random Forest**
- **Support Vector Machine (SVM)**

📂 `code/EvaluacionDeModelos.py`: Contiene el entrenamiento, validación y evaluación de los tres modelos.

### 3. Predicción

📂 `code/LoL_predicter.py`: Aplicación que permite ingresar estadísticas de una partida y predecir si el equipo azul ganará.

## 🧠 Modelos Evaluados

| Modelo         | Precisión Promedio |
|----------------|--------------------|
| SVM            | 72.93%             |
| Random Forest  | 71.81%             |
| RNA            | 69.08% (var. 51–71%) |

Aunque el modelo SVM alcanzó mayor precisión, la RNA demostró mayor capacidad de generalización en partidas con datos más complejos.

## 📈 Visualizaciones

Se generaron diversos gráficos para explorar el comportamiento de las métricas:

- Heatmap de correlación entre variables y `blueWins`.
- Distribución de KDA (Kill-Death-Assist ratio) por equipo.
- Relación entre KDA y oro acumulado.

> Las visualizaciones y el análisis exploratorio se utilizaron para definir las variables más relevantes para la predicción.

## 💡 Conclusiones

- Es posible predecir la victoria del equipo azul con modelos de IA utilizando métricas de los primeros 10 minutos.
- RNA es el modelo más equilibrado para evitar sesgos, aunque su precisión varía más que otros modelos.
- Para mejorar el rendimiento, podría extenderse el análisis a otros intervalos temporales de la partida.

## 🚀 Futuras Mejoras

- Incorporación de datos de fases medias y tardías del juego.
- Despliegue de una API REST que reciba datos en tiempo real.
- Integración en plataformas de análisis estratégico para jugadores competitivos.

## 📚 Referencias

- Riot Games, League of Legends Wiki, Kaggle Dataset por Bobby Science.
- Velicias Barquín (2023), *Diseño de un sistema inteligente para la predicción de partidas en League of Legends*.

---

**Autores:**  
Rodrigo Alejandro Meza Polo (U202224016)  
Liam Mikael Quino Neff (U20221E167)  
Universidad Peruana de Ciencias Aplicadas  
Curso: Inteligencia Artificial – Sección CC63
