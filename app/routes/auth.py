from datetime import timezone, datetime, timedelta
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt

import logging
from app.config import settings
from app.models import Token

router = APIRouter(tags=["auth"])

logger = logging.getLogger(__name__)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_credentials(username: str, password: str):
    """
        Verify the credentials of a user app

        Parameters:
        - username (str): username credential
        - password (str): password credential

        Return:
            True in case the user + password is valid. False in other case.
    """
    if username == "admin" and password == "password": # This check should be against an LDAP or an Active directory or a Local database.
        logger.info(f"Correct login for {username}")
        return True
    return False

def create_access_token(data: dict, exp_min: int) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=exp_min)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    logger.info(f"Creating token.")
    return encode_jwt

@router.post("/token")
async def get_access_token_authentication(
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Token:
    """
        Get the jwt token to authenticate in the other routers of the application

        Parameters: 
        - form_data (OAuth2PasswordRequestForm): A form data containing the username and password.

        Return: 
            A json response containing the access_token and the token_type.
    """
    username = form_data.username
    user = verify_credentials(username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    access_token = create_access_token(data={"username": user}, exp_min=settings.ACCESS_TOKEN_TIME)
    logger.info(f"Token generated for {username}")
    return Token(access_token=access_token)