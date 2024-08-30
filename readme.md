# Trabajo Final ITBA - NLP
Este repositorio contiene el trabajo final realizado para la Certificacion Profesional en Procesamiento de Lenguaje Natural (NLP) en el Instituto Tecnológico de Buenos Aires (ITBA).
El objetivo principal de este proyecto es desarrollar modelos y técnicas avanzadas en NLP aplicados a un conjunto de datos específicos para la **Detección de Tópicos y clasificación**.

El proyecto busca desarrollar un sistema para identificar y agrupar tópicos en textos de noticias recibidos diariamente. El sistema debe:

1) Detectar y agrupar tópicos diarios, considerando su evolución día a día.
2) Clasificar nuevos textos durante el día dentro de los tópicos ya existentes.
3) Extraer entidades y palabras clave y realizar análisis de sentimiento en los textos.

El modelo utilizará embeddings para la detección y agrupación de tópicos, y almacenará los resultados en una base de datos compatible con vectores.

# Detalles de Códigos

El objetivo de los cuatro códigos fue desarrollar y mejorar un sistema automatizado para la detección y clasificación de tópicos en documentos de texto, utilizando técnicas avanzadas de procesamiento de lenguaje natural (NLP) y almacenamiento vectorial.

1) **TP_NLP_1_Topicos_1dia:** realiza un análisis detallado de la detección y agrupación de tópicos en noticias de un solo día, utilizando técnicas avanzadas de NLP como embeddings y clustering. Almacena los tópicos en una base de datos vectorial para facilitar la clasificación futura y realiza una extracción de entidades, palabras clave y sentimiento en ese contexto diario.

2) **TP_NLP_2_ProcesamientoDiario:** Amplio el sistema inicial al implementar un procesamiento diario de tópicos, almacenando y comparando tópicos entre diferentes días. Se buscó asegurar la continuidad y actualización del análisis a lo largo del tiempo.

3) **TP_NLP_3_MergeModels:** Se abordo el problema de una manera alternativa. Aquí se entrena modelos de detección de tópicos diariamente, se fusionan esos modelos para identificar y agrupar tópicos similares a lo largo de múltiples días, y se almacenan los embeddings de los tópicos en OpenSearch para realizar búsquedas eficientes.

4) **TP_NLP_4_ChromaDb:** Se probo otro tipo base de datos vectorial (ChromaDB) para almacenar los embeddings de los tópicos.

En conjunto, estos códigos construyen un sistema robusto para la clasificación de textos, que puede manejar grandes volúmenes de datos diarios, identificar patrones temáticos y ofrecer análisis detallados sobre el contenido textual.



Instalación
``` bash
conda create -n topics python=3.11
conda activate topics

pip install -r requirements
```
