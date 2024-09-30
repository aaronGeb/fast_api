from model import Creature
from fastapi import FastAPI




app = FastAPI()
@app.get("/creature")
def get_all():
    from data import get_creature
    return get_creature()
@app.get("/")
def get_all():
  
    return {"message":"Welcome to the API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, reload=True)