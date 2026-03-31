from loguru import logger
from config.config import Config
import sys

def setup_logger(config: Config) -> None:
    logger.remove()

    if config.env == "prod":
        logger.add("logs/app_{date}.log", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", level="INFO", rotation="10 MB", retention="1 month", compression="gz")
    else:
        logger.add(sys.stderr, level="DEBUG", colorize=True)
