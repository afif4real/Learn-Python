def hitungVolumeSilinder(r, t):
  pi = 3.14
  return pi * r**2 * t

def isiAir(volume_teko, r_gelas, list_tinggigelas):
  jumlah_gelas = 0
  gelas_penuh = True
  i = 0
  while i < len(list_tinggigelas) and gelas_penuh:
    volume_gelas = hitungVolumeSilinder(r_gelas, list_tinggigelas[i])
    if volume_teko - volume_gelas >= 0:
      jumlah_gelas = jumlah_gelas + 1
      volume_teko = volume_teko - volume_gelas
    i = i + 1
  return jumlah_gelas

volume_teko = int(input())
r_gelas = int(input())
list_tinggigelas = list(map(int, input().split()))
print(isiAir(volume_teko, r_gelas, list_tinggigelas))
