from fastapi import FastAPI


app = FastAPI()
@app.get("/hi/{name}")
def greeting(name: str):
    return f"FastAPI, Hello from {name}"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, reload=True)