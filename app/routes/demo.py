from litestar import get, Router


@get("/")
async def demo_root() -> dict:
    return {"message": "Welcome to Litestar!"}


@get("/parm/{obj_id:int}")
async def get_obj(obj_id: int) -> dict[str, int]:
    return {"obj_id": obj_id}


routes = Router(path="/demo", route_handlers=[demo_root, get_obj])
