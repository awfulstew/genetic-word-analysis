from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from . import helpers
from . import ccrescentus
import pandas as pd
import matplotlib.pyplot as plt

def pca_analysis():
  # get out chunks of dna that we want to analyze
  dna_chunks = ccrescentus.ccresentus_dna_chunks(300)
  plt.figure(figsize=(12, 12))

  # run pca for each word length from one to four
  for word_length in range(1, 5):
    # generate the possible set of words
    possible_words = helpers.letter_combinations('acgt', word_length)
    feature_vectors = [
      helpers.feature_vector(dna_chunk, possible_words, word_length)
      for dna_chunk in dna_chunks
    ]
    data_frame = pd.DataFrame(feature_vectors)

    # run pca to cut down to two dimensions
    pca_data = PCA(n_components=2).fit_transform(data_frame)

    # plot the letter graph so that we can check it
    plt.subplot(2,2, word_length)
    plt.tight_layout()
    plt.scatter(pca_data[:, 0], pca_data[:, 1], marker=".")
    plt.title(f'{word_length}-letter long words')
  
  plt.show()

def kmeans_analysis():
  # get out chunks of dna that we want to analyze
  dna_chunks = ccrescentus.ccresentus_dna_chunks(300)
  plt.figure(figsize=(13, 8))

  # generate the possible set of words with length 3
  possible_words = helpers.letter_combinations('acgt', 3)
  feature_vectors = [
    helpers.feature_vector(dna_chunk, possible_words, 3)
    for dna_chunk in dna_chunks
  ]
  data_frame = pd.DataFrame(feature_vectors)
  scaled_data = StandardScaler().fit_transform(data_frame)
  pca_data = PCA(n_components=2).fit_transform(scaled_data)

  # lets try cluster for six or seven clusters
  for cluster_count in range(6, 8):
    coloring = KMeans(n_clusters=cluster_count, random_state=0).fit_predict(scaled_data)
    plt.subplot(1,2,(cluster_count - 5))
    plt.tight_layout() 
    plt.scatter(pca_data[:, 0], pca_data[:, 1], c=coloring, marker=".")
    plt.title(f'k-means with k={cluster_count}')

  plt.show()