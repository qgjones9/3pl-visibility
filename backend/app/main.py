from fastapi import FastAPI


def create_app() -> FastAPI:
    """Application factory for the 3PL visibility API."""
    app = FastAPI(
        title="3PL Supply Chain Visibility API",
        version="0.1.0",
        docs_url="/api/docs",
        openapi_url="/api/openapi.json",
    )

    @app.get("/")
    async def root() -> dict[str, str]:
        return {"service": app.title, "docs": "/api/docs"}

    return app


app = create_app()
