import random
import argparse

from word_base_tokenization import word_tokenization
from character_base_tokenization import character_tokenization
from subword_base_tokenization import bpe_processing, encoding


def main(args):
    sample_text = """My lovely dog likes eating sausage.
    My cat likes eating salmon.
    Jane's koala likes eating eucalyptus leaves.
    Jack's panda likes eating bamboo."""

    listofsent = sample_text.split("\n")

    idx = random.randint(0,len(listofsent)-1)
    print("Input text: {}".format(listofsent[idx]))

    if args.tokenization == "word":
        # Word-based tokenization
        print("Word-based tokenization")
        print("None\n->", word_tokenization(listofsent[idx], None, True))
        print("Stanza\n->", word_tokenization(listofsent[idx], "stanza", True))
        print("Spacy\n->", word_tokenization(listofsent[idx], "spacy", True))
        print("Nltk\n->", word_tokenization(listofsent[idx], "nltk", True))
        print("Gensim\n->", word_tokenization(listofsent[idx], "gensim", True))

    if args.tokenization == "char":
        # Character-based tokenization
        print("Character-based tokenization")
        print(character_tokenization(listofsent[idx], True))

    # Subword-based tokenization
    if args.tokenization == "subword":
        bpe_codes = bpe_processing(listofsent, args.num_merges)
        print("SubWord-based tokenization (BPE)")
        print(encoding(listofsent[idx], bpe_codes))
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--tokenization", default="word", type=str, help="The type of tokenization techinque.")
    parser.add_argument("--nlp_pipeline", default="stanza", type=str, help="NLP preprocessing pipeline.")
    parser.add_argument("--num_merges", default=20, type=int, help="The number of merges of BPE techinque.")
    
    args = parser.parse_args()

    main(args)
