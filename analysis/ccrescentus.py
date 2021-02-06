from . import helpers
import requests

url = 'http://www.ihes.fr/~zinovyev/pcadg/ccrescentus.fa'

def ccresentus_dna_chunks(chunk_length):
  # fetch the dna sequence of cresentus
  response_iter = requests.get(url).iter_lines()
  # skip the first line of the response since it just has a header name
  next(response_iter)

  # generate raw data string from response text
  raw_data_string = ''
  for line in response_iter:
    raw_data_string += line.decode("utf-8")

  # return the raw data broken up into chunks
  return helpers.chunked_dna_data_list(raw_data_string, chunk_length)