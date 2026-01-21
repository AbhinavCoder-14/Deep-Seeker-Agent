from fastapi import FastAPI
from pydantic import BaseModel
from Agent.agentic_workflow import GraphBuilder

from fastapi.responses import JSONResponse
import os


app = FastAPI()

class QueryRequest(BaseModel):
    query:str
    
    
@app.post("/query")
async def query_travel_agent(query:QueryRequest):
    try:
        print(query)
        graph = GraphBuilder(model_provider="groq")
        react_app = graph()
        
        
    except Exception as e:
        print("problem occurs in app.py ")