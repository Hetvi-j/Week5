from loguru import logger


class MyContextManager:

    def __enter__(self):

        logger.info("Entering Context Manager")

        print("Setup Started")

        return self

    def show_message(self):

        print("Inside Context Manager")

    def __exit__(self, exc_type, exc_value, traceback):

        logger.info("Exiting Context Manager")

        print("Cleanup Done")

        if exc_type:
            logger.error(f"Error: {exc_value}")

        return False