# Leet speak is a term for the style of typing that replaces letters with numbers or symbols that resemble them, e.g. leet becomes 1337. Speak might become 5p3@k. There is a variety of different character substitutions (Wikipedia for leetLinks to an external site.), but here is the translation table we will use for this assignment:
#
# a -> @
# A -> 4
# B, b -> 8
# E, e -> 3
# I, i -> !
# L, l -> 1
# O, o -> 0
# S, s -> 5
#
#
# Create a function convert(text: str) -> str that accepts a string, converts the string to leet speak using the conversion table above, and returns the converted string. No other changes should be made to the string.


def leet_converter(s: str) -> str:
    new_s = ""
    for letter in s:
        match letter:
            case "a":
                new_s = new_s + "@"
            case "A":
                new_s = new_s + "4"
            case "B":
                new_s = new_s + "8"
            case "b":
                new_s = new_s + "8"
            case "E":
                new_s = new_s + "3"
            case "e":
                new_s = new_s + "3"
            case "I":
                new_s = new_s + "!"
            case "i":
                new_s = new_s + "!"
            case "L":
                new_s = new_s + "1"
            case "l":
                new_s = new_s + "1"
            case "O":
                new_s = new_s + "0"
            case "o":
                new_s = new_s + "0"
            case "S":
                new_s = new_s + "5"
            case "s":
                new_s = new_s + "5"
            case _:
                new_s = new_s + letter
    return new_s


print(leet_converter("Gabriel Sampson"))
