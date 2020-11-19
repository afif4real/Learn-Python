hari = input("masukan hari:")
if hari in ('Senin', 'Selasa', 'Rabu', 'Kamis', 'Jum\'at', 'Sabtu', 'Minggu'):
    if hari == 'Senin':
        print('1')
    elif hari == 'Selasa':
        print('2')
    elif hari == 'Rabu':
        print('3')
    elif hari == 'Kamis':
        print('4')
    elif hari == 'Jum\'at':
        print('5')
    elif hari == 'Sabtu':
        print('6')
    elif hari == 'Minggu':
        print('7')
else:
    print('Tidak valid')
