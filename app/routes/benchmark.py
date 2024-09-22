from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from app.models import LLM_Benchmark
from sqlalchemy import func
from dotenv import load_dotenv
import os
from app.database import get_db
from .random_generator import generate_random_data, retry_on_failure

# Load environment variables
load_dotenv()

# Create the API router
router = APIRouter()

# Security: API key validation loaded from .env
API_KEY = os.getenv("API_KEY")


# Check to see if API key is passed in any request
def get_api_key(api_key: str = Header(...)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Unauthorized")


# API endpoint to trigger random data generation (for demonstration)
@router.get("/generate_data")
def generate_data(api_key: str = Depends(get_api_key), db: Session = Depends(get_db)):
    generate_random_data(db)
    return {"message": "Random benchmark data generated successfully."}
