from dotenv import load_dotenv
from llama_index.llms.google_genai import GoogleGenAI

load_dotenv()
llm = GoogleGenAI(
    model="gemini-2.5-flash"
)

# Send a prompt
response = llm.complete(
    "Explain Retrieval Augmented Generation in simple terms."
)

print(response)