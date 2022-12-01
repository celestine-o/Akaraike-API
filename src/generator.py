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

strength = 0

class Password:

    def length(self):
        length = 0
        match [length > 8, length > 12]:
            case [False, False]:
                strength += 0
            case [True, False]:
                strength += 1
            case [True, True]:
                strength += 2
        return strength

    