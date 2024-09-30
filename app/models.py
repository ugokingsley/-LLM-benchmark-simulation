from sqlalchemy import Column, DateTime, Float, Integer, String, func

from app.database import Base


class LLM_Benchmark(Base):
    __tablename__ = "llm_benchmark"
    id = Column(Integer, primary_key=True, index=True)
    llm_name = Column(String, index=True)
    metric_name = Column(String, index=True)
    value = Column(Float)
    timestamp = Column(DateTime, default=func.now())
