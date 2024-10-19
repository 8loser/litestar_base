from typing import cast

from litestar.config.compression import CompressionConfig
from litestar.config.cors import CORSConfig
from litestar.openapi.config import OpenAPIConfig

from .envSetting import get_settings

settings = get_settings()

compression = CompressionConfig(backend="gzip")

cors = CORSConfig(
    allow_origins=cast("list[str]", settings.app.ALLOWED_CORS_ORIGINS))

openAPI = OpenAPIConfig(title=settings.app.NAME, version=settings.app.VERSION)
