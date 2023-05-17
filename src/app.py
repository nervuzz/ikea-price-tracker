from http import HTTPStatus
from fastapi import FastAPI

from providers import IKEApi

app = FastAPI(title="IKEAPI")


@app.get("/", description="Just API root.",
         response_description="Greetings message.")
async def homepage() -> dict:
    return {"code": HTTPStatus.OK, "status": HTTPStatus.OK.phrase}


@app.get("/ikeapi", description="Fetch data from IKEA API.",
         response_description="JSON with data returned from IKEA API.")
async def fetch_ikeapi() -> dict:
    return IKEApi().fetch()
