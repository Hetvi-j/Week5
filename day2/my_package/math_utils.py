from loguru import logger


class MathError(Exception):
    pass


def divide(a, b):

    try:
        if b == 0:
            raise MathError("Division by zero is not allowed")

        result = a / b

        logger.info(f"Division result: {result}")

        return result

    except MathError:
        logger.exception("Math error occurred")
        raise

    except TypeError:
        logger.exception("Invalid data type")
        raise