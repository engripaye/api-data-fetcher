import logging
from logging.handlers import RotatingFileHandler


def setup_logger():
    logger = logging.getLogger("api-fetcher")
