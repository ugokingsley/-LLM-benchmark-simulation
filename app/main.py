from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.routes import benchmark

app = FastAPI(debug=True)

# Include the benchmark routes
app.include_router(benchmark.router, prefix="/api")

# Instrument the FastAPI app, This exposes a /metrics endpoint that Prometheus can scrape.
Instrumentator().instrument(app).expose(app)


@app.get("/")
def read_root():
    return {"message": "LLM Benchmarking API"}
