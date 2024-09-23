
# FastAPI LLM Benchmarking Tool

This project is a FastAPI application that benchmarks various Language Learning Models (LLMs) based on performance metrics such as Time to First Token (TTFT), Tokens Per Second (TPS), End-to-End Latency (e2e_latency), and Requests Per Second (RPS). The application is deployed using Kubernetes with Helm charts and includes monitoring through Prometheus and Grafana.

## Features
- Simulates and benchmarks LLMs like GPT-4o, Llama 3.1, Mistral Large2, Claude 3.5, and more.
- Exposes API endpoints to fetch benchmark results and LLM rankings.
- Robust and scalable deployment with Kubernetes using Helm charts.
- Integrated monitoring with Prometheus and Grafana for metrics tracking and alerts.


# Installation
## Prerequisites
- Docker
- Kubernetes (minikube, Docker Desktop, or cloud provider)
- Helm
- Prometheus and Grafana (optional for monitoring)
- Python 3.8+
- PostgreSQL (used for storing benchmark data)

## Clone the repository
```bash
https://github.com/ugokingsley/-LLM-benchmark-simulation.git
cd -LLM-benchmark-simulation
cp .env.example .env
```

## Running the Application
### Using Docker Compose
- Set up a PostgreSQL DB with PGAdmin with the DB credentials as stated in the .env file
- Ensure you have Docker installed.
- Run the application:

```bash
docker-compose up --build
```

## API Endpoints
The FastAPI application exposes the following endpoints:

### Generate data points
- GET /api/generate_data -  API endpoint to generate 1,000 data points for each LLM against each given metric.
(for demonstration)

#### Example request:
```bash
curl -X 'GET' \
  'http://localhost:8000/api/generate_data' \
  -H 'accept: application/json' \
  -H 'api-key: mysecureapikey'
```

### Rank Metric
- GET /api/rankings/{metric} -  API endpoint that returns the ranking of LLMs for a given metric.

#### Example request:
```bash
curl -X 'GET' \
  'http://localhost:8000/api/rankings/TPS' \
  -H 'accept: application/json' \
  -H 'api-key: mysecureapikey'
```

### Prometheus scrape:
- GET /metrics -  API endpoint This exposes a /metrics endpoint that Prometheus can scrape.

#### Example request:
```bash
curl -X 'GET' \
  'http://localhost:8000/metrics' \
  -H 'accept: application/json'
```

