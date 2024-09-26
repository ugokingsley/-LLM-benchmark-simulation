"""
An in-memory SQLite database for testing, 
ensuring the database interactions are isolated.

"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Base
from app.database import get_db
from app.main import app  # Import your FastAPI app

# Create an in-memory SQLite database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Override the get_db dependency to use the test database session
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


# Apply the override to the FastAPI app
app.dependency_overrides[get_db] = override_get_db


# Fixture to create the test database
@pytest.fixture(scope="module")
def client():
    # Create the database and tables
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c
    # Drop the tables after the tests run
    Base.metadata.drop_all(bind=engine)
