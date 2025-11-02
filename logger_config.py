import logging
from logging.handlers import RotatingFileHandler


def setup_logger():
    logger = logging.getLogger("api_fetcher")
    logger.setLevel(logging.INFO)

    # File handler
    file_handler = RotatingFileHandler("fetcher.log", maxBytes=2000000, backupCount=3, encoding="utf-8")
    file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    return logger
