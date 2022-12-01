from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World - Server 1"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=9001)