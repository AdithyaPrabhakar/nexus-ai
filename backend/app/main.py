from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.incidents import router as incident_router
from app.routers.users import router as user_router
from app.routers.auth import router as auth_router
app = FastAPI(
    title="NexusAI API",
    description="Enterprise IT Incident Intelligence Platform",
    version="0.1.0",
)


# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register API routers
app.include_router(incident_router)
app.include_router(user_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to NexusAI API",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }