from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

prompt = ChatPromptTemplate.from_template("""
You are an write that receives a list of 
top trending GitHub Repositories and creates
a markdown article with that. You will receive
the data and in return will give as output
a title with a content.                                       
""")

class Article(BaseModel):
    title: str = Field(description="Title of the article")
    content: str = Field(description="Markdown details of the article")

llm = ChatOpenAI(api_key=OPENAI_API_KEY)

parser = JsonOutputParser(pydantic_object=Article)

chain = prompt | llm | parser