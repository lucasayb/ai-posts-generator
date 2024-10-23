from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langserve import add_routes

import os

load_dotenv()

# I don't want to start the server 
# without an API Key, so I really 
# want an error to be returned
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

prompt = ChatPromptTemplate.from_template("""
You are an writer that receives a list of 
top trending GitHub Repositories from a RSS feed 
and creates a markdown article with that, being 
the top 10 trending repositories of the week.
You will receive the data as the context and 
in return you will give me the article built, 
in a natural way, but without too much gibberish.

<context>
{context}
</context>
""")

class Article(BaseModel):
    title: str = Field(description="Title of the article")
    content: str = Field(description="Markdown details of the article")

llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4o-mini")

parser = JsonOutputParser(pydantic_object=Article)

chain = prompt | llm | parser

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server to save articles in the Lucas Yamamoto's blog."
)

add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="localhost", port=8000)