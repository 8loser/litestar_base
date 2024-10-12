from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR
from litestar import MediaType, Request, Response
from litestar.exceptions import ValidationException


def custom_exception_handler(_: Request, exc: Exception) -> Response:
    """Default handler for exceptions subclassed from HTTPException."""
    status_code = getattr(exc, "status_code", HTTP_500_INTERNAL_SERVER_ERROR)
    detail = getattr(exc, "detail", "")

    return Response(
        media_type=MediaType.JSON,
        content={"detail": detail},
        status_code=status_code,
    )


def validation_exception_handler(_: Request,
                                 exc: ValidationException) -> Response:
    '''參數錯誤'''
    return Response(
        media_type=MediaType.TEXT,
        content=f"validation error: {exc.detail}",
        status_code=400,
    )
