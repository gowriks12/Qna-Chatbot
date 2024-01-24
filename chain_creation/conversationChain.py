from langchain import HuggingFaceHub

from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

def get_conv_chain(vector_store):

    llm_openai = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages= True)
    chain_openai = ConversationalRetrievalChain.from_llm(llm_openai,
                                                         chain_type="stuff",
                                                         retriever= vector_store.as_retriever(search_kwargs={"k": 3}),
                                                         return_source_documents=True,
                                                         verbose=False,
                                                         memory=memory
                                                         )
    return chain_openai

