"""
DSA03 – Natural Language Processing
Program 15: Probabilistic context-free grammar (PCFG) parsing.

The grammar assigns probabilities to productions. NLTK's ViterbiParser
selects the highest-probability parse tree.
Install: pip install nltk
"""
from nltk import PCFG
from nltk.parse import ViterbiParser

GRAMMAR_TEXT = """
S  -> NP VP [1.0]
NP -> Det N [0.6] | 'John' [0.4]
VP -> V NP [0.7] | V [0.3]
Det -> 'the' [0.5] | 'a' [0.5]
N -> 'dog' [0.5] | 'cat' [0.5]
V -> 'sees' [0.6] | 'likes' [0.4]
"""

def main():
    grammar = PCFG.fromstring(GRAMMAR_TEXT)
    parser = ViterbiParser(grammar)
    sentence = input("Enter sentence (example: John sees the dog): ").split()

    trees = list(parser.parse(sentence))
    if not trees:
        print("No parse is possible under this PCFG.")
        return

    best_tree = trees[0]
    print("\nMost probable parse tree:")
    best_tree.pretty_print()
    print("Parse probability:", best_tree.prob())

if __name__ == "__main__":
    main()
