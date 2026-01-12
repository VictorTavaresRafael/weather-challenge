# Script de Extração (OpenWeather)
import requests
import os
from .database import SessionLocal
from .models import WeatherData

# Parâmetros Dinâmicos
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "Sao Paulo"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=pt_br"

def run_etl():
    print(f"Iniciando extração para: {CITY}...")
    try:
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()

        # Tratamento simples dos dados
        weather_entry = WeatherData(
            city=data["name"],
            temperature=data["main"]["temp"],
            humidity=data["main"]["humidity"],
            description=data["weather"][0]["description"]
        )

        # Carga no Banco
        db = SessionLocal()
        db.add(weather_entry)
        db.commit()
        db.close()
        print("Dados armazenados com sucesso!")

    except Exception as e:
        print(f"Erro no ETL: {e}")

if __name__ == "__main__":
    run_etl()