from sentence_transformers import SentenceTransformer

def load_model():
    return SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

def create_embeddings(model, documents):
    return model.encode(documents, batch_size=64, show_progress_bar=True)