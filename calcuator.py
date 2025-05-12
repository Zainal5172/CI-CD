def penjumlahan(a, b):
    return int(a + b)

def pengurangan(a, b):
    return int(a - b)

def Pembagian(a, b):
    return int(a * b)

def Perkalian(a, b):
    if b == 0:
        return "Error: Pembagian dengan nol tidak diperbolehkan"
    return int(a / b)

def main():
    print("=== KALKULATOR SEDERHANA ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Pembagian")
    print("4. Perkalian")

    pilihan = input("Pilih operasi (1/2/3/4): ")

    if pilihan in ["1", "2", "3", "4"]:
        try:
            x = int(input("Masukkan angka pertama: "))
            y = int(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input tidak valid. Harus berupa angka bulat.")
            return

        if pilihan == "1":
            hasil = penjumlahan(x, y)
        elif pilihan == "2":
            hasil = pengurangan(x, y)
        elif pilihan == "3":
            hasil = Pembagian(x, y)
        elif pilihan == "4":
            hasil = Perkalian(x, y)

        print(f"Hasil: {hasil}")
    else:
        print("Operasi tidak valid")

if __name__ == "__main__":
    main()
        