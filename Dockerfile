# Usa uma imagem oficial do Python levinha
FROM python:3.11-slim

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Copia a lista de dependências e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o teu código Python pra dentro do container
COPY agente.py .

# Executa o teu script Python quando o container subir
CMD ["python", "agente.py"]