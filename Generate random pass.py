import random

lower = "abcdefghijklmnopkrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"

all = lower + upper + number
length = int(input("input panjang password (8-16 karakter) : "))
password = "".join(random.sample(all, length))
print(password)