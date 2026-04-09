import numpy as np

def search(query, model, index, documents, k=5):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k)

    results = []
    for i, d in zip(indices[0], distances[0]):
        results.append({
            "text": documents[i],
            "score": float(d)
        })

    return results