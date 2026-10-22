from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello":"World"}

@app.get("/health")
def health_check():
    return {"All okay":"200"}