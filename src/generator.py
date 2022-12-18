import random
from collections import Counter


class PasswordGenerator:

    # String of numbers
    numbers = '0123456789'

    # string of special characters
    special_char = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    # String of uppercase characters
    lower_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # String of lowercase characters
    upper_char = 'abcdefghijklmnopqrstuvwxyz'


    strength = 0
    def length_strength(self, len_pass):
        len_pass = 0
        len_strength = 0
        
        match [len_pass > 8, len_pass > 12]:
            case [True, True]:
                len_strength = 3
            case [True, False]:
                len_strength = 2
            case [False, False]:
                len_strength = 3
        return len_strength

    def char_strength(self, password):
        char_type_count = 0
        for char in self.upper_char:
            if char in password == True:
                char_type_count += 1
        for char in self.slower_char:
            if char in password == True:
                char_type_count += 1
        for char in self.numbers:
            if char in password == True:
                char_type_count += 1
        for char in self.special:
            if char in password == True:
                char_type_count += 1
        return char_type_count

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
    def check_password(self, string1, string2, word):
        for letter in string1:
            if letter not in word:
                return False
        for letter in string2:
            if letter not in word:
                return False
        return True
