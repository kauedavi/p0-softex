import os 
from typing import Dict, List, Any
from dotenv import load_dotenv
from ollama import Client

load_dotenv()

LLM_ENDERECO: str = os.getenv("OLLAMA_LINK")
MODELO: str = os.getenv("MODELO")

client: Client = Client(host=LLM_ENDERECO)

print(f"rodando no endereco: {LLM_ENDERECO} \nModelo: {MODELO}")

def perguntas_user():
    entrada: str = input("Digite sua mensagem: ")
    return input


def chat_ollama():
    input: str = perguntasUser()
    print("Enviando dados para LLM...")
    ...