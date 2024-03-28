import traceback
from fastapi import Request, Response, status
import logging

logger = logging.getLogger(__name__)

async def generic_exception_handler(request: Request, exc: Exception):
    """
        Generic excpetion handler that catches most unhandled exceptions.

        Parameters:
        - exc (Exception): Exceptionn that has been raised.

        Return:
        - response (dict): a json response that includes the error
    """
    print("sdjslkj")
    logger.error(traceback.format_exc())
    return Response(content=str(exc), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    