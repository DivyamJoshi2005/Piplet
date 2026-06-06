from fastapi import FastAPI

from src.core.config import settings

app=FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Production ML Platform - Train, Track, Deploy, Monitor",
)

@app.get("/")
async def root():
    """Root endpoint - basic health check."""
    return{
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }

@app.get("/health")
async def health_check():
    """Health check endpoint - useful for load balancers."""
    return {"status": "healthy"}