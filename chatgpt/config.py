import os



###########################################
## OPENAI CONFIG
###########################################

COMPLETIONS_MODEL = "text-davinci-003"
EMBEDDINGS_MODEL = "text-embedding-ada-002"
CHAT_MODEL = 'gpt-3.5-turbo'
TEXT_EMBEDDING_CHUNK_SIZE = 300
OPENAI_KEY = os.environ.get('OPENAI_KEY')

###########################################
## PINCONE CONFIG
###########################################
PINECONE_KEY = os.environ.get('PINECONE_KEY')
INDEX_NAME = 'gpt-4-langchain-docs-test01'
PINECONE_ENV = "northamerica-northeast1-gcp"
INDEX_DIM = 1536
###########################################
# SYSTEM CONFIG
###########################################
VECTOR_FIELD_NAME = 'content_vector'
PREFIX = "sportsdoc"
