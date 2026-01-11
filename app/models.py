# Modelagem do Banco
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .database import Base, engine

class WeatherData(Base):
    __tablename__ = "weather_logs"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    temperature = Column(Float)
    humidity = Column(Integer)
    description = Column(String)
    collected_at = Column(DateTime, default=datetime.utcnow)

# Cria as tabelas automaticamente
Base.metadata.create_all(bind=engine)