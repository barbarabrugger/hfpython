def search4vowels(phrase: str) -> set:
    """Display any vowels found in a supplied word."""
    vowels = set("aeiou")
    return search4letters(phrase, vowels)


def search4letters(phrase: str, letters: str) -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


print(search4letters("alle Menschen werden Brüder", "abcdefghijklmnopqrstuvwxyz"))
print(search4vowels("alle Menschen werden Brüder"))
