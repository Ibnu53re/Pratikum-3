max = 0

while True:
    bilangan = int(input("Masukan bilangan(0 untuk berhenti): "))
    if bilangan == 0:
        break
    if bilangan > max:
        max = bilangan

print(f"Bilangan terbesar: {max}")
