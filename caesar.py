def encrypt(text,rot):
    i = 0
    newtext = ""
    while i < len(text):
        newtext = newtext + rotate_character(text[i],rot)
        i = i + 1
    return newtext

def alphabet_position(letter):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    while i < len(alpha):
        if letter.lower() == alpha[i]:
            return i
            i = i + 1
        else:
            i = i + 1

def rotate_character(char,rot):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    if char.lower() in alpha:
        if char.isupper():
            char = alphabet_position(char)
            char = (char + rot) % 26
            char = alpha[char].upper()
        else:
            char = alphabet_position(char)
            char = (char + rot) % 26
            char = alpha[char]
        return char
    else:
        return char
