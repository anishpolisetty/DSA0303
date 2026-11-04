"""
DSA03 – Natural Language Processing
Program 20: TF-IDF information retrieval and document ranking.

TF-IDF gives higher weight to terms that are frequent in one document
but less common across the document collection.
Install: pip install scikit-learn
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DOCUMENTS = [
    "Natural language processing helps computers understand text.",
    "Machine learning algorithms learn patterns from data.",
    "Information retrieval finds relevant documents for a query.",
    "Python is a popular programming language for data science.",
    "Text classification is an important NLP application."
]

def search_documents(query, documents):
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(documents + [query])
    query_vector = matrix[-1]
    document_vectors = matrix[:-1]
    scores = cosine_similarity(query_vector, document_vectors).flatten()

    ranked = sorted(enumerate(scores), key=lambda item: item[1], reverse=True)
    return ranked

if __name__ == "__main__":
    print("Document collection:")
    for index, document in enumerate(DOCUMENTS, start=1):
        print(f"{index}. {document}")

    query = input("\nEnter search query: ").strip()
    if not query:
        print("Query cannot be empty.")
    else:
        print("\nRanked results:")
        for rank, (index, score) in enumerate(search_documents(query, DOCUMENTS), start=1):
            print(f"{rank}. Document {index + 1} | similarity={score:.4f}")
            print("   ", DOCUMENTS[index])
