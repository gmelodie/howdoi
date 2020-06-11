from fastapi import FastAPI
from pydantic import BaseModel
from howdoi import howdoi


class Request(BaseModel):
    query_str: str
    other_content: str = None  # optional


class Response(BaseModel):
    answer_str: str
    plugin: str = None
    other_content: str = None  # optional


app = FastAPI(
    title="Howdoi Clients",
    description="Howdoi's API for clients",
    version="1",
)


def _get_answer(query_str):
    # TODO: maybe this wouldn't be needed in the future,
    #       it would be done by the client
    parser = howdoi.get_parser()
    args = vars(parser.parse_args(query_str.split(' ')))
    return howdoi.howdoi(args)


@app.post('/plugins', response_model=Response)
async def plugins(request: Request):
    answer = _get_answer(request.query_str)

    return {
        "answer_str": answer,
    }


@app.post('/plugins/{plugin}', response_model=Response)
async def plugin(plugin: str, request: Request):
    answer_str = _get_answer(request.query_str)

    return {
        "answer_str": answer_str,
        "plugin": plugin,
    }
