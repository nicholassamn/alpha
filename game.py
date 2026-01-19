# Aplikasi game secret number

import random

# Pilih angka rahasia secara acak antara 1 dan 100
secret_number = random.randint(1, 100)
max_attempts = 10
attempts = 0

print("Selamat datang di Game Tebak Angka!")
print("Saya telah memilih angka rahasia antara 1 dan 100.")
print(f"Anda memiliki {max_attempts} kesempatan untuk menebak.")

while attempts < max_attempts:
    try:
        guess_number = int(input("Masukkan tebakan Anda: "))
        attempts += 1

        if guess_number == secret_number:
            print(f"Selamat! Tebakan Anda benar pada percobaan ke-{attempts}.")
            print("Hadiah: Anda mendapatkan 100 poin virtual dan gelar 'Master Tebak Angka'!")
            break
        elif guess_number < secret_number:
            print("Tebakan Anda terlalu rendah.")
        else:
            print("Tebakan Anda terlalu tinggi.")

        if attempts < max_attempts:
            print(f"Kesempatan tersisa: {max_attempts - attempts}")
    except ValueError:
        print("Masukkan angka yang valid!")

if attempts == max_attempts and guess_number != secret_number:
    print("Game Over! Anda telah kehabisan kesempatan.")
    print(f"Angka rahasianya adalah {secret_number}.")
    print("Konsekuensi: Anda harus mulai dari awal. Coba lagi nanti!")

print("Terima kasih telah bermain!")