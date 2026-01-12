import pytest
import requests
from unittest.mock import MagicMock, patch
from app.etl import fetch_weather_data, load_data_to_db

MOCK_API_RESPONSE = {
    "name": "Test City",
    "main": {"temp": 25.0, "humidity": 60},
    "weather": [{"description": "ceu limpo"}]
}

def test_fetch_weather_data_success():
    """Testa se a função retorna o JSON correto quando a API responde 200."""
    with patch("app.etl.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_API_RESPONSE
        
        data = fetch_weather_data()
        
        assert data == MOCK_API_RESPONSE
        assert data["name"] == "Test City"

def test_fetch_weather_data_retry_logic():
    """Testa se o sistema tenta 3 vezes antes de falhar (Retry Logic)."""
    with patch("app.etl.requests.get") as mock_get:
        # CORREÇÃO AQUI: Simulamos um erro de REDE específico, não um erro genérico
        mock_get.side_effect = requests.exceptions.RequestException("Connection Error")
        
        with pytest.raises(Exception) as excinfo:
            fetch_weather_data(retries=3, delay=0)
        
        # Agora o código vai capturar o erro, tentar 3x e lançar a exceção final
        assert "Max retries exceeded" in str(excinfo.value)
        assert mock_get.call_count == 3

def test_load_data_to_db():
    """Testa se os dados são enviados corretamente para o banco (Mockado)."""
    with patch("app.etl.SessionLocal") as mock_session_cls:
        mock_db = MagicMock()
        mock_session_cls.return_value = mock_db
        
        load_data_to_db(MOCK_API_RESPONSE)
        
        mock_db.add.assert_called_once()
        mock_db.commit.assert_called_once()
        mock_db.close.assert_called_once()