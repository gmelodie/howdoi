from fastapi import FastAPI
from pydantic import BaseModel


class Query(BaseModel):
    content: str
    other_content: str = None # optional


client_app = FastAPI(
    title="Howdoi Clients",
    description="Howdoi's API for clients",
    version="1",
)


@client_app.post('/plugins')
async def plugins(query: Query):
    return {
        "Hello": "World",
        "content": query.content,
    }


@client_app.post('/plugins/{plugin}')
async def plugin(plugin: str, query: Query):
    return {
        "plugin": plugin,
        "content": query.content,
    }
