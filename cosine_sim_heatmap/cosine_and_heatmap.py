import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_data(file_path):
    sources = []
    content = []
    with open(file_path, 'r') as f:
        for line in f:
            data = json.loads(line)
            sources.append(data['source'])
            content.append(data['content'])

    return sources, content

def compute_cosine_similarity(content):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(content)
    similarity_matrix = cosine_similarity(X)
    return similarity_matrix

def create_heatmap(similarity, labels, cmap="YlGnBu"):
    df = pd.DataFrame(similarity, index=labels, columns=labels)
    plt.figure(figsize=(8, 6))
    sns.heatmap(df, cmap=cmap, annot=True, fmt=".2f")
    plt.title("Cosine Similarity Heatmap")
    plt.show()

def main():
    file_path = '/opt/homebrew/Cellar/hadoop/3.4.0/fancier_news_articles/cosine_sim_heatmap/outlet_dicts'
    labels, content = read_data(file_path)
    similarity_matrix = compute_cosine_similarity(content)

    create_heatmap(similarity_matrix, labels)

if __name__ == '__main__':
    main()