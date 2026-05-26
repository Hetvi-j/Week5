def count_vowels(text: str) -> int:
    """Count the number of vowels in the input text."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
