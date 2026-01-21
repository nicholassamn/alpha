import os
import sys
import time
import random
import threading

# ANSI escape codes for colors
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

def slow_print(text, delay=0.03):
    """Print text with typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    """Clear the terminal screen."""
    os.system('clear' if os.name == 'posix' else 'cls')

class GameEngine:
    def __init__(self):
        self.day_count = 1
        self.oxygen_level = 100
        self.power_level = 100
        self.sanity_meter = 100
        self.signals = []  # List of discovered signals
        self.signal_counter = 0  # Counter for signal IDs
        self.data_points = 0  # Points collected from survivors
        self.running = True

    def render_ui(self):
        """Render the game UI."""
        clear_screen()
        print("""
╔══════════════════════════════════════════════════════════════╗
║                    MONITOR STASIUN ATLAS-4                   ║
╠══════════════════════════════════════════════════════════════╣
║ Hari: {day} | Oksigen: {oxygen}% | Energi: {power}% | Kewarasan: {sanity}% | Data: {data} ║
╚══════════════════════════════════════════════════════════════╝
        """.format(day=self.day_count, oxygen=self.oxygen_level, power=self.power_level, sanity=self.sanity_meter, data=self.data_points))

    def check_fail_state(self):
        """Check if game over conditions are met."""
        if self.oxygen_level <= 0 or self.sanity_meter <= 0 or self.power_level <= 0:
            slow_print(Colors.RED + "KEGAGALAN SISTEM: TINGKAT KRITIS DICAPAI. STASIUN TERKOMPROMI." + Colors.RESET)
            self.running = False
            return True
        return False

    def check_win_state(self):
        """Check if win conditions are met."""
        if self.day_count >= 7 and self.data_points >= 50:
            slow_print(Colors.GREEN + "SELAMAT! ANDA BERHASIL BERTAHAN SELAMA 7 HARI DAN MENGUMPULKAN DATA YANG CUKUP. BANTUAN SEDANG DALAM PERJALANAN." + Colors.RESET)
            self.running = False
            return True
        return False

    def advance_day(self):
        """Advance to the next day."""
        self.day_count += 1
        # Simulate resource drain
        self.oxygen_level = max(0, self.oxygen_level - random.randint(5, 15))
        self.power_level = max(0, self.power_level - random.randint(5, 15))
        self.sanity_meter = max(0, self.sanity_meter - random.randint(0, 10))

class SignalGenerator:
    def __init__(self, game_engine):
        self.game_engine = game_engine
        self.survivor_templates = [
            "Kami butuh bantuan... koordinat: {coords}",
            "Persediaan makanan habis... tolong respon",
            "Penghuni selamat terdeteksi di sektor {sector}...",
            "Sinyal darurat dari koloni {sector}... harap bantu evakuasi",
            "Pesan dari kapal selamat: {coords}, butuh energi",
        ]
        self.anomaly_templates = [
            "Mata di dinding... mengawasi...",
            "Jangan lihat bulan... tidak aman",
            "Suara goresan dari ventilasi...",
            "Bisikan di kegelapan... mereka datang",
            "Cermin retak menunjukkan wajah asing...",
        ]

    def generate_signal(self, frequency):
        """Generate a signal based on frequency."""
        self.game_engine.signal_counter += 1
        signal_id = self.game_engine.signal_counter
        signal_type = random.choice(['survivor', 'anomaly'])
        if signal_type == 'survivor':
            template = random.choice(self.survivor_templates)
            content = template.format(coords=f"{random.randint(100,999)}.{random.randint(10,99)}", sector=random.randint(1,10))
        else:
            content = random.choice(self.anomaly_templates)

        # Add corruption
        corruption_level = random.randint(0, 3)
        corrupted_content = self.corrupt_text(content, corruption_level)

        return {
            'id': signal_id,
            'frequency': frequency,
            'type': signal_type,
            'content': corrupted_content,
            'danger_level': 'high' if signal_type == 'anomaly' else 'low'
        }

    def corrupt_text(self, text, level):
        """Corrupt text with symbols."""
        corrupted = list(text)
        for _ in range(level):
            if corrupted:
                idx = random.randint(0, len(corrupted) - 1)
                corrupted[idx] = random.choice(['@', '#', '!', '?'])
        return ''.join(corrupted)

class TerminalInterface:
    def __init__(self, game_engine, signal_generator):
        self.game_engine = game_engine
        self.signal_generator = signal_generator

    def parse_command(self, command):
        """Parse user input command."""
        parts = command.lower().split()
        if not parts:
            return self.error_message("Tidak ada perintah dimasukkan.")

        cmd = parts[0]
        if cmd == 'scan':
            if len(parts) < 2:
                return self.error_message("SCAN memerlukan rentang frekuensi. Penggunaan: SCAN <frekuensi>")
            try:
                freq = float(parts[1])
                return self.scan_command(freq)
            except ValueError:
                return self.error_message("Frekuensi tidak valid.")
        elif cmd == 'analyze':
            if len(parts) < 3 or parts[1] != 'signal':
                return self.error_message("Penggunaan: ANALYZE SIGNAL <id>")
            try:
                signal_id = int(parts[2])
                return self.analyze_command(signal_id)
            except ValueError:
                return self.error_message("ID sinyal tidak valid.")
        elif cmd == 'save':
            if len(parts) < 3 or parts[1] != 'signal':
                return self.error_message("Penggunaan: SAVE SIGNAL <id>")
            try:
                signal_id = int(parts[2])
                return self.save_command(signal_id)
            except ValueError:
                return self.error_message("ID sinyal tidak valid.")
        elif cmd == 'purge':
            if len(parts) < 3 or parts[1] != 'signal':
                return self.error_message("Penggunaan: PURGE SIGNAL <id>")
            try:
                signal_id = int(parts[2])
                return self.purge_command(signal_id)
            except ValueError:
                return self.error_message("ID sinyal tidak valid.")
        elif cmd == 'help':
            return self.help_command()
        elif cmd == 'status':
            return self.status_command()
        elif cmd == 'quit' or cmd == 'keluar':
            self.game_engine.running = False
            return "Mematikan sistem..."
        else:
            return self.error_message("Perintah tidak dikenal.")

    def error_message(self, msg):
        return Colors.RED + f"KESALAHAN: {msg}" + Colors.RESET

    def scan_command(self, freq):
        """Handle SCAN command."""
        slow_print(Colors.YELLOW + f"Memindai sektor {freq}..." + Colors.RESET)
        # Simulate scanning with progress bar
        for i in range(0, 101, 10):
            time.sleep(0.2)
            sys.stdout.write(f"\r[{'|' * (i//10)}{'.' * (10 - i//10)}] {i}%")
            sys.stdout.flush()
        print()

        # Chance to find signal
        if random.random() < 0.7:  # 70% chance
            signal = self.signal_generator.generate_signal(freq)
            self.game_engine.signals.append(signal)
            slow_print(Colors.GREEN + f"SINYAL DITEMUKAN. ID: {signal['id']}" + Colors.RESET)
            slow_print(Colors.BLUE + f"KONTEN: {signal['content']}" + Colors.RESET)
            if signal['danger_level'] == 'high':
                slow_print(Colors.RED + "PERINGATAN: ANCAMAN BIOLOGIS TERDETEKSI DALAM POLA TEKS." + Colors.RESET)
            return "Sinyal diperoleh."
        else:
            slow_print(Colors.YELLOW + "Tidak ada sinyal terdeteksi. Kebisingan statis." + Colors.RESET)
            return "Pemindaian selesai."

    def analyze_command(self, signal_id):
        """Handle ANALYZE command."""
        signal = next((s for s in self.game_engine.signals if s['id'] == signal_id), None)
        if not signal:
            return self.error_message("Sinyal tidak ditemukan.")
        slow_print(Colors.BLUE + f"Menganalisis sinyal {signal_id}..." + Colors.RESET)
        time.sleep(1)
        slow_print(f"Jenis: {signal['type'].upper()}")
        slow_print(f"Tingkat Bahaya: {signal['danger_level'].upper()}")
        if signal['type'] == 'anomaly':
            # Mini-puzzle: Guess the word
            words = ["HOROR", "ENTITAS", "KEGELAPAN", "BISIKAN"]
            chosen = random.choice(words)
            clue = f"Kata yang hilang: {chosen[0]}...{chosen[-1]} (panjang {len(chosen)} huruf)"
            slow_print(Colors.YELLOW + f"Puzzle: {clue}" + Colors.RESET)
            guess = input("Tebak kata: ").strip().upper()
            if guess == chosen:
                slow_print(Colors.GREEN + "Benar! Analisis lengkap." + Colors.RESET)
            else:
                slow_print(Colors.RED + "Salah! Sanity -10." + Colors.RESET)
                self.game_engine.sanity_meter -= 10
        return "Analisis selesai."

    def save_command(self, signal_id):
        """Handle SAVE command."""
        signal = next((s for s in self.game_engine.signals if s['id'] == signal_id), None)
        if not signal:
            return self.error_message("Sinyal tidak ditemukan.")
        if signal['type'] == 'anomaly':
            self.game_engine.sanity_meter -= 30
            slow_print(Colors.RED + "ENTITAS HOROR TERDETEKSI! KEWARASAN MENURUN DRAMATIS." + Colors.RESET)
        else:
            self.game_engine.data_points += 20  # Gain data points
            slow_print(Colors.GREEN + "Data disimpan. Sumber daya diperoleh. Poin data +20." + Colors.RESET)
        self.game_engine.signals.remove(signal)
        return "Sinyal diproses."

    def purge_command(self, signal_id):
        """Handle PURGE command."""
        signal = next((s for s in self.game_engine.signals if s['id'] == signal_id), None)
        if not signal:
            return self.error_message("Sinyal tidak ditemukan.")
        slow_print(Colors.YELLOW + "Sinyal dihapus. Energi dikonsumsi: 15%" + Colors.RESET)
        self.game_engine.power_level -= 15
        self.game_engine.signals.remove(signal)
        return "Sinyal dihapus."

    def help_command(self):
        """Display help."""
        help_text = """
