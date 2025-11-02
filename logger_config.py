import logging
from logging.handlers import RotatingFileHandler


def setup_logger():
    logger = logging.getLogger("api-fetcher")
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler("fetcher.log", maxBytes=2000000, backupCount=3)
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    handler.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(handler)

    return logger