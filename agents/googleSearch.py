from langchain.agents import AgentType, Tool, initialize_agent
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_community.chat_models import ChatOpenAI
import os

def search_agent(question):
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    SERPER_API_KEY = os.environ["SERPER_API_KEY"]


    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name="gpt-3.5-turbo", temperature=0.1)
    search = GoogleSerperAPIWrapper()
    tools = [
        Tool(
            name="Intermediate Answer",
            func=search.run,
            description="useful for when you need to ask with search",
        )
    ]

    self_ask_with_search = initialize_agent(
        tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True, handle_parsing_errors=True
    )
    answer = self_ask_with_search.run(question)
    return answer