import requests
import os
import logging
import time
from .database import SessionLocal
from .models import WeatherData

# Configuração de Logging 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("ETL_Process")

# Parâmetros
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "Sao Paulo"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=pt_br"

def fetch_weather_data(retries=3, delay=2):
    """
    Realiza a extração dos dados da API com mecanismo de retry.
    """
    logger.info(f"Iniciando extração de dados para: {CITY}")
    
    for attempt in range(retries):
        try:
            response = requests.get(URL, timeout=10)
            response.raise_for_status()
            logger.info("Dados extraídos com sucesso.")
            return response.json()
        except requests.RequestException as e:
            logger.warning(f"Tentativa {attempt + 1}/{retries} falhou: {e}")
            time.sleep(delay)
    
    logger.error("Falha crítica: Não foi possível conectar à API após várias tentativas.")
    raise Exception("Max retries exceeded")

def load_data_to_db(data):
    """
    Transforma e carrega os dados no banco de dados.
    """
    db = SessionLocal()
    try:
        # Tratamento / Transformação
        weather_entry = WeatherData(
            city=data["name"],
            temperature=data["main"]["temp"],
            humidity=data["main"]["humidity"],
            description=data["weather"][0]["description"]
        )

        # Carga
        db.add(weather_entry)
        db.commit()
        logger.info(f"Dados climáticos de {data['name']} persistidos no banco de dados (ID: {weather_entry.city}).")
        
    except Exception as e:
        db.rollback() # Importante: Desfaz mudanças em caso de erro
        logger.error(f"Erro ao salvar no banco de dados: {e}")
        raise
    finally:
        db.close() # Garante o fechamento da conexão

def run_etl():
    """
    Função principal que orquestra o pipeline.
    """
    try:
        raw_data = fetch_weather_data()
        load_data_to_db(raw_data)
        logger.info("Pipeline ETL finalizado com sucesso.")
    except Exception as e:
        logger.error(f"O Pipeline ETL falhou. Detalhes: {e}")

if __name__ == "__main__":
    run_etl()