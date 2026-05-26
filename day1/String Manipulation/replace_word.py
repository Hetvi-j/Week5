def replace_word(text: str, old: str, new: str) -> str:
    """Replace every occurrence of one word or substring with another."""
    return text.replace(old, new)


if __name__ == "__main__":
    sample_text = "I like cats and cats are cute"
    result = replace_word(sample_text, "cats", "dogs")
    print(result)
