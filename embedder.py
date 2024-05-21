import json

import chromadb
from chromadb.utils.embedding_functions import OllamaEmbeddingFunction


chroma_client = chromadb.HttpClient(host="100.73.70.105")

embedding_function = OllamaEmbeddingFunction(
    model_name="mxbai-embed-large",
    url="http://localhost:11434/api/embeddings",
)

collection = chroma_client.get_or_create_collection(
    name="aita", embedding_function=embedding_function
)

with open("aita.json", "r") as data:
    posts = json.loads(data.read())

for post in posts:
    contents = post["text"]

    del post["text"]

    print(f"Creating and inserting embedding for {post['title']}")

    try:
        collection.add(
            documents=[contents],
            metadatas=[post],
            ids=[post["id"]],
        )
    except Exception as e:
        print(e)

# search = collection.query(
#     query_texts=["sex"],
#     n_results=1,
# )
# print(search)
