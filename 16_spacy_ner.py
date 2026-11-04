"""
DSA03 – Natural Language Processing
Program 16: Named Entity Recognition (NER) using spaCy.

Install:
  pip install spacy
  python -m spacy download en_core_web_sm
"""
import spacy

def recognize_entities(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    if not doc.ents:
        print("No named entities detected.")
        return

    print(f"{'ENTITY':<25}{'LABEL':<15}DESCRIPTION")
    print("-" * 65)
    for entity in doc.ents:
        print(f"{entity.text:<25}{entity.label_:<15}{spacy.explain(entity.label_)}")

if __name__ == "__main__":
    sample = "Sundar Pichai works at Google, which is based in California."
    try:
        recognize_entities(sample)
    except OSError:
        print("spaCy English model is missing.")
        print("Run: python -m spacy download en_core_web_sm")
