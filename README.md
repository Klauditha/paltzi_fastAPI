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