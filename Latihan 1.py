print("=== KALKULATOR AMAN ===")

try:
    # Input angka pertama
    num1 = float(input("Masukkan angka pertama: "))

    # Input angka kedua
    num2 = float(input("Masukkan angka kedua: "))

    # Input operator
    op = input("Masukkan operator (+, -, *, /): ")

    # Proses perhitungan
    if op == "+":
        hasil = num1 + num2
    elif op == "-":
        hasil = num1 - num2
    elif op == "*":
        hasil = num1 * num2
    elif op == "/":
        try:
            hasil = num1 / num2
        except ZeroDivisionError:
            print("Error: Tidak bisa membagi dengan nol!")
            raise SystemExit
    else:
        # Jika operator tidak valid → error kustom
        raise Exception("Operator tidak valid! Gunakan +, -, *, atau /")

    print("Hasil:", hasil)

# Menangani input yang bukan angka
except ValueError:
    print("Error: Input harus berupa angka!")

# Menangani error lain (custom)
except Exception as e:
    print("Kesalahan:", e)
