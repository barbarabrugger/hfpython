def search4vowels(phrase: str) -> set:
    """Display any vowels found in a supplied word."""
    vowels = set("aeiou")
<<<<<<< HEAD
    return search4letters(phrase, vowels)
=======
    return vowels.intersection(set(phrase))
>>>>>>> 666df255994ae1a06fb87de14616cb9019a49317


def search4letters(phrase: str, letters: str) -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


<<<<<<< HEAD
print(search4letters("alle Menschen werden Brüder", "abcdefghijklmnopqrstuvwxyz"))
print(search4vowels("alle Menschen werden Brüder"))
=======
help(search4letters)
>>>>>>> 666df255994ae1a06fb87de14616cb9019a49317
