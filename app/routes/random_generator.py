from sqlalchemy.orm import Session
from app.models import LLM_Benchmark
import time
from fastapi import HTTPException
import random


# Retry logic with exponential backoff
def retry_on_failure(func):
    def wrapper(*args, **kwargs):
        retries = 3
        delay = 1
        for i in range(retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(
                    f"Retry {i+1}/{retries} failed: {e}. Retrying in {delay} seconds..."
                )
                time.sleep(delay)
                delay *= 2
        raise HTTPException(status_code=500, detail="Failed after multiple retries.")

    return wrapper


# Random data generation with seeding
@retry_on_failure
def generate_random_data(db: Session, seed_value=42):
    llms = [
        "GPT-4o",
        "Llama 3.1 405",
        "Mistral Large2",
        "Claude 3.5 Sonnet",
        "Gemini 1.5 Pro",
        "GPT-4o mini",
        "Llama 3.1 70B",
        "amba 1.5Large",
        "Mixtral 8x22B",
        "Gemini 1.5Flash",
        "Claude 3 Haiku",
        "Llama 3.1 8B",
    ]
    metrics = ["TTFT", "TPS", "e2e_latency", "RPS"]

    random.seed(seed_value)  # Seed for reproducibility
    for llm in llms:
        for metric in metrics:
            for _ in range(1000):
                value = random.uniform(0.1, 100)
                benchmark = LLM_Benchmark(llm_name=llm, metric_name=metric, value=value)
                db.add(benchmark)
    db.commit()
