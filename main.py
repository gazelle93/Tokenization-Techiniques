from word_base_tokenization import word_tokenization
from character_base_tokenization import character_tokenization
from subword_base_tokenization import bpe_processing, encoding

import random

sample_text = """My lovely dog likes eating sausage.
My cat likes eating salmon.
Jane's koala likes eating eucalyptus leaves.
Jack's panda likes eating bamboo."""

listofsent = sample_text.split("\n")

idx = random.randint(0,len(listofsent)-1)
print(listofsent[idx])

# Word-based tokenization
print(word_tokenization(listofsent[idx], None, True))
print(word_tokenization(listofsent[idx], "stanza", True))
print(word_tokenization(listofsent[idx], "spacy", True))
print(word_tokenization(listofsent[idx], "nltk", True))
print(word_tokenization(listofsent[idx], "gensim", True))

# Character-based tokenization
print(character_tokenization(listofsent[idx], True))

# Subword-based tokenization
num_merges = 20
bpe_codes = bpe_processing(listofsent, num_merges)
print(encoding(listofsent[idx]))
