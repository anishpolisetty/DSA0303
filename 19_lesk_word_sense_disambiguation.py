"""
DSA03 – Natural Language Processing
Program 19: Word Sense Disambiguation using the simplified Lesk algorithm.

The algorithm chooses the dictionary sense whose definition/examples
share the largest number of words with the surrounding context.
Install: pip install nltk
Download: nltk.download('wordnet')
"""
import re
import nltk
from nltk.corpus import wordnet as wn

STOP_WORDS = {
    "the", "a", "an", "is", "are", "was", "were", "of", "in",
    "on", "at", "to", "and", "with", "for", "this", "that"
}

def normalize(text):
    return {
        word for word in re.findall(r"[a-z]+", text.lower())
        if word not in STOP_WORDS
    }

def lesk(context, ambiguous_word):
    context_words = normalize(context)
    best_sense = None
    best_score = -1

    for sense in wn.synsets(ambiguous_word):
        signature = normalize(sense.definition())
        for example in sense.examples():
            signature |= normalize(example)
        score = len(context_words & signature)

        if score > best_score:
            best_score = score
            best_sense = sense

    return best_sense, best_score

if __name__ == "__main__":
    context = "He deposited money in the bank near the river."
    word = "bank"
    try:
        sense, score = lesk(context, word)
        print("Context:", context)
        print("Ambiguous word:", word)
        if sense:
            print("Selected sense:", sense.name())
            print("Meaning:", sense.definition())
            print("Overlap score:", score)
        else:
            print("No WordNet senses found.")
    except LookupError:
        print("Download WordNet using nltk.download('wordnet').")
