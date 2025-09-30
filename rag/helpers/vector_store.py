import openai
from chromadb import PersistentClient
from chromadb.config import Settings
from chromadb.api.models import Collection
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY


def embed_texts(texts: list[str]) -> list[list[float]]:
    """
    Embed a list of texts using OpenAI's embedding model.
    
    Args:
        texts (list of str): List of texts to embed.

    Returns:
        list of list of float: List of embeddings corresponding to the input texts.
    """
    response = openai.Embedding.create(
        model="text-embedding-3-small", 
        input=texts
    )
    return [r['embedding'] for r in response['data']]


def get_chroma_collection(collection_name: str = "pdf_chunks", persist_dir: str = "chroma_db") -> Collection:
    """
    Initialize Chroma PersistentClient and get or create a collection.

    Args:
        collection_name (str): Name of the collection to use.
        persist_dir (str): Directory to persist the Chroma database.

    Returns:
        chromadb.api.models.Collection.Collection: 
        A Chroma collection object used to store and query embeddings.
    """
    client = PersistentClient(path=persist_dir, settings=Settings())
    collection = client.get_or_create_collection(collection_name)
    return collection