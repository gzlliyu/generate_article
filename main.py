from typing import Dict

from fastapi import FastAPI

from generate_article import generate_article_by_language

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/generate_article")
async def generate_article(item: Dict):
    return generate_article_by_language(item.get("query"))


if __name__ == "__main__":
    import uvicorn
    port = 8000
    uvicorn.run(app, port=port)