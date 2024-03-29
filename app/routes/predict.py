import logging
import pickle
from fastapi import APIRouter, Depends, status, HTTPException, File, UploadFile, HTTPException
from jose import jwt

from app.config import settings
from app.dependencies import token_required

from fastapi import File, UploadFile, HTTPException
import numpy as np
from PIL import Image
import io

logger = logging.getLogger(__name__)
router = APIRouter(tags=["model"], dependencies=[Depends(token_required)])

with open("./app/svm_model_glasses.pkl", 'rb') as file:
    svm_model = pickle.load(file)

def data_prep(image_data):
    logger.info("Preparing the image.")
    image = Image.open(io.BytesIO(image_data))
    print(image)
    image = image.convert('L')  # Escala grises
    return np.asarray(image).flatten()  # Normaliza y aplana

@router.post("/predict/")
async def predict_glasses(file: UploadFile = File(...)):
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="El archivo no es una imagen")
    
    # Convertir la imagen cargada en un formato que el modelo pueda procesar
    image_data = await file.read()
    image_array =  data_prep(image_data)
    # Hacer la predicción
    prediction = svm_model.predict([image_array])
    logger.info("Giving the prediction.")
    result = "Gafas" if prediction[0] == 1 else "No Gafas"
    return {"filename": file.filename, "prediction": result}
