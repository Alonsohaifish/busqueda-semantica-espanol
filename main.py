from src.load_data import load_documents
from src.embeddings import load_model, create_embeddings
from src.index import build_index
from src.search import search


def main():
    print("Cargando documentos...")
    documents = load_documents("data/df_total.csv")

    print("Cargando modelo...")
    model = load_model()

    print("Generando embeddings...")
    embeddings = create_embeddings(model, documents)

    print("Construyendo índice...")
    index = build_index(embeddings)

    print("\nSistema listo. Escribe 'salir' para terminar.\n")

    while True:
        query = input("Buscar: ")

        if query.lower() == "salir":
            print("Cerrando programa...")
            break

        results = search(query, model, index, documents)

        print("\nResultados:\n")
        for i, r in enumerate(results, 1):
            print(f"{i}. {r['text']}")
            print(f"   Score: {r['score']}\n")


if __name__ == "__main__":
    main()