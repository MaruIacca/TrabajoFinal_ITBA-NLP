from opensearchpy import helpers
from opensearchpy import Float, OpenSearch, Field, Integer, Document, Keyword, Text, Boolean, DenseVector, Nested, Date, Object, connections, InnerDoc, helpers


import re, os
import unicodedata
from functools import wraps
from dotenv import load_dotenv

from sklearn.metrics.pairwise import cosine_similarity
from opensearch_data_model import TopicKeyword
from collections import defaultdict 
from collections import Counter
import pandas as pd
import numpy as np

SPANISH_STOPWORDS = list(pd.read_csv('data/spanish_stop_words.csv' )['stopwords'].values)

def plot_top_words(model, feature_names, n_top_words, title):
    fig, axes = plt.subplots(2, 5, figsize=(30, 15), sharex=True)
    axes = axes.flatten()
    for topic_idx, topic in enumerate(model.components_):
        top_features_ind = topic.argsort()[-n_top_words:]
        top_features = feature_names[top_features_ind]
        weights = topic[top_features_ind]

        ax = axes[topic_idx]
        ax.barh(top_features, weights, height=0.7)
        ax.set_title(f"Topic {topic_idx +1}", fontdict={"fontsize": 30})
        ax.tick_params(axis="both", which="major", labelsize=20)
        for i in "top right left".split():
            ax.spines[i].set_visible(False)
        fig.suptitle(title, fontsize=40)

    plt.subplots_adjust(top=0.90, bottom=0.05, wspace=0.90, hspace=0.3)
    plt.show()



def best_document(topic, topic_model, docs_embedding, id_data, title_data, data) -> str:
    """
    Función que devuelve el texto del documento mas cercano al topico elegido
    """
    try:       
        # Obtenemos la matriz de similitud coseno entre topicos y documentos
        sim_matrix = cosine_similarity(topic_model.topic_embeddings_, docs_embedding)

        best_doc_index = sim_matrix[topic + 1].argmax()      

        return id_data[best_doc_index], title_data[best_doc_index], data[best_doc_index]

    except:
        return None, "None", "None"