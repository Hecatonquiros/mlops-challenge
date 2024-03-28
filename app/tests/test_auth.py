import httpx
import pytest
from app.main import app  # Ajusta la importación según la estructura de tu proyecto

@pytest.mark.asyncio
async def test_get_access_token_authentication():
    # Crear un cliente de prueba para tu aplicación FastAPI
    ac = httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://0.0.0.0:8000")
    
    try:
        # Datos del formulario para enviar
        data = {
            "username": "admin",
            "password": "password"
        }
        
        # Realizar una solicitud POST al endpoint /token/
        response = await ac.post("/token", data=data)
        
        # Verificar la respuesta
        assert response.status_code == 200, response.text
        response_json = response.json()
        assert "access_token" in response_json, response.text
        assert response_json["token_type"] == "bearer", response.text
    finally:
        await ac.aclose()
