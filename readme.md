# Trabajo Final ITBA - NLP
Este repositorio contiene el trabajo final realizado para la Certificacion Profesional en Procesamiento de Lenguaje Natural (NLP) en el Instituto Tecnológico de Buenos Aires (ITBA).
El objetivo principal de este proyecto es desarrollar modelos y técnicas avanzadas en NLP aplicados a un conjunto de datos específicos para la **Detección de Tópicos y clasificación**.

El proyecto busca desarrollar un sistema para identificar y agrupar tópicos en textos de noticias recibidos diariamente. El sistema debe:

1) Detectar y agrupar tópicos diarios, considerando su evolución día a día.
2) Clasificar nuevos textos durante el día dentro de los tópicos ya existentes.
3) Extraer entidades y palabras clave y realizar análisis de sentimiento en los textos.

El modelo utilizará embeddings para la detección y agrupación de tópicos, y almacenará los resultados en una base de datos compatible con vectores.


Instalación
``` bash
conda create -n topics python=3.11
conda activate topics

pip install -r requirements
```
