import os 
from dotenv import load_dotenv
from ollama import Client

load_dotenv()

LLM_ENDERECO = os.getenv("OLLAMA_LINK")
MODELO = os.getenv("MODELO")

print(f"rodando no endereco: {LLM_ENDERECO} \nModelo: {MODELO}")