Perintah Tersedia:
- SCAN <frekuensi>: Memindai sinyal di frekuensi tertentu (contoh: SCAN 90.5) untuk mencari pesan dari survivor (aman) atau anomali (berbahaya).
- ANALYZE SIGNAL <id>: Menganalisis sinyal yang ditemukan (contoh: ANALYZE SIGNAL 1) untuk mengetahui jenis dan tingkat bahaya. Anomali mungkin ada puzzle.
- SAVE SIGNAL <id>: Menyimpan data sinyal (contoh: SAVE SIGNAL 1). Aman jika survivor (+20 data), tapi berisiko jika anomali (menurunkan kewarasan).
- PURGE SIGNAL <id>: Menghapus sinyal dengan aman (contoh: PURGE SIGNAL 1), mengkonsumsi energi tapi tanpa risiko.
- STATUS: Menampilkan status sistem saat ini (hari, oksigen, energi, kewarasan, data).
- HELP: Menampilkan bantuan ini.
- QUIT/KELUAR: Keluar dari permainan.

Tujuan: Bertahan sampai hari 7 dengan mengumpulkan minimal 50 poin data. Jika oksigen/energi/kewarasan 0, game over.

"Aman" berarti sinyal dari survivor (tidak berbahaya). Jika anomali, SAVE bisa menyebabkan kegilaan. Situasi khusus: Anomali sering mengandung kata-kata horor seperti "mata di dinding" atau "suara goresan".

