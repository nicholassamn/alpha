def main():
    print("Kalkulator Sederhana")
    while True:
        try:
            num1 = float(input("Masukkan angka pertama: "))
            op = input("Masukkan operasi (+, -, *, /): ")
            num2 = float(input("Masukkan angka kedua: "))
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
            again = input("Hitung lagi? (y/n): ")
            if again.lower() != 'y':
                break
        except ValueError:
            print("Input tidak valid")

if __name__ == "__main__":
    main()