from pydantic import BaseModel, ConfigDict
from datetime import datetime

# Classe base com os campos comuns
class WeatherBase(BaseModel):
    city: str
    temperature: float
    humidity: int
    description: str

# Classe de resposta (Response) que herda da base e adiciona ID e data
class WeatherResponse(WeatherBase):
    id: int
    collected_at: datetime

    model_config = ConfigDict(from_attributes=True) # Permite conversão de ORM para Pydantic