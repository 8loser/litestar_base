from litestar import get, Router


@get("/")
async def home() -> dict:
    return {"message": "Welcome to Litestar!"}


@get("/books/{book_id:int}")
async def get_book(book_id: int) -> dict[str, int]:
    return {"book_id": book_id}


routes = Router(path="/home", route_handlers=[home, get_book])
