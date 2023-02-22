import math

def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True

def rsa_encrypte(m, e, n):
    return m ** e % n

def rsa_decrypte(m1, d, n):
    return m1 ** d % n

print('Введите два простых числа')
p, q = int(input('p: ')), int(input('q: '))
while not is_prime(p) and not is_prime(q):
    print('Введите ПРОСТЫЕ числа')
    p, q = int(input('p: ')), int(input('q: '))

n = p * q
phi, e, d = (p - 1) * (q - 1), 0, 0
for i in range(2, p):
    if math.gcd(i, phi) == 1:
        e = i
        break
for i in range(1, phi):
    if e * i % phi == 1:
        d = i
        break

m = ord(input('Введите одну букву алфавита: '))
m1 = rsa_encrypte(m, e, n)
print(f'Зашифрованное число: {m1}')
m2 = rsa_decrypte(m1, d, n)
print(f'Расшифрованное число: {m2}')
print(f'Использованная буква: {chr(m2)}')