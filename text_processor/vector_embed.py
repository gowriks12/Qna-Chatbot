from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def get_retriever(text_chunks):
    # embeddings = HuggingFaceEmbeddings(
    #     model_name="sentence-transformers/all-MiniLM-L6-v2"
    # )
    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )

    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    # vectorstore.save_local("faiss_index_store")
    # retriever = vectorstore.as_retriever()

    return vectorstore
