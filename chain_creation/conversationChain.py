from langchain import HuggingFaceHub
import os
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
load_dotenv('.env')

def get_conv_chain(vector_store):
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    # print(OPENAI_API_KEY)
    llm_openai = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name="gpt-3.5-turbo", temperature=0)
    # template ="""
    # You are a PDF Helper Chat bot, given the CHAT_HISTORY and CONTEXT from user PDFs, answer the asked QUESTION.
    # Reply with I don't know if there is no information about the question in context.
    # Use the chat history to understand the question correctly.
    # CHAT_HISTORY: {chat_history}
    # CONTEXT: {context}
    # QUESTION: {question}
    # ANSWER: """

    # prompt = PromptTemplate.from_template(template=template)
    # input_variables = ["chat_history", "context", "question"],
    memory = ConversationBufferMemory(memory_key="chat_history",input_key="question", output_key="text", return_messages=True)
    chain_openai = ConversationalRetrievalChain.from_llm(
        llm_openai,
        chain_type="stuff",
        retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True,
        verbose=True,

    )
    return chain_openai
