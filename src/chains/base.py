from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser

from src.schemas.article import Article
from src.config.settings import OPENAI_API_KEY

llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4o-mini")

parser = JsonOutputParser(pydantic_object=Article)

chain = llm | parser