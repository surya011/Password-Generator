import random
#range of characters and sybols from which your password will be choosen.
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
#enter the length of password you want to generate
length = input('password length?')
length = int(length)

print('Your passwords are:')
password = ''
for c in range(length):
    password += random.choice(chars)
print(password)
