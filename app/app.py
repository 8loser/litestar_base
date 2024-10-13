from litestar import Litestar, get
from typing import Any, Dict, TYPE_CHECKING
from litestar.datastructures import State

# 透過在型別檢查時才導入，減少程式的啟動時間或資源使用
if TYPE_CHECKING:
    from litestar.types import Scope


@get("/", sync_to_thread=False)
def handler(state: State) -> Dict[str, Any]:
    return state.dict()


async def after_exception_handler(exc: Exception, scope: "Scope") -> None:
    """Hook function that will be invoked after each exception."""
    state = scope["app"].state
    if not hasattr(state, "error_count"):
        state.error_count = 1
    else:
        state.error_count += 1

    # 出現 exception 紀錄 request IP, 參數
    client_ip, _ = scope.get("client", ("0.0.0.0", 0))
    scheme = scope.get("scheme", "http")
    server = scope.get("server", ("localhost", 80))
    host, port = server
    path = scope.get("path", "/")

    # 取得查詢參數 (若有)
    query_string = scope.get("query_string", b"").decode("latin-1")
    if query_string:
        url = f"{scheme}://{host}:{port}{path}?{query_string}"
    else:
        url = f"{scheme}://{host}:{port}{path}"

    from litestar.cli._utils import console
    console.print(f"[yellow]{client_ip} - {type(exc).__name__} - {url}[/]")


def create_app() -> Litestar:
    from app.routes import home
    from app.exceptions import http_exception_handler, validation_exception_handler
    from app.config import app as config
    from litestar.exceptions import HTTPException, ValidationException

    return Litestar(route_handlers=[handler, home.routes],
                    cors_config=config.cors,
                    compression_config=config.compression,
                    exception_handlers={
                        ValidationException: validation_exception_handler,
                        HTTPException: http_exception_handler,
                    },
                    after_exception=[after_exception_handler])


app = create_app()