Tekan Enter untuk melanjutkan...
        """
        print(Colors.BLUE + help_text + Colors.RESET)
        input()  # Tunggu user tekan enter
        return ""  # Return empty to avoid double printing

    def status_command(self):
        """Show status."""
        return f"Hari: {self.game_engine.day_count} | Oksigen: {self.game_engine.oxygen_level}% | Energi: {self.game_engine.power_level}% | Kewarasan: {self.game_engine.sanity_meter}% | Data: {self.game_engine.data_points}"

def main():
    # Intro
    clear_screen()
    slow_print(Colors.GREEN + "Selamat datang di ECHO PROTOCOL: The Last Watcher" + Colors.RESET)
    slow_print("Anda adalah Operator Stasiun Luar Angkasa Atlas-4 yang telah ditinggalkan.")
    slow_print("Bumi telah hancur, dan tugas Anda adalah memantau sinyal radio dari sisa-sisa manusia atau ancaman asing.")
    slow_print("Kelola energi, oksigen, dan kewarasan Anda untuk bertahan hidup.")
    slow_print("Apakah Anda ingin memulai permainan? (y/n)")
    while True:
        choice = input().strip().lower()
        if choice == 'y':
            break
        elif choice == 'n':
            slow_print("Permainan dibatalkan.")
            return
        else:
            slow_print("Masukkan 'y' untuk ya atau 'n' untuk tidak.")

    game_engine = GameEngine()
    signal_generator = SignalGenerator(game_engine)
    terminal = TerminalInterface(game_engine, signal_generator)

    # Boot sequence
    clear_screen()
    slow_print(Colors.GREEN + "SISTEM REBOOT..." + Colors.RESET)
    time.sleep(1)
    slow_print("ATLAS-4 OS VERSI 9.0")
    slow_print("SISTEM HIDUP: 100%")
    slow_print("SUHU EKSTERNAL: -270°C")
    time.sleep(1)

    # Tutorial
    slow_print("Selamat bergabung di stasiun Atlas-4. Tugas Anda:")
    slow_print("1. Gunakan SCAN <frekuensi> (contoh: SCAN 90.5) untuk mencari sinyal.")
    slow_print("2. ANALYZE SIGNAL <id> (contoh: ANALYZE SIGNAL 1) sinyal yang ditemukan.")
    slow_print("3. SAVE SIGNAL <id> jika aman (survivor), PURGE SIGNAL <id> jika berbahaya (anomali).")
    slow_print("   Aman: Sinyal dari manusia selamat. Berbahaya: Anomali horor yang bisa gila.")
    slow_print("4. Pantau STATUS Anda. Bertahan sampai hari 7 dengan 50+ data poin untuk menang!")
    slow_print("5. Gunakan HELP kapan saja.")
    slow_print("Tekan Enter untuk memulai...")
    input()

    while game_engine.running:
        game_engine.render_ui()
        print(Colors.BLUE + "Perintah Tersedia: SCAN, ANALYZE, SAVE, PURGE, STATUS, HELP, QUIT/KELUAR" + Colors.RESET)
        if game_engine.check_fail_state() or game_engine.check_win_state():
            break
        command = input(Colors.GREEN + "> PERINTAH? " + Colors.RESET).strip()
        response = terminal.parse_command(command)
        slow_print(response)
        input("Tekan Enter untuk melanjutkan...")  # Tunggu user sebelum lanjut

        # Advance day occasionally (simplified)
        if random.random() < 0.1:  # 10% chance
            game_engine.advance_day()
            slow_print(Colors.YELLOW + "Hari maju. Sumber daya berkurang." + Colors.RESET)

        # Random horror event
        if random.random() < 0.05:  # 5% chance per command
            slow_print(Colors.RED + "PERINGATAN: SUARA ANEH DARI KORIDOR... KEWARASAN -5." + Colors.RESET)
            game_engine.sanity_meter = max(0, game_engine.sanity_meter - 5)

if __name__ == "__main__":
    main()
