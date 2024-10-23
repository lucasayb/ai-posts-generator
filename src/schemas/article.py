from langchain_core.pydantic_v1 import BaseModel, Field

class Article(BaseModel):
    title: str = Field(description="Title of the article")
    content: str = Field(description="Markdown details of the article")