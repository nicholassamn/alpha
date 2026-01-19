# Aplikasi game secret number

import random
import os

# Fungsi untuk load/save high score
def load_high_score():
    if os.path.exists("high_score.txt"):
        with open("high_score.txt", "r") as f:
            try:
                return int(f.read().strip())
            except:
                return 0
    return 0

def save_high_score(score):
    with open("high_score.txt", "w") as f:
        f.write(str(score))

# Aplikasi game secret number

import random
import os
import time

# Fungsi untuk load/save high score
def load_high_score():
    if os.path.exists("high_score.txt"):
        with open("high_score.txt", "r") as f:
            try:
                return int(f.read().strip())
            except:
                return 0
    return 0

def save_high_score(score):
    with open("high_score.txt", "w") as f:
        f.write(str(score))

def play_game(level):
    if level == 1:  # Mudah
        min_num, max_num = 1, 50
        max_attempts = 10
        point_penalty = 5
        win_multiplier = 2
    elif level == 2:  # Sedang
        min_num, max_num = 1, 100
        max_attempts = 10
        point_penalty = 10
        win_multiplier = 3
    elif level == 3:  # Sulit
        min_num, max_num = 1, 1000
        max_attempts = 15
        point_penalty = 15
        win_multiplier = 5

    secret_number = random.randint(min_num, max_num)
    attempts = 0
    points = 100
    hints_used = 0
    guesses = []
    start_time = time.time()

    print(f"\nSelamat datang di Game Tebak Angka - Level {level}!")
    print(f"Saya telah memilih angka rahasia antara {min_num} dan {max_num}.")
    print(f"Anda memiliki {max_attempts} kesempatan.")
    print(f"Poin awal: {points}")

    while attempts < max_attempts and points > 0:
        print(f"\nPercobaan {attempts + 1}/{max_attempts}, Poin: {points}")
        print("Pilih: 1. Tebak angka  2. Beli hint (biaya 20 poin)")

        try:
            choice = int(input("Masukkan pilihan: "))
        except ValueError:
            print("Pilihan tidak valid! Masukkan 1 atau 2.")
            continue

        if choice == 2:
            if points >= 20:
                points -= 20
                hints_used += 1
                parity = "genap" if secret_number % 2 == 0 else "ganjil"
                print(f"Hint: Angka rahasia adalah {parity}.")
            else:
                print("Poin tidak cukup untuk hint!")
            continue

        elif choice == 1:
            try:
                guess_number = int(input("Masukkan tebakan Anda: "))
            except ValueError:
                print("Masukkan angka yang valid!")
                continue

            attempts += 1
            guesses.append(guess_number)

            if guess_number == secret_number:
                final_points = points * win_multiplier
                end_time = time.time()
                duration = end_time - start_time
                print(f"Selamat! Tebakan Anda benar pada percobaan ke-{attempts}.")
                print(f"Hadiah: {final_points} poin virtual! (multiplier x{win_multiplier})")
                print(f"Gelar: 'Master Tebak Angka Level {level}'!")

                # Statistik
                print("\n=== Statistik Permainan ===")
                print(f"1. Berapa kali mencoba menebak: {attempts}")
                print(f"2. Skor akhir yang diperoleh: {final_points}")
                print(f"3. Lama waktu mencoba menebak: {duration:.2f} detik")
                print(f"4. Angka rahasia: {secret_number}")
                print(f"5. Angka apa saja yang telah ditebak: {', '.join(map(str, guesses))}")

                # Update high score
                high_score = load_high_score()
                if final_points > high_score:
                    save_high_score(final_points)
                    print(f"Skor tertinggi baru: {final_points}!")
                else:
                    print(f"Skor tertinggi saat ini: {high_score}")

                return final_points

            elif guess_number < secret_number:
                print("Tebakan Anda salah: terlalu rendah.")
            else:
                print("Tebakan Anda salah: terlalu tinggi.")

            points -= point_penalty
            if points < 0:
                points = 0

            if attempts < max_attempts:
                print(f"Kesempatan tersisa: {max_attempts - attempts}")

    # Game over
    end_time = time.time()
    duration = end_time - start_time
    print("Game Over!")
    if points <= 0:
        print("Poin Anda habis!")
    else:
        print(f"Anda telah kehabisan kesempatan.")
    print(f"Angka rahasianya adalah {secret_number}.")
    print("Konsekuensi: Mulai dari awal. Coba lagi nanti!")

    # Statistik
    print("\n=== Statistik Permainan ===")
    print(f"1. Berapa kali mencoba menebak: {attempts}")
    print(f"2. Skor akhir yang diperoleh: 0")
    print(f"3. Lama waktu mencoba menebak: {duration:.2f} detik")
    print(f"4. Angka rahasia: {secret_number}")
    print(f"5. Angka apa saja yang telah ditebak: {', '.join(map(str, guesses))}")

    return 0

def main():
    print("=== Game Tebak Angka Advanced ===")
    while True:
        print("\nPilih level kesulitan:")
        print("1. Mudah (1-50, 10 attempts)")
        print("2. Sedang (1-100, 10 attempts)")
        print("3. Sulit (1-1000, 15 attempts)")
        print("4. Keluar")

        try:
            level = int(input("Masukkan level (1-4): "))
            if level == 4:
                print("Terima kasih telah bermain!")
                break
            elif level in [1, 2, 3]:
                score = play_game(level)
                print(f"Skor Anda: {score}")
                again = input("Main lagi? (y/n): ")
                if again.lower() != 'y':
                    break
            else:
                print("Level tidak valid!")
        except ValueError:
            print("Input tidak valid!")

if __name__ == "__main__":
    main()