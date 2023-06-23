from fastapi import FastAPI

app = FastAPI()

@app.get("/") #Path Operation Decorator
def home():                     #path Operation Function
    return {"Hello":"World"}