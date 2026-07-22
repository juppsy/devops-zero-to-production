from fastapi import FastAPI
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def root():
    logger.info("Root endpoint called")

    return {"message": "Welcome to DevOps Zero to Production"}

@app.get("/health")
def health():
    logger.info("Health endpoint called")

    return {"status": "healthy"}

@app.get("/hello/Sebastian")
def hello_sebastian():
    logger.info("Greeting requested for Sebastian")

    return {"message": "Hello, Sebastian!"}
