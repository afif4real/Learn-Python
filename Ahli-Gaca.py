import random

while True:
    no_soal = int(input("Masukkan nomor soal('0' Untuk Esc): "))
    x = ("faris", "faris", "faris", "faris", "afif", "carlo", "akbar", "hilmi", "fachrur", "albani", "naufal", "adit", "dedy", "apis")

    a = random.choice(x)
    if no_soal != 0:
        print('nomor', no_soal, ':', a, '\n')

    elif no_soal == 0:
        break
print('Semoga Anda Beruntung')    
    
