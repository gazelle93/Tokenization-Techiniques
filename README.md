# Overview
- Tokenization is the first step in NLP where a piece of text such as a sentence or document is split into small pieces called tokens where the most widely used methods of tokenization are word-based, character-based, and subword-based tokenization. Word-based tokenization technique is the most commonly used technique. The text is broken down into word levels using a selected delimiter. Character-based tokenization is a technique that separates the text based on character. A distinctive characteristic of character-level tokenization is that it significantly reduces the size of the vocabulary. Also, this tokenization technique is able to handle Out Of Vocabulary (OOV) issues. OOV issue represents when the new words that appeared at the test step are not foreshadowed at the training step and do not exist in the vocabulary. This is a crucial problem for the systems that leverage word embeddings because OOV words cannot be converted to a real-value vector as a representation of a token in the vector space. Subword-based tokenization technique is most widely adopted in Transformer-based architectures such as WordPiece and Byte-Pair Encoding. This project aims to implement word-based, character-based and subword-based tokenization techniques.

# Brief description
- word_base_tokenization.py
> Output format
> - output: Tokenized result of a given text. (list)
- character_base_tokenization.py
> Output format
> - output: Tokenized result of a given text. (list)
- subword_base_tokenization.py
> Output format
> - output: Tokenized result of a given text. (list)

# Prerequisites
- argparse
- stanza
- spacy
- nltk
- gensim

# Parameters
- tokenization(str, defaults to "word"): Type of tokenization techinque.
- nlp_pipeline(str, defaults to "stanza"): NLP preprocessing pipeline.
- num_merges(int, defaults to 20): The number of merges of the BPE technique.

# References
- Stanza: Qi, P., Zhang, Y., Zhang, Y., Bolton, J., & Manning, C. D. (2020). Stanza: A Python natural language processing toolkit for many human languages. arXiv preprint arXiv:2003.07082.
- Spacy: Matthew Honnibal and Ines Montani. 2017. spaCy 2: Natural language understanding with Bloom embeddings, convolutional neural networks and incremental parsing. To appear (2017).
- NLTK: Bird, Steven, Edward Loper and Ewan Klein (2009). Natural Language Processing with Python.  O'Reilly Media Inc.
- Gensim: Rehurek, R., & Sojka, P. (2010). Software framework for topic modelling with large corpora. In In Proceedings of the LREC 2010 workshop on new challenges for NLP frameworks.
- BPE algorithm in NMT: Sennrich, R., Haddow, B., & Birch, A. (2015). Neural machine translation of rare words with subword units. arXiv preprint arXiv:1508.07909.
- BPE algorithm: Gage, P. (1994). A new algorithm for data compression. C Users Journal, 12(2), 23-38.
