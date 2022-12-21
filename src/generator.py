import random
import re

class PasswordGenerator:

    # String of numbers
    numbers = '0123456789'

    # string of special characters
    special_char = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    # String of uppercase characters
    lower_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # String of lowercase characters
    upper_char = 'abcdefghijklmnopqrstuvwxyz'
    

    def generate_password(self, length, chars):
        password = ""

        for _ in range(length):
            # Generate a random index between 0 and the length of chars
            index = random.randint(0, len(chars) - 1)

            # Retrieve a random character from chars using the generated index and
            # append it to password
            password += chars[index]

        return password
    
    # Not used as maximum recursion depth is always exceeded
    # Intended to check if password contains different character types
    def check_char(self, string1, string2, word):
        for letter in string1:
            if letter not in word:
                return False
        for letter in string2:
            if letter not in word:
                return False
        return True
    
    def check_password_strength(self, password):
        strength = 0
        if len(password) > 8:
            strength += 1
        if re.search("[a-z]", password):
            strength += 1
        if re.search("[A-Z]", password):
            strength += 1
        if re.search("[0-9]", password):
            strength += 1
        if re.search("[!@#$%^&*()_+-=[]{}|;':\",./<>?]", password):
            strength += 1
        return strength

gen = PasswordGenerator()

def make_random(length, *args):
    # final lenght of character type
    len_char_type = 0
    # Total number of character types
    total_args = len(args)
    # the average length to be selected for each character type
    char_len = length / total_args
    password = ''
    pw =''

    for arg in args:
        len_char_type = (
            (length / total_args) * 2 if char_len <= 5 else length / total_args
        )
        for _ in range(int(len_char_type)):
            index = random.randint(0, len(arg) - 1)
            pw += arg[index]
    print(pw)
    for _ in range(length):
        index = random.randint(0, len(pw) -1)
        password += pw[index]
    print(password)
    return password


make_random(10, 'sdxcvbnmfghj', '1234567890', 'SDFGBJFDWEFF', '!@#$%^&*()_+=-')  