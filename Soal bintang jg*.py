n = int(input("Masukkan n: "))
for i in range(n):
  print("*", end="")
  for _ in range(n-2):
    if i == 0 or i == n-1:
      print('*', end="")
    else:
      print('*', end="")
  print("*")
