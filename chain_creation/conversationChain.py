from langchain import HuggingFaceHub
import os
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain


def get_conv_chain(vector_store):
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    # print(openai_api_key)
    llm_openai = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name="gpt-3.5-turbo", temperature=0)

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    chain_openai = ConversationalRetrievalChain.from_llm(
        llm_openai,
        chain_type="stuff",
        retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True,
        verbose=True,
    )
    return chain_openai
