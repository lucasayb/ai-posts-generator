from fastapi import FastAPI
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes

from src.schemas.article import Article
from src.prompts.github_trending import prompt as github_trending_prompt
from src.config.settings import OPENAI_API_KEY

llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4o-mini")

parser = JsonOutputParser(pydantic_object=Article)

chain = github_trending_prompt | llm | parser

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