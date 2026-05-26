from dotenv import load_dotenv
from loguru import logger
import os

load_dotenv()

try:
    APP_NAME = os.environ.get("APP_NAME", "DefaultApp")
    Password = os.environ.get("Password", "12345678")

    logger.info(f"Loaded config for {APP_NAME}")

except ValueError as e:
    logger.exception("Invalid environment variable")
    raise