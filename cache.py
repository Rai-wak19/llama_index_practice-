from google import genai
from google.genai.types import CreateCachedContentConfig, Content, Part
import time

client = genai.Client()

# For VertexAI
# client = genai.Client(
#     http_options=HttpOptions(api_version="v1"),
#     project="your-project-id",
#     location="us-central1",
#     vertexai="True"
# )

# Upload and process local PDF files
pdf_file = client.files.upload(file="./")
while pdf_file.state.name == "PROCESSING":
    print("Waiting for PDF to be processed.")
    time.sleep(2)
    pdf_file = client.files.get(name=pdf_file.name)

# Create cache with uploaded file
cache = client.caches.create(
    model="gemini-2.5-flash",
    config=CreateCachedContentConfig(
        display_name="Document Analysis Cache",
        system_instruction=(
            "You are an expert document analyzer. Answer questions "
            "based on the provided documents with accuracy and detail."
        ),
        contents=[pdf_file],  # Direct file reference
        ttl="3600s",  # Cache for 1 hour
    ),
)