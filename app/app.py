from litestar import Litestar, get
from app.routes import home
from typing import Any, Dict, TYPE_CHECKING
import logging
from litestar.datastructures import State

from app.exceptions import custom_exception_handler, validation_exception_handler
from litestar.exceptions import HTTPException, ValidationException

logger = logging.getLogger()


@get("/", sync_to_thread=False)
def handler(state: State) -> Dict[str, Any]:
    return state.dict()


# 透過在型別檢查時才導入，減少程式的啟動時間或資源使用
if TYPE_CHECKING:
    from litestar.types import Scope


async def after_exception_handler(exc: Exception, scope: "Scope") -> None:
    """Hook function that will be invoked after each exception."""
    state = scope["app"].state
    if not hasattr(state, "error_count"):
        state.error_count = 1
    else:
        state.error_count += 1

    logger.info(
        "an exception of type %s has occurred for requested path %s and the application error count is %d.",
        type(exc).__name__,
        scope["path"],
        state.error_count,
    )


# app = Litestar(route_handlers=[handler, home.routes])
app = Litestar(
    [handler, home.routes],
    exception_handlers={
        ValidationException: validation_exception_handler,
        HTTPException: custom_exception_handler,
    },
    after_exception=[after_exception_handler])
