from fastapi import FastAPI
from pydantic import BaseModel
from langserve import add_routes

from src.chains.base import chain
from src.prompts.github_trending import prompt as github_trending_prompt

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

class Payload(BaseModel):
    context: str

@app.post("/github_trending")
def github_trending(payload: Payload):
    return (github_trending_prompt | chain).invoke({ "context": payload.context })