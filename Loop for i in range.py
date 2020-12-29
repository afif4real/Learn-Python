# n = int(input("Banyaknya nilai: "))
# jumlah = 0
# for i in range(n):
#   jumlah = jumlah + int(input("Masukkan nilai ke-{}: ".format(i+1)))
# print(jumlah)

n = int(input("Angka brp kek: "))
total = 0
jumlah = 0
for i in range(n):
  i += 1
  jumlah = int(input(f"angka ke-{i} "))
  total += jumlah
print(total)
  