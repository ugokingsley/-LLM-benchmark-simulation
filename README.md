
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
- Once inside the container, you can run Alembic migrations 
  ```bash
  alembic upgrade head
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

<img width="899" alt="image" src="https://github.com/user-attachments/assets/a379ab49-c22a-4e17-9a16-a80c7028867a">


### Rank Metric
- GET /api/rankings/{metric} -  API endpoint that returns the ranking of LLMs for a given metric.

#### Example request:
```bash
curl -X 'GET' \
  'http://localhost:8000/api/rankings/TPS' \
  -H 'accept: application/json' \
  -H 'api-key: mysecureapikey'
```

<img width="886" alt="image" src="https://github.com/user-attachments/assets/c6f0e50a-fe84-455b-ac0f-f35140362f78">

### Prometheus scrape:
- GET /metrics -  API endpoint This exposes a /metrics endpoint that Prometheus can scrape.

#### Example request:
```bash
curl -X 'GET' \
  'http://localhost:8000/metrics' \
  -H 'accept: application/json'
```

<img width="873" alt="image" src="https://github.com/user-attachments/assets/208c28be-60a9-45ff-bf82-ec39096355a0">

## Metric Visualization
The FastAPI application also contains a visualization of the LLM Metrics:
<img width="949" alt="image" src="https://github.com/user-attachments/assets/08c6c79b-508b-45bb-8528-ed4a6c3bfee0">

## Monitoring with Prometheus and Grafana
### Prometheus Setup
#### Install Prometheus using Helm:
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prometheus prometheus-community/prometheus
```

The Prometheus service will be exposed, and you can access it via:
```bash http://localhost:9090```

#### Grafana Setup
##### Install Grafana using Helm:

```bash helm repo add grafana https://grafana.github.io/ ```

##### helm-charts
```bash helm install grafana grafana/grafana```

##### Retrieve the Grafana admin password:

```bash kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo```

##### Access Grafana at:
```bash http://localhost:3000 ```

##### Configure Grafana to use Prometheus as a data source.


### Kubernetes Deployment
### Step 1: Install Helm
Make sure Helm is installed. You can install it by running:
```bash 
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash

```

### Step 2: Deploy the Application
#### Initialize a Kubernetes cluster if not already running (use minikube, Docker Desktop, or any cloud Kubernetes provider).

##### Install the application using Helm:
```bash
helm install k8-llmbenchmark ./k8-llmbenchmark
 ```

##### The application will be exposed through an ingress (or use a NodePort/LoadBalancer service based on your configuration).

### Step 3: Check Application Status
#### To check the status of the deployment:
```bash
kubectl get pods
kubectl get services
 ```

### Helm Charts
#### This project includes Helm charts to deploy the FastAPI app. You can find the Helm charts in the k8-llmbenchmark/ directory.

#### Installing the Charts
```bash
helm install k8-llmbenchmark ./k8-llmbenchmark

 ```

