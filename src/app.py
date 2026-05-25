from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/test")
def test():
    return {"test": "ok"}

@app.get("/")
def root():
    return {"ok": True}
