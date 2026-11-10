from llama_index.core.llms import ChatMessage
from llama_index.llms.google_genai import GoogleGenAI
from dotenv import load_dotenv


load_dotenv()
llm = GoogleGenAI(
    model="gemini-2.5-flash"
)
messages = [
    ChatMessage(
        role="system", content="You are a pirate with a colorful personality"
    ),
    ChatMessage(role="user", content="Tell me a story"),
]
llm = GoogleGenAI(model="gemini-2.5-flash")
resp = llm.chat(messages)

print(resp)
