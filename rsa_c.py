import math
import base64

def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True

def key_generation(p, q):
    n = p * q
    phi, e, d = (p - 1) * (q - 1), 0, 0
    for i in range(2, max(p, q)):
        if math.gcd(i, phi) == 1:
            e = i
            break
    for i in range(1, phi):
        if e * i % phi == 1:
            d = i
            break
    return [n, phi, e, d]

def rsa_encrypte(m, e, n):
    return m ** e % n

def rsa_decrypte(m1, d, n):
    return m1 ** d % n

def encode_message(message, n, e):
    encode_line, encode_text = [], ''
    for i in message:
        encode_line.append(rsa_encrypte(ord(i), e, n))
    for i in encode_line:
        encode_text += chr(i)
    qw1 = base64.b64encode(encode_text.encode("UTF-8"))
    return qw1.decode("UTF-8")

def decode_message(encode_message, n, d):
    encode_line, decode_line, decode_text = [], [], ''
    qw2 = base64.b64decode(encode_message.encode("UTF-8"))
    encode_text = qw2.decode("UTF-8")
    for i in encode_text:
        encode_line.append(ord(i))
    for i in encode_line:
        decode_line.append(rsa_decrypte(i, d, n))
    for i in decode_line:
        decode_text += chr(i)
    return decode_text

print('Введите два различных простых числа')
p, q = int(input('p: ')), int(input('q: '))
while not is_prime(p):
    print('Введите ПРОСТОЕ число')
    p = int(input('p: '))
while not is_prime(q):
    print('Введите ПРОСТОЕ число')
    q = int(input('q: '))

n, phi, e, d = key_generation(p, q)
message = input('Введите сообщение: ')
encode_text = encode_message(message, n, e)
print(f'Зашифрованное сообщение: {encode_text}')
decode_text = decode_message(encode_text, n, d)
print(f'Расшифрованное сообщение: {decode_text}')