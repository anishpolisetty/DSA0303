"""
DSA03 – Natural Language Processing
Program 17: Access WordNet to explore word meanings and synsets.

Install: pip install nltk
Download once:
  import nltk
  nltk.download('wordnet')
  nltk.download('omw-1.4')
"""
import nltk
from nltk.corpus import wordnet as wn

def explore_word(word):
    synsets = wn.synsets(word)
    if not synsets:
        print("No WordNet synsets found.")
        return

    print(f"Word: {word}")
    for index, synset in enumerate(synsets, start=1):
        print(f"\n{index}. Synset: {synset.name()}")
        print("   Definition:", synset.definition())
        print("   Examples:", synset.examples() or "None")
        print("   Lemmas:", [lemma.name() for lemma in synset.lemmas()])

if __name__ == "__main__":
    try:
        explore_word(input("Enter a word: ").strip().lower() or "bank")
    except LookupError:
        print("WordNet data is missing. Run:")
        print("import nltk")
        print("nltk.download('wordnet')")
        print("nltk.download('omw-1.4')")
