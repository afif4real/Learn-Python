hari = input(("Masukkan hari:"))
tanggal = input(("Masukkan tanggal:"))
YesNo =input(("Tanggal Merah: Ya atau Tidak? "))

if YesNo == 'Ya':
    print('Bebas')
elif hari == 'jumat' or 'Jumat':
    if tanggal == '1':
        print("Batik")
    else:
        print("Olah Raga")
else:
    print("Putih")
