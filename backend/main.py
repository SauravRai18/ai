from fastapi import FastAPI
from backend.api.chat import router as chat_router

app = FastAPI(title="Open-Source AI Assistant")

app.include_router(chat_router)

@app.get("/")
def root():
    return {"status": "AI Assistant backend running"}
