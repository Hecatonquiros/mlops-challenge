from fastapi import APIRouter, Depends, HTTPException, status

from pydantic import BaseModel, Field

class Token(BaseModel):
    """
        Token model
    """
    access_token: str
    token_type: str = Field(default="bearer")