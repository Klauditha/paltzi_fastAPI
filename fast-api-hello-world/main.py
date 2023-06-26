#Python
from typing import Optional
#Pydantic
from pydantic import BaseModel
#fastAPI
from fastapi import FastAPI
from fastapi import Body

app = FastAPI()

#Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


@app.get("/") #Path Operation Decorator
def home():                     #path Operation Function
    return {"Hello":"World"}

# Request and Response Body
@app.post("/person/new")
def create_person(person:Person = Body(...)): # ... indica que es obligatorio
    return Person
