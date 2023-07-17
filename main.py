from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import Base, engine
from middleware.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router


app = FastAPI()
app.title = "Mi primera API con FastAPI"
app.version = "0.0.1"

# Middlewares
app.add_middleware(ErrorHandler)

# Routers
app.include_router(movie_router)
app.include_router(user_router)


Base.metadata.create_all(bind=engine)


@app.get("/", tags=["Home"])
def home():
    # responde un elemento HTML
    return HTMLResponse("<h1>Home</h1>")
