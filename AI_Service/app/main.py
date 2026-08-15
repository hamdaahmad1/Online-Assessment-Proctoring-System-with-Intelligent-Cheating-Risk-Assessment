from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Proctoring System - AI Service",
    description="Backend service providing AI capabilities (Face Verification, Object Detection, etc.) for the Online Proctoring System.",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Proctoring System AI Service API"}

# Include routers here as they are developed
# from app.api import face_verification
# app.include_router(face_verification.router)
