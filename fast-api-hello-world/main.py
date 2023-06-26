#Python
from typing import Optional
#Pydantic
from pydantic import BaseModel
#fastAPI
from fastapi import FastAPI
from fastapi import Body,Query,Path

app = FastAPI()

#Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

class Location(BaseModel):
    city: str
    state:str
    country:str

@app.get("/") #Path Operation Decorator
def home():                     #path Operation Function
    return {"Hello":"World"}

# Request and Response Body
@app.post("/person/new")
def create_person(person:Person = Body(...)): # ... indica que es obligatorio
    return person

#Validaciones query parameters
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title="Person name",
        description="this is the person name.It's between 1 and 50 characters"
        ),
    age: Optional[str] = Query(
        ...,
        title="Person age",
        description="This is the person age. It's required"
        )
):
    return {name:age}

#Validaciones path parameters
@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(...,gt=0)
):
    return {person_id:"It exists!"}

#Validaciones request body
@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person Id",
        description="This is the person ID",
        gt=0
        ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return results
