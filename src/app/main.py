from typing import Union

from fastapi import FastAPI

from app.foobar.constants import PI

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "Hello": "World",
        "PI": PI,
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
