from itertools import product
from collections import Counter


def chunked_dna_data_list(raw_string_data, chunk_length):
  # break the original string into a list of chunk_length segments
  return [
    raw_string_data[chunk_length*i:chunk_length*i + chunk_length]
    for i in range(int(len(raw_string_data)/chunk_length))
  ]


def letter_combinations(letters, word_length):
  # use the cartesian product to return every possible ordering of the input letters
  return [
    ''.join(combination)
    for combination in product(letters, repeat=word_length)
  ]


def feature_vector(dna_chunk, word_combinations, word_length):
  # the counter type counts occurences in the underlying list which contains exactly the cut dna_chunk
  chunk_words_counter = Counter([
    word
    for word in (
      # cut the original dna_chunk into words of length word_length
      dna_chunk[i:i + word_length]
      for i in range(0, len(dna_chunk), word_length)
    )
    if len(word) == word_length
  ])
  return {
    # use the comprehension to build a dictionary which contains 0s for missing words
    # counter type returns zero for keys which are not in the counter
    # this gives us a full pow(4, word_length)-dimension feature vector
    word : chunk_words_counter[word]
    for word in word_combinations
  }
