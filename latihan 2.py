print("=== VALIDASI DAFTAR NILAI ===")

nilai = [80, 90, 'A', 70, 100, 'B']

jumlah = 0
hitung = 0

for n in nilai:
    try:
        angka = float(n)
        jumlah += angka
        hitung += 1
    except ValueError:
        print(f"Melewati data tidak valid: {n}")

if hitung > 0:
    rata = jumlah / hitung
    print("\nRata-rata nilai valid =", rata)
else:
    print("Tidak ada data nilai valid.")
