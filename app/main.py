from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import victims, auth

app = FastAPI(
    title="Human Rights Monitor - Victim/Witness Database",
    description="Secure database for managing victim and witness information",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8080"],  # Add your frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(victims.router)

@app.get("/")
async def root():
    return {"message": "Human Rights Monitor - Victim/Witness Database API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}