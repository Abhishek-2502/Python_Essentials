from fastapi import FastAPI
import uvicorn

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

def main():
    print("Hello from project-name!")
    # Start the FastAPI server
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
