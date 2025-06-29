from fastapi import FastAPI
from pydantic import BaseModel
from core.ollama_client import ask_ollama

app=FastAPI()

class PromptRequest(BaseModel):
    command:str

@app.post("/parse")
def parse_command(request:PromptRequest):
    json_command=ask_ollama(request.command)
    return{"parsed":json_command}

@app.get("/")
def home():
    return {"message": "Welcome to LlamaOrganizer API"}
