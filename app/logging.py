import logging
from logging.handlers import RotatingFileHandler

from app.config import settings

def setup_log():
    """
        Sets up the application logging
    """
    logging_format = "%(asctime)s - %(levelname)s - %(module)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=logging_format)
    handler = RotatingFileHandler(settings.LOG_PATH_FILE, maxBytes=10000000, backupCount=3)
    handler.setFormatter(logging.Formatter(logging_format))

    logger = logging.getLogger()
    logger.addHandler(handler)