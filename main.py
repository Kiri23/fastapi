import uvicorn
from fastapi import FastAPI
from version import custom_openapi

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World 2"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


app.openapi = lambda: custom_openapi(app)

# To allow clicking the play button in vscode and uvicorn command is run
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
