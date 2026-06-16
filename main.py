from fastapi import FastAPI
from agent.loop import run_agent

app = FastAPI()
@app.get("/")
def home():
    return {
        "message": "POC3 AI Agent Running"
    }
@app.post("/agent")
def ask_agent(query: str):

    result = run_agent(query)

    return {
        "answer": result
    }