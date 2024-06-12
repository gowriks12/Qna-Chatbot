from input.parse_pdf import get_pdf_text
from text_processor.text_chunking import get_chunk_text
from text_processor.vector_embed import *
from chain_creation.conversationChain import get_conv_chain


def get_chain(input_files):
    # text = ""
    # if input_type == "PDF":
    text = get_pdf_text(input_files)
    chunks = get_chunk_text(text)
    retriever = get_retriever(chunks)
    chain = get_conv_chain(retriever)
    return chain


def run_llm(query,chat_history):
    chain= get_chain(["ML concept cheat sheet.pdf"])
    # docs = retriever.get_relevant_documents(query)
    response = chain({"question": query,"chat_history":chat_history})
    print(response)
    return response


if __name__ == "__main__":
    input_type = "PDF"
    pdf_files = ["static/Gowri-rao.pdf"]
    chat_history = []
    chain= get_chain(pdf_files)
    query = "Did Gowri do her Masters Degree?"
    # docs = retriever.get_relevant_documents(query)
    response = chain({"question": query,"chat_history":chat_history})
    # result = chain({"question": query})
    print("Question: ", query)
    print("Answer: ", response['answer'])
    chat_history.append((query,response["answer"]))
    query = "Where did she do it?"
    # docs = retriever.get_relevant_documents(query)
    response = chain({"question": query,"chat_history":chat_history})
    # result = chain({"question": query})
    print("Question: ", query)
    print("Answer: ", response['answer'])
    chat_history.append((query, response["answer"]))
