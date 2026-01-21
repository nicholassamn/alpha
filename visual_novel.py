# Visual Novel: The Deceptive Detective
# Game antimainstream dengan alur tak terduga

import time
import random

def intro():
    print("🌑 === The Deceptive Detective === 🌑")
    print("\nKamu adalah Detektif Alex Thorne, detektif legendaris yang selalu memecahkan kasus paling rumit.")
    print("Tapi malam ini, segalanya berubah. Kamu bangun di sel penjara, dituduh membunuh bos mafia terbesar di kota.")
    print("Darah di tanganmu, senjata di sampingmu. Tapi kamu tidak ingat apa-apa.")
    print("Apakah kamu dijebak? Atau ada rahasia gelap yang kamu sembunyikan?")
    print("\nTekan Enter untuk memulai...")
    input()

def scene1():
    print("\n🔍 Scene 1: Interogasi dengan Kapten Ramirez")
    print("Kapten Ramirez: 'Alex, di mana kamu malam pembunuhan itu terjadi?'")
    print("\nPilih dialogmu:")
    print("1. 'Saya sedang menyelidiki kasus korupsi internal polisi.'")
    print("2. 'Saya tidak ingat... kepalaku sakit.'")
    print("3. 'Saya bersama saksi utama, Maria.'")
    choice = input("Pilihan (1-3): ")
    return choice

def scene2(choice1):
    if choice1 == '1':
        print("\n🔍 Scene 2: Penyelidikan Korupsi")
        print("Kamu mengungkap korupsi, tapi menemukan bukti bahwa kamu yang membunuh bos mafia untuk menutupi jejak.")
        print("Kapten Ramirez: 'Kamu pikir aku bodoh? Ini sidik jarimu!'")
        print("\nPilih dialogmu:")
        print("1. 'Ini jebakan! Rekanku yang lakukan.'")
        print("2. 'Aku bersalah... aku monster.'")
        print("3. 'Tunggu, ini mimpi!'")
        choice = input("Pilihan (1-3): ")
        return 'corrupt_' + choice
    elif choice1 == '2':
        print("\n🔍 Scene 2: Amnesia Misterius")
        print("Dokter datang, kamu menderita amnesia. Tapi saat hipnosis, kamu mengingat sesuatu yang mengerikan.")
        print("Kamu melihat dirimu sendiri membunuh bos mafia... tapi itu bukan kamu, itu klonmu!")
        print("\nPilih dialogmu:")
        print("1. 'Aku bukan manusia asli!'")
        print("2. 'Ini konspirasi pemerintah.'")
        print("3. 'Aku harus bunuh diri untuk hentikan ini.'")
        choice = input("Pilihan (1-3): ")
        return 'amnesia_' + choice
    elif choice1 == '3':
        print("\n🔍 Scene 2: Bertemu Maria")
        print("Maria: 'Alex, aku melihatmu malam itu. Kamu tidak bersalah.'")
        print("Tapi saat kalian bicara, Maria mengeluarkan pistol. 'Kamu yang bunuh suamiku!'")
        print("\nPilih dialogmu:")
        print("1. 'Tunggu, aku pikir bos mafia itu suamimu?'")
        print("2. 'Aku akan buktikan aku tidak bersalah.'")
        print("3. 'Baiklah, aku penjahatnya.'")
        choice = input("Pilihan (1-3): ")
        return 'maria_' + choice
    else:
        return 'invalid'

def ending(path):
    print("\n🌟 === Ending ===")
    if path == 'corrupt_1':
        print("Ending: The Betrayer")
        print("Rekanmu ternyata penjahatnya. Kamu dibebaskan, tapi kepercayaanmu hancur. Kamu menjadi detektif bayangan, memburu korupsi dari dalam kegelapan.")
    elif path == 'corrupt_2':
        print("Ending: The Monster Within")
        print("Kamu mengaku. Ternyata kamu memiliki kepribadian ganda. Kamu dikurung seumur hidup, tapi kepribadian jahatmu melarikan diri dan melanjutkan pembunuhan.")
    elif path == 'corrupt_3':
        print("Ending: Dream Eater")
        print("Ini mimpi! Kamu bangun di dunia nyata, tapi bos mafia adalah ayahmu. Kamu harus memilih: bunuh dia atau bergabung dengannya.")
    elif path == 'amnesia_1':
        print("Ending: Clone Conspiracy")
        print("Kamu menemukan lab rahasia. Kamu adalah klon dari detektif asli yang sudah mati. Kamu menghancurkan lab, tapi dunia tahu rahasiamu.")
    elif path == 'amnesia_2':
        print("Ending: Government Shadow")
        print("Pemerintah menutup kasus. Kamu direkrut sebagai agen rahasia, tapi kamu mulai curiga bahwa semua detektif adalah klon.")
    elif path == 'amnesia_3':
        print("Ending: Eternal Loop")
        print("Kamu bunuh diri, tapi bangun lagi di sel yang sama. Ini loop waktu. Kamu harus pecahkan teka-teki untuk keluar.")
    elif path == 'maria_1':
        print("Ending: Family Secret")
        print("Bos mafia adalah ayah Maria. Kamu tidak bunuh dia, tapi ayahmu yang lakukan. Kamu dan Maria memburu ayahmu bersama.")
    elif path == 'maria_2':
        print("Ending: Innocent Proof")
        print("Kamu buktikan dengan CCTV bahwa kamu dijebak. Kamu dibebaskan, tapi mafia memburu kalian. Kamu hidup dalam pelarian.")
    elif path == 'maria_3':
        print("Ending: Double Agent")
        print("Kamu akui. Ternyata kamu agen ganda untuk mafia. Kamu dibebaskan, tapi sekarang kamu bos baru.")
    else:
        print("Ending: Invalid Choice - The Void")
        print("Pilihanmu tidak valid. Kamu tersedot ke dimensi lain, di mana semua kemungkinan terjadi sekaligus.")

def main():
    intro()
    choice1 = scene1()
    path = scene2(choice1)
    ending(path)
    print("\nTerima kasih telah bermain! Apakah kamu ingin main lagi? (y/n)")
    again = input().lower()
    if again == 'y':
        main()
    else:
        print("Sampai jumpa!")

if __name__ == "__main__":
    main()