from loguru import logger

from my_package.math_utils import divide
from my_package.string_utils import reverse_text
from my_package.config import APP_NAME
from my_package.my_context import MyContextManager


logger.info(f"Starting {APP_NAME}")

try:

    print(divide(10, 2))

    print(reverse_text("Hetvi"))

    with MyContextManager() as context:

        context.show_message()

except Exception as e:

    logger.error(e)

finally:

    logger.info("Application finished")