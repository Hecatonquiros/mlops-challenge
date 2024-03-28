import httpx
import pytest
from app.main import app  # Asume que tu FastAPI app está en main.py

@pytest.mark.asyncio
async def test_predict_glasses():
    # Crear un cliente de prueba para tu aplicación FastAPI
    ac = httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://0.0.0.0:8000")
    
    try:
        # Abrir una imagen de prueba desde el sistema de archivos
        files = {'file': ('sample_face.png', open('app/tests/test_files/sample_face.png', 'rb'), 'image/png')}
        
        # Realizar una solicitud POST al endpoint /predict/
        response = await ac.post("/predict/", files=files)
        
        # Verificar la respuesta
        print(response)
        assert response.status_code == 200
        assert "filename" in response.json()
        assert "prediction" in response.json()  # Asegúrate de que haya una predicción
        assert response.json() == {"filename": "sample_face.png", "prediction": "No Gafas"}
    finally:
        await ac.aclose()  # Cerrar el cliente de manera explícita al final de la prueba
