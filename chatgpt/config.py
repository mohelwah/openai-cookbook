import os
from typing import Dict

def read_api_keys(file_path: str) -> Dict[str, None]:
    """
    Reads a list of API keys from a text file.

    Args:
        file_path: A string representing the path to the text file containing the API keys.

    Returns:
        A list of strings representing the API keys read from the text file.

    Raises:
        FileNotFoundError: If the specified file cannot be found or accessed.
    """
    api_keys = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                name, key = line.strip().split(sep="=")
                api_keys[name] = key
    except FileNotFoundError:
        raise
    return api_keys
api_keys = read_api_keys('.api_key.txt')

###########################################
## OPENAI CONFIG
###########################################

COMPLETIONS_MODEL = "text-davinci-003"
EMBEDDINGS_MODEL = "text-embedding-ada-002"
CHAT_MODEL = 'gpt-3.5-turbo'
TEXT_EMBEDDING_CHUNK_SIZE = 300
OPENAI_KEY = api_keys['OPENAI_KEY']

###########################################
## PINCONE CONFIG
###########################################
PINECONE_KEY = api_keys['PINECONE_KEY']
INDEX_NAME = 'gpt-4-langchain-docs-test'
PINECONE_ENV = "northamerica-northeast1-gcp"
INDEX_DIM = 1536
DISTANCE_METRIC = 'dotproduct'
###########################################
# SYSTEM CONFIG
###########################################
VECTOR_FIELD_NAME = 'content_vector'
PREFIX = "sportsdoc"



if __name__ == "__main__":
    print(OPENAI_KEY, type(PINECONE_KEY), PINECONE_KEY)