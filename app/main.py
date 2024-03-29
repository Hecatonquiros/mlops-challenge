import os
import pickle
from fastapi import FastAPI

from app.logging import setup_log
from app import exceptions

from app.routes import auth
from app.routes import predict

app = FastAPI()

# APP LOG
setup_log()

# Exceptions handler
app.add_exception_handler(Exception, exceptions.generic_exception_handler)

# ROUTERs
app.include_router(auth.router)
app.include_router(predict.router)
