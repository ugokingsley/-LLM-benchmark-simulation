from sqlalchemy.orm import Session

from app.database import get_db
from app.models import LLM_Benchmark


# Testing to show that the /api/dashboard endpoint works
def test_dashboard(client):
    headers = {"api-key": "mysecureapikey"}
    response = client.get("/api/dashboard", headers=headers)
    assert response.status_code == 200
    assert (
        b"LLM Benchmark Dashboard" in response.content
    )  # Check if the dashboard page loads correctly


# Helper function to add testing data to the test database
def add_test_data(db: Session):
    test_entries = [
        LLM_Benchmark(llm_name="GPT-4o", metric_name="TTFT", value=0.5),
        LLM_Benchmark(llm_name="Llama 3.1 405", metric_name="TPS", value=1.2),
        LLM_Benchmark(llm_name="Mistral Large2", metric_name="e2e_latency", value=0.7),
    ]
    db.add_all(test_entries)
    db.commit()


# Test the dashboard visualization with real data
def test_dashboard_with_data(client):
    headers = {"api-key": "mysecureapikey"}
    db = next(get_db())
    add_test_data(db)

    response = client.get("/api/dashboard", headers=headers)
    assert response.status_code == 200
    assert b"LLM Benchmark Dashboard" in response.content

    # Ensure some visualization data is present
    assert b"plotly" in response.content


def test_rank_invalid_metric(client):
    headers = {"api-key": "mysecureapikey"}
    response = client.get("/api/rankings/INVALID_METRIC", headers=headers)
    assert response.status_code == 404  # Check for bad request on invalid metric name
