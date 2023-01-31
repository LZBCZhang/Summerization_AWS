from nltk.tokenize import sent_tokenize
import skipthoughts
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min

def sumarization(sentencesFilteredList):
    # Tokenize the sentences
    contentsFilted = " ".join(sentencesFilteredList)
    sentences = sent_tokenize(contentsFilted)

    # Skip-thoughts encoding
    model = skipthoughts.load_model()
    encoder = skipthoughts.Encoder(model)
    encoded = encoder.encode(sentences)

    # Clustering 
    n_clusters = int(np.ceil(len(encoded) ** 0.5))
    kmeans = KMeans(n_clusters = n_clusters)
    kmeans = kmeans.fit(encoded)

    # Sumarization
    avg = []
    for j in range(n_clusters):
        idx = np.where(kmeans.labels_ == j)[0]
        avg.append(np.mean(idx))
    closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, encoded)
    ordering = sorted(range(n_clusters), key=lambda k: avg[k])
    summary = ' '.join([sentences[closest[idx]] for idx in ordering])
    return summary