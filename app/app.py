from litestar import Litestar
from app.routes import home

app = Litestar(route_handlers=[home.routes], )
