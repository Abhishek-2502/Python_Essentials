from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from FastAPI on Vercel!"}


@app.get("/health")
async def health():
    return {"status": "ok"}
