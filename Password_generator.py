import random
digits = '1234567890'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!#$%&*+-=?@^_'
chars = ''
chars_new = ''

print('Укажите количество паролей для генерации:')
password_quantity = int(input())

print('Укажите длину одного пароля:')
password_lenght = int(input())

print('Включать ли цифры 0123456789 ?')
digits_yes_no = input()
if digits_yes_no == 'да':
    chars += digits


print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ ?')
uppercase_yes_no = input()
if uppercase_yes_no == 'да':
    chars += uppercase_letters

print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz ?')
lowercase_yes_no = input()
if lowercase_yes_no == 'да':
    chars += lowercase_letters

print('Включать ли символы !#$%&*+-=?@^_ ?')
symbols_yes_no = input()
if symbols_yes_no == 'да':
    chars += symbols

print('Исключать ли неоднозначные символы il1Lo0O ?')
il1Lo0O_yes_no = input()
if il1Lo0O_yes_no == 'да':
    for i in range(len(chars)):
        if chars[i] not in 'il1Lo0O':
            chars_new += chars[i]
        else:
            continue
else:
    chars_new = chars

def generate_password(characters, lenght):
    for _ in range(password_quantity):
        print(*random.sample(characters, lenght), sep='')

generate_password(chars_new, password_lenght)