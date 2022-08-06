from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TestModel(Base):
    __tablename__ = "Test"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.utcnow)
    new_column = Column(Float, default=0.0)
    
    def __repr__(self):
        return f"TestModel(id: {self.id}, name: {self.name}, created: {self.created}, new_column: {self.new_column})"