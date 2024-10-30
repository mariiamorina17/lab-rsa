import random
import math



# Проверка, является ли число простым
def is_prime (number):
    if number < 2: # Если число меньше 2, то возвращаем ошибку
        return False
    for i in range (2, int(pow(number, 0.5)) + 1): # Ищем делители
        if number % i == 0:
            return False
    return True

# Генерация простого числа
def generate_prime (min_value, max_value):
    prime = random.randint(min_value, max_value) # Генерируем случайное число
    while not is_prime(prime): # Проверка сгенерированного числа на простоту
        prime = random.randint(min_value, max_value)
    return prime

# Поиск мультипликативного обратного
def mod_inverse(e, phi):
    for d in range (3, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError ("Мультипликативно обратного не существует")



# Вычисляем p и q
p, q = generate_prime(10000, 50000), generate_prime (10000, 50000)
while p==q:
    q = generate_prime(10000, 50000)

# Вычисляем n
n = p * q
# Вычисляем phi(n)
phi_n = (p -1 ) * (q - 1)

# Выбираем e
e = random.randint(3, phi_n - 1)
while math.gcd(e, phi_n) != 1: # Пока наибольший общий делитель не равен 1 (пока числа не являются взаимно простыми)
     e = random.randint (3, phi_n - 1)

# Вычисляем d
d = mod_inverse(e, phi_n)

# Ввод сообщения для дальнейшей работы
message = input("Введите сообщение, которое хотите зашифровать: ")

# Вывод расчитанных значений
print ("\nПростое число (p):", p)
print ("Простое число (q):", q)
print ("Целое число (e):", e)
print ("Мультипликативно обратное к числу e (d):", d)
print ("Модуль (n):", n)
print ("Значение функции Эйлера (phi(n)):", phi_n)

# Перевод сообщения в массив из ASCII-кодов
messagetoenc = [ord(ch) for ch in message]
# Вывод полученного значения
print ("\nСообщение, записанное с помощью ASCII-кодов:", messagetoenc)

# (m ^ e) mod n = c - получение зашифрованного сообщения
ciphertext = [pow(ch, e, n) for ch in messagetoenc]
# Вывод полученного значения
print ("\nЗашифрованное сообщение:", ciphertext, "\n")

# Получение сообщения из зашифрованного сообщения (результат представлен в ASCII-кодах)
decodedmessage = [pow(ch, d, n) for ch in ciphertext]
# Вывод полученных значений
print ("Расшифрованное сообщение, представленное с помощью ASCII-кодов:", decodedmessage)

# Переход от ASCII-кодов к символам
msg = "".join(chr(ch) for ch in decodedmessage)
# Расшифрованное сообщение
print("Расшифрованное сообщение:", msg)