def search4vowels(phrase: str) -> set:
    """Display any vowels found in a supplied word."""
    vowels = set("aeiou")
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str) -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


help(search4letters)
