import pandas as pd

def load_documents(path):
    df = pd.read_csv(path)
    return df["news"].tolist()