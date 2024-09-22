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


# API endpoint to fetch rankings for a specific metric
@retry_on_failure
@router.get("/rankings/{metric}")
def get_rankings(
    metric: str, api_key: str = Depends(get_api_key), db: Session = Depends(get_db)
):
    results = (
        db.query(
            LLM_Benchmark.llm_name, func.avg(LLM_Benchmark.value).label("mean_value")
        )
        .filter(LLM_Benchmark.metric_name == metric)
        .group_by(LLM_Benchmark.llm_name)
        .order_by("mean_value")
        .all()
    )

    if not results:
        raise HTTPException(
            status_code=404, detail="No data found for the specified metric."
        )

    result_dict = {row[0]: row[1] for row in results}

    return {"rankings": result_dict}
