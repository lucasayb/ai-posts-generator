from dotenv import load_dotenv

import os

load_dotenv()

# I don't want to start the server 
# without an API Key, so I really 
# want an error to be returned
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")