from decimal import Decimal, getcontext
import math

# Set presisi tinggi untuk akurasi
getcontext().prec = 28

def main():
    print("Kalkulator Advanced")
    history = []

    while True:
        print("\nPilih mode:")
        print("1. Basic (+, -, *, /)")
        print("2. Scientific (pangkat, akar, log, sin, cos, tan)")
        print("3. Lihat history")
        print("4. Keluar")

        try:
            mode = int(input("Masukkan pilihan (1-4): "))
        except ValueError:
            print("Input tidak valid. Masukkan angka 1-4.")
            continue

        if mode == 4:
            print("Terima kasih telah menggunakan kalkulator!")
            break

        elif mode == 3:
            if history:
                print("\nHistory Perhitungan:")
                for i, calc in enumerate(history, 1):
                    print(f"{i}. {calc}")
            else:
                print("Belum ada perhitungan.")
            continue

        elif mode == 1:  # Basic
            try:
                num1 = Decimal(input("Masukkan angka pertama: "))
                op = input("Masukkan operasi (+, -, *, /): ")
                num2 = Decimal(input("Masukkan angka kedua: "))

                if op == '+':
                    result = num1 + num2
                elif op == '-':
                    result = num1 - num2
                elif op == '*':
                    result = num1 * num2
                elif op == '/':
                    if num2 == 0:
                        print("Error: Pembagian dengan nol")
                        continue
                    result = num1 / num2
                else:
                    print("Operasi tidak valid")
                    continue

                print(f"Hasil: {result}")
                history.append(f"{num1} {op} {num2} = {result}")

            except (ValueError, decimal.InvalidOperation):
                print("Input tidak valid atau operasi tidak mungkin")

        elif mode == 2:  # Scientific
            print("Pilih operasi:")
            print("1. Pangkat (num1 ** num2)")
            print("2. Akar kuadrat (sqrt(num))")
            print("3. Logaritma natural (ln(num))")
            print("4. Sinus (sin(num))")
            print("5. Cosinus (cos(num))")
            print("6. Tangen (tan(num))")

            try:
                sub_mode = int(input("Masukkan pilihan (1-6): "))
            except ValueError:
                print("Input tidak valid.")
                continue

            try:
                if sub_mode in [1, 4, 5, 6]:  # Butuh dua angka atau satu dengan derajat
                    if sub_mode == 1:
                        num1 = float(input("Masukkan basis: "))
                        num2 = float(input("Masukkan eksponen: "))
                        result = num1 ** num2
                        calc_str = f"{num1} ** {num2} = {result}"
                    else:
                        num = float(input("Masukkan angka (dalam derajat untuk trig): "))
                        if sub_mode == 4:
                            result = math.sin(math.radians(num))
                            calc_str = f"sin({num}°) = {result}"
                        elif sub_mode == 5:
                            result = math.cos(math.radians(num))
                            calc_str = f"cos({num}°) = {result}"
                        elif sub_mode == 6:
                            result = math.tan(math.radians(num))
                            calc_str = f"tan({num}°) = {result}"

                elif sub_mode == 2:
                    num = float(input("Masukkan angka: "))
                    if num < 0:
                        print("Error: Akar kuadrat dari angka negatif")
                        continue
                    result = math.sqrt(num)
                    calc_str = f"sqrt({num}) = {result}"

                elif sub_mode == 3:
                    num = float(input("Masukkan angka: "))
                    if num <= 0:
                        print("Error: Logaritma dari angka <= 0")
                        continue
                    result = math.log(num)
                    calc_str = f"ln({num}) = {result}"

                else:
                    print("Pilihan tidak valid")
                    continue

                print(f"Hasil: {result}")
                history.append(calc_str)

            except ValueError:
                print("Input tidak valid")

        else:
            print("Pilihan mode tidak valid")

if __name__ == "__main__":
    main()