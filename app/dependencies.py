import time
from fastapi import HTTPException, Depends, status
from jose import jwt
from app.config import settings
from app.routes.auth import oauth2_scheme

async def token_required(authorization_token: str = Depends(oauth2_scheme)):
    if authorization_token is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization header missing.")
    try:
        if authorization_token.startswith("Bearer "):
            _, authorization_token = authorization_token.split(" ", 1)
        payload = jwt.decode(authorization_token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        expiration_date = payload["exp"]
        if expiration_date < int(time.time()):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Failed authentication: the token is expired.")
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")