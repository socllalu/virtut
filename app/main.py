from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import AzureOpenAI
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración del cliente
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2023-05-15",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Inicialización de FastAPI
app = FastAPI()

# Modelo de datos para la petición
class QuestionRequest(BaseModel):
    question: str

# Endpoint principal
@app.post("/ask")
async def ask_question(request: QuestionRequest):
    try:
        # Enviar la pregunta al modelo de Azure OpenAI
        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),  # Cambiado de 'engine' a 'model'
            messages=[{"role": "user", "content": request.question}],
            max_tokens=500
        )

        # Extraer la respuesta del modelo
        answer = response.choices[0].message.content
        return {"answer": answer.strip()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

# Ruta de prueba
@app.get("/")
def read_root():
    return {"message": "¡El backend está funcionando correctamente!"}
