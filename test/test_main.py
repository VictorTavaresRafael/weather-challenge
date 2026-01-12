from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from app.main import app
from app.database import get_db
from datetime import datetime

client = TestClient(app)

# Fixture: cria um banco de dados falso
def override_get_db():
    mock_db = MagicMock()
    # Simula o retorno de uma query no banco
    mock_item = MagicMock()
    mock_item.id = 1
    mock_item.city = "Test City"
    mock_item.temperature = 22.5
    mock_item.humidity = 50
    mock_item.description = "teste"
    mock_item.collected_at = datetime.now()
    
    # Quando chamarem db.query()...all(), retorna uma lista com o item falso
    mock_db.query.return_value.offset.return_value.limit.return_value.all.return_value = [mock_item]
    
    try:
        yield mock_db
    finally:
        pass

# Aplica a substituição da dependência
app.dependency_overrides[get_db] = override_get_db

def test_read_root():
    """Testa se a raiz responde 200 OK."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API Online. Acesse /docs para documentação."}

def test_read_weather_data():
    """Testa se o endpoint /weather retorna a lista de dados corretamente."""
    response = client.get("/weather")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["city"] == "Test City"
    assert "temperature" in data[0]