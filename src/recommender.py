from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from src.prompt_template import get_anime_prompt
from langchain_groq import ChatGroq

class AnimeRecommender:
    def __init__(self, api_key:str, retriever, model_name:str):
        self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)
        self.prompt = get_anime_prompt()

        self.chain = (
            {
                "context":retriever,
                "question": RunnablePassthrough() #these both are input variables from the prompt template
            }
            | self.prompt
            | self.llm
            |StrOutputParser()
        )

    def get_recommendation(self, query:str):
        return self.chain.invoke(query)