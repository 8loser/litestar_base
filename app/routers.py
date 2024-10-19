"""Application Modules."""
from __future__ import annotations

from typing import TYPE_CHECKING

from app.domain.demo.controllers import DemoController

if TYPE_CHECKING:
    from litestar.types import ControllerRouterHandler

route_handlers: list[ControllerRouterHandler] = [DemoController]
