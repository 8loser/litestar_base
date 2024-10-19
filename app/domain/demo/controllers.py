from __future__ import annotations

from litestar import Controller, get


class DemoController(Controller):
    tags = ['Demo']

    @get(path=["/demo"], )
    async def index(self) -> dict:
        return {"message": "Welcome to Litestar!"}

    @get("/demo/parm/{obj_id:int}")
    async def get_obj(self, obj_id: int) -> dict[str, int]:
        return {"obj_id": obj_id}
