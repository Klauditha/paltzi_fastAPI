# Curso de FastAPI: Fundamentos, Path Operations y Validaciones

## Fast API
Framework de backend con Python y es muy veloz.

FastAPI utiliza otros frameworks dentro de si para funcionar:

- *Uvicorn*: es una librería de Python que funciona de servidor, es decir, permite que cualquier computadora se convierta en un servidor
- *Starlette* : es un framework de desarrollo web de bajo nivel, para desarrollar aplicaciones con este requieres un amplio conocimiento de Python, entonces FastAPI se encarga de añadirle funcionalidades por encima para que se pueda usar mas fácilmente
- *Pydantic*: Es un framework que permite trabajar con datos similar a pandas, pero este te permite usar modelos los cuales aprovechara FastAPI para crear la API.

## Creacion entorno virtual
py -m venv venv

## Activar entorno en windows
.\venv\Scripts\activate

## Activar entorno en linux
source venv/bin/activate
source venv/Scripts/activate

## Instalacion del framework
pip install fastapi uvicorn

## Correr aplicacion
uvicorn main:app --reload

## Documentacion interactiva
openAPI 
swagger 
redoc (alternativa swagger) -> http://127.0.0.1:8000/redoc
http://127.0.0.1:8000/docs (openAPI)
OAS -> Especificacion de las APIs

## Path Operations
www.myproject.com/API/
Path / Rutas / Endpoints -> lo que va a la derecha del dominio.
Operations -> Metodo HTTP :
- GET
- POST -> Envia informacion
- PUT
- DELETE

Otras
- OPTIONS
- HEAP
- PATCH
- TRACE

## Path Parameters
Variable definida dentro de un path
Para el caso de :
/tweets/22
/tweets/1

/tweets/{tweet_id}

Pasarlo es obligatorio

## Query Parameters
Permite no pasar parh parametros de forma obligatoria
PUT /users/{user_id}/details?age=20&height=184

## Request Body y Response Body
Request -> Cuando nos comunicamos con el servidor
Response -> Lo que entrega el servidor tras la peticion

## Models
Pydantic -> Base Model

## Validaciones: Query Parameters
https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
- max_length
- min_length
- regex
  
- >= Greater or equals than -> ge
- <= Less or equals then -> le
- > Greater than -> gt
- < Less than -> lt

- title
- description