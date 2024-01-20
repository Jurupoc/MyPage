from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app import constants

app = FastAPI()
app.mount("/app/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory=constants.TEMPLATES_PATH)


@app.get("/")
def welcome(request: Request):
    return templates.TemplateResponse(request=request, name=constants.WELCOME_PAGE)
