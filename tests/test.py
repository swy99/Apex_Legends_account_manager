def remove_punctuation(string):
    res = ''
    for letter in string:
        if letter.isdigit() or letter.isalpha():
            print(letter)
            print(res)
            res = res + letter
    return res

print(remove_punctuation("hirdesgfr"))
print('ef'+'es')