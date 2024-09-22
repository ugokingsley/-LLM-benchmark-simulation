# app/models.py

from sqlalchemy import Column, Integer, String, Float, DateTime, func
from app.database import Base


class LLM_Benchmark(Base):
    __tablename__ = "llm_benchmarks"
    id = Column(Integer, primary_key=True, index=True)
    llm_name = Column(String, index=True)
    metric_name = Column(String, index=True)
    value = Column(Float)
    timestamp = Column(DateTime, default=func.now())
