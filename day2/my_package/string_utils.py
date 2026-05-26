from loguru import logger

class StringError(Exception):
    pass


def reverse_text(text):

    try:
        if not isinstance(text, str):
            raise StringError("Input must be string")

        result = text[::-1]

        logger.info(f"Reversed text: {result}")

        return result

    except StringError:
        logger.exception("String processing failed")
        raise