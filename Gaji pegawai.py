status = input("Masukkan status pegawai (Tetap/Kontrak): ")
jum_anak = int(input("Masukkan jumlah anak: "))
gaji = 4000000
if status in ('Tetap', 'tetap'):
  gaji = 6000000
if jum_anak <= 3:
  gaji += (220000 * jum_anak)
else:
  gaji += (200000 * jum_anak)
print("Gaji anda adalah", gaji)
