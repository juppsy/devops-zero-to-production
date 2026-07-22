from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to DevOps Zero to Production"}

@app.get("/health")
def health():
    return {"status": "healthy"}
