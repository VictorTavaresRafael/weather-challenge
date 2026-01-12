# API (Endpoints)
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .models import WeatherData
from typing import List
from . import schemas


app = FastAPI(title="Weather API Challenge", description="API para consulta de dados climáticos.")

@app.get("/")
def read_root():
    return {"message": "API Online. Acesse /docs para documentação."}

@app.get("/weather", response_model=List[schemas.WeatherResponse])
def read_weather_data(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """ 
    Retorna os dados climáticos armazenados no banco.
    """
    data = db.query(WeatherData).offset(skip).limit(limit).all()
    return data