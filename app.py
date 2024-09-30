"""from fastapi import FastAPI
import asyncio
import time


app = FastAPI()
@app.get("/creature/")
async def greeting(name: str):
    #await asyncio.sleep(2)
    return f"FastAPI, Hello from {name}?"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, reload=True)"""