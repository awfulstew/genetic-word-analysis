from itertools import product
from collections import Counter

def chunked_dna_data_list(raw_string_data, chunk_length):
  return [
    raw_string_data[chunk_length*i:chunk_length*i + chunk_length]
    for i in range(int(len(raw_string_data)/chunk_length))
  ]


def letter_combinations(letters, word_length):
  return [
    ''.join(combination)
    for combination in product(letters, repeat=word_length)
  ]


def feature_vector(dna_chunk, word_combinations, word_length):
  chunk_words_counter = Counter([
    word
    for word in (
      dna_chunk[i:i + word_length]
      for i in range(0, len(dna_chunk), word_length)
    )
    if len(word) == word_length
  ])
  return { 
    word : chunk_words_counter[word]
    for word in word_combinations
  }
