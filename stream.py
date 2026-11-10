from llama_index.llms.google_genai import GoogleGenAI
from dotenv import load_dotenv
load_dotenv()


llm = GoogleGenAI(model="gemini-2.5-flash")

resp = llm.stream_complete("Who is Paul Graham?")
for r in resp:
    print(r.delta, end="")