import random
import re


# String of numbers
numbers = '0123456789'
# string of special characters
special_char = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# String of uppercase characters
lower_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# String of lowercase characters
upper_char = 'abcdefghijklmnopqrstuvwxyz'

        
def generate_password_basic(length, chars):
    password = ""
    length = int(length)
    for _ in range(length):
        # Generate a random index between 0 and the length of chars
        index = random.randint(0, len(chars) - 1)
        # Retrieve a random character from chars using the generated index and
        # append it to password
        password += chars[index]
    return password

# Not used as maximum recursion depth is always exceeded
# Intended to check if password contains different character types
# def check_char(string1, string2, word):
#     for letter in string1:
#         if letter not in word:
#             return False
#     for letter in string2:
#         if letter not in word:
#             return False
#     return True

def check_password_strength(password):
    strength = 0
    if len(password) > 8:
        strength += 2
    if re.search("[a-z]", password):
        strength += 2
    if re.search("[A-Z]", password):
        strength += 2
    if re.search("[0-9]", password):
        strength += 2
    if re.search("[!@#$%^&*()_+-=[]{}|;':\",./<>?]", password):
        strength += 2
    return strength

def generate_password(length, *args):
    # final lenght of character type
    len_char_type = 0
    # Total number of character types
    total_args = len(args)
    # the average length to be selected for each character type
    char_len = length / total_args
    password = ''
    pw ='' # a variable name to hold string to be used to generate password
    # generate random string based on given character types
    for arg in args:
        # len_char_type is new length of each given arguement (character type)
        # based on number of character type and length of password
        len_char_type = (
            (length / total_args) * 2 if char_len <= 5 else length / total_args
        )
        # random strings of length = len_char_type are generated from given
        # character types
        pw = generate_password_basic(len_char_type, arg)
        # generated character stings are saved in variable password
        password += pw
    # Use generated string in variable password to generate password of given length
    password = generate_password_basic(length, password)
    return password