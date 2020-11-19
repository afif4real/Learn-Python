total = input(("Masukkan Total Belanja:"))
member = input(("Apakah member Ya atau Tidak: "))
total = int(total)

if member == 'Ya':
    if total > 500000 and total < 1000000:
        print("Anda mendapat diskon 7%")
    elif total > 1000000:
        print("Anda mendapat diskon 8%")
    else:
        print("Anda mendapat diskon 5%")
elif member == 'Tidak':
    if total > 500000 and total < 1000000:
        print("Anda mendapat diskon 2%")
    elif total > 1000000:
        print("Anda mendapat diskon 3%")
    else:
        print("Anda Tidak mendapat diskon")
