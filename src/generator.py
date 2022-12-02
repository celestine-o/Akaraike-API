import random

numbers = [0,1,2,3,4,5,6,7,8,9]

special = ['!','@','#','$','%','&','*','(',')','_','-','+','=','|','?','/']

lower_char = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

upper_char = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]


class Password:
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
        for char in upper_char:
            if char in password == True:
                char_type_count += 1
        for char in lower_char:
            if char in password == True:
                char_type_count += 1
        for char in numbers:
            if char in password == True:
                char_type_count += 1
        for char in special:
            if char in password == True:
                char_type_count += 1
        return 

    def gen(self, len_pass):
        if len_pass == 1:
            password= password.extend(random.choice(upper_char))
        Password.gen(self, len_pass - 1)
        return password

    def combine(self, *args):
        return upper_char + lower_char


p = Password()
print(p.length_strength(12))

print(p.combine(upper_char, lower_char))
print("password", p.gen(12))