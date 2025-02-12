import sys
from loguru import logger
from my_service.config.config import settings


def setup_logger():
    logger.remove()
    logger.add(sys.stderr, level=settings.LOG_LEVEL)
    return logger
