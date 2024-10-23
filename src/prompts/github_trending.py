from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("""
You are an writer that receives a list of 
top trending GitHub Repositories from a RSS feed 
and creates a markdown article with that, being 
the top 10 trending repositories of the week.
You will receive the data as the context and 
in return you will give me the article built, 
in a natural way, but without too much gibberish.

You must return a JSON with a title and content
of the article.

<context>
{context}
</context>
""")