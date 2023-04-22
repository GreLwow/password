from random import *

uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
punctuation = '!#$%&*+-=?@^_'
digits = '23456789'
bad_symbols = 'il1Lo0O'
chars = ''

def get_quantity(): 
    try:
        quantity = int(input('Какое количество паролей Вам нужно?\n'))
        if quantity < 0: 
            return get_quantity()
        return quantity
    except:
        return get_quantity()


def block_questions():
    global chars
    digits_q = input('Включать ли цифры?\n')

    if digits_q.lower() == 'да':
        chars += digits
    elif digits_q.lower() == 'нет':
        print('Удаляю цифры.')
    else:
        block_questions()

    up_letters_q = input('Включать ли прописные буквы?\n')

    if up_letters_q.lower() == 'да':
        chars += uppercase_letters
    elif up_letters_q.lower() == 'нет':
        print('Удаляю прописные буквы.')
    else:
        block_questions()
            
    low_letters = input('Включать ли строчные буквы?\n')

    if low_letters.lower() == 'да':
        chars += lowercase_letters
    elif low_letters.lower() == 'нет':
        print('Удаляю строчные буквы.')
    else:
        block_questions()

    punc = input('Включать ли символы?\n')

    if punc.lower() == 'да':
        chars += punctuation
    elif punc.lower() == 'нет':
        print('Удаляю символы.')
    else: 
        block_questions()

    strange_symbs = input('Включать неоднозначные символы?\n')
    if strange_symbs.lower() == 'да':
        chars += bad_symbols
    elif strange_symbs.lower() == 'нет':
        print('Удаляю неоднозначные символы.')
    else:
        block_questions()
    return chars



def generate_password(length):
    q = get_quantity()
    chars = block_questions()
    if not chars:
        print('Ошибка: строка chars пуста.')
        return
    if len(chars) < length:
        print('Ошибка: строка chars короче требуемой длины пароля.')
        return
    for _ in range(q):
        length = randint(10, 16)
        password = ''.join([choice(chars) for _ in range(length)])
        print(password)


length = 0

generate_password(length)