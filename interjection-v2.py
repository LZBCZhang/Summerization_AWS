# -*- coding: utf-8 -*-

import json
import re
import string
import io
from nltk.tokenize import word_tokenize, sent_tokenize
import skipthoughts
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min

idict = {
    'language': 'fr',
    'interjections': ['ah', 'eh', 'oh', 'ha', 'hi', 'hue', 'ohé', 'holà', 'ouf', 'euh', 'voilà'] 
}

sentencesFilteredList = []
interjections = set(idict['interjections'])

# Function 1
#   input: file json
#   output: list of transcripts : 
#       ["Février Bush et après je bouge. Voilà, ça marche par euh bonjour,", "toto va au cmarché"]

# Function 2 
#   input: list of transcripts
#   output: list of sentences filtered

# Function 3
#   input: null
#   output: tokenize the output of Function 2 and print the result


# Function 1 
def openFile(fileS):

    with io.open(fileS, mode='r', encoding='utf-8') as f:
        data = f.readlines()

    return data

def splitSpk(data):

    result = []
    for i in range(len(data)):
        if data[i] != '\n':
            line = re.sub(r"[\(\[].*?[\)\]]", "", data[i])
            line = line[1:]
            result.append(line.split(':'))
    
    return result

def printTable(data):
    for i in range(len(data)):
        print(data[i])
        print('-----------------------------------')

# Function 2
def splitTxt(keyValue):
     
    textsplitted = keyValue.split('.')
    for sentenceItem in textsplitted:
        filtertedWords = []
        indexDelete = -1
        word_tokens = word_tokenize(sentenceItem)
        for wIndex in range(len(word_tokens)):
            w = word_tokens[wIndex]
            if w.lower() in interjections:
                if (wIndex - 1) >= 0:
                    if not word_tokens[wIndex - 1].isalpha() and not word_tokens[wIndex + 1].isalpha():
                        indexDelete = wIndex + 1
                else:
                    if not word_tokens[wIndex + 1].isalpha():
                        indexDelete = wIndex + 1
            else:
                if wIndex != indexDelete and indexDelete != 0:
                    filtertedWords.append(w)

        sentencesFilteredList.append(" ".join(filtertedWords))

# Function 3
def sumarization():
    # Tokenize the sentences
    contentsFilted = ". ".join(sentencesFilteredList)
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
    print(summary)
        
printTable(splitSpk(openFile('ObamaOutput.json.txt')))

#splitTxt(openFile('MacronOutput.json'))
#sumarization()