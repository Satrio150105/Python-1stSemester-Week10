def faktorial(n):
  if n == 0:
    return 1
  else:
    return n * faktorial(n - 1)
bilangan = int(input("Masukkan bilangan: "))
hasil = faktorial(bilangan)
print(f"Faktorial dari {bilangan} adalah {hasil}")