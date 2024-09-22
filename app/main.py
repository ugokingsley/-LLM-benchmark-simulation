# app/main.py

from fastapi import FastAPI
from app.routes import benchmark

app = FastAPI(debug=True)

# Include the benchmark routes
app.include_router(benchmark.router, prefix="/api")


@app.get("/")
def read_root():
    return {"message": "LLM Benchmarking API"}
