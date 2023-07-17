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
    return HTMLResponse(
        """
                        <div>
                            <h1>API con FastAPI</h1>
                            <p>Para más información visita la documentación: <a href="/docs">en este link</a></p>
                        </div>
        """
    )


if __name__ == "__main__":
    import uvicorn
    import os

    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
