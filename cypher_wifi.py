import os
import sys
import time
import subprocess

os.system('')

# Cyberpunk Renk Paleti
CYAN = '\033[96m'
MAGENTA = '\033[95m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
RESET = '\033[0m'

def get_profiles():
    """Sistemdeki kayıtlı Wi-Fi profillerini listeler."""
    try:
        profiles = subprocess.check_output('netsh wlan show profiles', shell=True).decode('utf-8', errors='ignore')
        return [
            line.split(':')[1].strip()
            for line in profiles.split('\n')
            if 'All User Profile' in line or 'Tüm Kullanıcı Profili' in line
        ]
    except Exception:
        return []

def get_password(wifi):
    """Belirtilen ağın şifresini çeker."""
    try:
        result = subprocess.check_output(f'netsh wlan show profile name="{wifi}" key=clear', shell=True).decode('utf-8', errors='ignore')
        for line in result.split('\n'):
            if 'Key Content' in line or 'Anahtar İçeriği' in line:
                return line.split(':')[1].strip()
    except Exception:
        pass
    return "Bulunamadı / Açık Ağ"

def show_profile_details(wifi):
    """Seçilen profilin teknik detaylarını ekrana basar."""
    try:
        result = subprocess.check_output(f'netsh wlan show profile name="{wifi}"', shell=True).decode('utf-8', errors='ignore')
        print(f"\n{GREEN}--- [ '{wifi}' TEKNİK PROFİL DETAYLARI ] ---{RESET}")
        print(result)
    except Exception as e:
        print(f"{RED}[!] Detaylar alınamadı: {e}{RESET}")

def scan_nearby_networks():
    """Çevredeki tüm canlı Wi-Fi ağlarını tarar."""
    print(f"\n{YELLOW}[*] Etraftaki frekanslar taranıyor...{RESET}\n")
    try:
        output = subprocess.check_output('netsh wlan show networks mode=bssid', shell=True).decode('utf-8', errors='ignore')
        print(f"{CYAN}--- [ CANLI ÇEVRE AĞLARI ] ---{RESET}")
        print(output)
    except Exception as e:
        print(f"{RED}[!] Tarama başarısız: {e}{RESET}")

def scan_network_devices():
    """Ağdaki bağlı cihazların IP ve MAC adreslerini listeler (ARP)."""
    print(f"\n{YELLOW}[*] Yerel ağdaki (LAN/WLAN) aktif cihazlar tespit ediliyor...{RESET}\n")
    try:
        arp_output = subprocess.check_output('arp -a', shell=True).decode('utf-8', errors='ignore')
        print(f"{CYAN}{'IP ADRESİ':<20} | {'MAC ADRESİ':<20} | {'TİP':<10}{RESET}")
        print("-" * 55)
        for line in arp_output.split('\n'):
            parts = line.split()
            if len(parts) == 3 and '.' in parts[0]:
                print(f"{GREEN}{parts[0]:<20}{RESET} | {MAGENTA}{parts[1]:<20}{RESET} | {parts[2]:<10}")
    except Exception as e:
        print(f"{RED}[!] ARP taraması yapılamadı: {e}{RESET}")

def repair_dns():
    """DNS önbelleğini temizler ve ağı yeniler."""
    print(f"\n{YELLOW}[*] Ağ adaptörü ve DNS önbelleği temizleniyor...{RESET}\n")
    try:
        subprocess.run('ipconfig /flushdns', shell=True, check=True)
        print(f"{GREEN}[+] DNS Önbelleği başarıyla temizlendi.{RESET}")
    except Exception as e:
        print(f"{RED}[!] Onarım sırasında hata: {e}{RESET}")

def delete_profile(wifi):
    """Kayıtlı Wi-Fi profilini siler."""
    try:
        subprocess.run(f'netsh wlan delete profile name="{wifi}"', shell=True, check=True)
        print(f"\n{GREEN}[+] '{wifi}' profili sistemden silindi.{RESET}")
    except Exception as e:
        print(f"\n{RED}[!] Profil silinemedi: {e}{RESET}")

def generate_qr_string(ssid, password):
    if password and password != "Bulunamadı / Açık Ağ":
        return f"WIFI:S:{ssid};T:WPA;P:{password};;"
    return f"WIFI:S:{ssid};T:nopass;;"

def export_report(data):
    filename = "wifi_cyber_report.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=========================================\n")
        f.write("     CYBER-NET SYSTEM REPORT v3.1        \n")
        f.write("=========================================\n\n")
        for ssid, pwd in data:
            qr_str = generate_qr_string(ssid, pwd)
            f.write(f"SSID    : {ssid}\n")
            f.write(f"ŞİFRE   : {pwd}\n")
            f.write(f"QR CODE : {qr_str}\n")
            f.write("-" * 41 + "\n")
    print(f"\n{GREEN}[+] Rapor başarıyla '{filename}' dosyasına kaydedildi.{RESET}")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""{MAGENTA}{BOLD}
  /$$$$$$  /$$     /$$ /$$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$  /$$      /$$ /$$$$$$ /$$$$$$$$ /$$$$$$
 /$$__  $$|  $$   /$$/| $$__  $$| $$  | $$| $$_____/| $$__  $$| $$  /$ | $$|_  $$_/| $$_____/|_  $$_/
| $$  \__/ \  $$ /$$/ | $$  \ $$| $$  | $$| $$      | $$  \ $$| $$ /$$$| $$  | $$  | $$        | $$  
| $$        \  $$$$/  | $$$$$$$/| $$$$$$$$| $$$$$   | $$$$$$$/| $$/$$ $$ $$  | $$  | $$$$$     | $$  
| $$         \  $$/   | $$____/ | $$__  $$| $$__/   | $$__  $$| $$$$_  $$$$  | $$  | $$__/     | $$  
| $$    $$    | $$    | $$      | $$  | $$| $$      | $$  \ $$| $$$/ \  $$$  | $$  | $$        | $$  
|  $$$$$$/    | $$    | $$      | $$  | $$| $$$$$$$$| $$  | $$| $$/   \  $$ /$$$$$$| $$       /$$$$$$
 \______/     |__/    |__/      |__/  |__/|________/|__/  |__/|__/     \__/|______/|__/      |______/
                                                                                                     
                                                                                                     
                                                                                                     
        """)

        # ÖNEMLİ GÜVENLİK NOTU EKLENDİ
        print(f"{YELLOW}{BOLD}[ÖNEMLİ NOT: GÖSTERİLEN IP ADRESLERİ, ŞİFRELER VE HESAP PROFİLLERİ ÜÇÜNCÜ ŞAHIS İLE PAYLAŞILMAZ, BUNLAR SİZİN BİLGİSAYARINIZA KAYITLI OLMAKTADIR.]{RESET}\n")

        print(f"{CYAN}[1]{RESET} Tekli Ağ Şifresi & QR Bağlantı Kodu")
        print(f"{CYAN}[2]{RESET} Tüm Kayıtlı Ağları ve Şifreleri Tablo Yap")
        print(f"{CYAN}[3]{RESET} Çevredeki Canlı Wi-Fi Ağlarını Tara (Mode: BSSID)")
        print(f"{CYAN}[4]{RESET} Ağdaki Diğer Cihazları Bul (IP/MAC ARP Scan)")
        print(f"{CYAN}[5]{RESET} İnternet Bağlantı Onarımı (Flush DNS)")
        print(f"{CYAN}[6]{RESET} Tüm Ağ Raporunu Dosyaya Kaydet (.txt)")
        print(f"{CYAN}[7]{RESET} Eski / İstenmeyen Ağ Profilini Sil")
        print(f"{CYAN}[8]{RESET} Kayıtlı Profil Detaylarını Göster (Şifreleme / Güvenlik)")
        print(f"{RED}[0]{RESET} Çıkış\n")

        secim = input(f"{YELLOW}Sistem Komutu Seçin >> {RESET}").strip()

        if secim == '0':
            print(f"\n{GREEN}[*] Sistem kapatılıyor...{RESET}")
            break

        names = get_profiles()

        if secim == '1':
            if not names:
                print(f"{RED}[!] Kayıtlı profil bulunamadı.{RESET}")
            else:
                for i, n in enumerate(names, 1):
                    print(f"[{i:02d}] {n}")
                try:
                    ch = int(input("\nHedef Ağ No: "))
                    wifi = names[ch - 1]
                    pwd = get_password(wifi)
                    qr_code = generate_qr_string(wifi, pwd)
                    print(f"\n{GREEN}[+] SSID       : {wifi}{RESET}")
                    print(f"{GREEN}[+] ŞİFRE      : {pwd}{RESET}")
                    print(f"{CYAN}[+] QR DIZESI  : {qr_code}{RESET}")
                except (ValueError, IndexError):
                    print(f"{RED}[!] Geçersiz seçim.{RESET}")

        elif secim == '2':
            if not names:
                print(f"{RED}[!] Kayıtlı profil bulunamadı.{RESET}")
            else:
                print(f"\n{CYAN}{'AĞ ADI (SSID)':<30} | {'ŞİFRE':<20}{RESET}")
                print("-" * 55)
                for name in names:
                    pwd = get_password(name)
                    print(f"{BOLD}{name:<30}{RESET} | {YELLOW}{pwd:<20}{RESET}")

        elif secim == '3':
            scan_nearby_networks()

        elif secim == '4':
            scan_network_devices()

        elif secim == '5':
            repair_dns()

        elif secim == '6':
            if not names:
                print(f"{RED}[!] Kayıtlı profil bulunamadı.{RESET}")
            else:
                all_data = [(name, get_password(name)) for name in names]
                export_report(all_data)

        elif secim == '7':
            if not names:
                print(f"{RED}[!] Silinecek profil bulunamadı.{RESET}")
            else:
                for i, n in enumerate(names, 1):
                    print(f"[{i:02d}] {n}")
                try:
                    ch = int(input("\nSilinecek Ağ No: "))
                    wifi = names[ch - 1]
                    delete_profile(wifi)
                except (ValueError, IndexError):
                    print(f"{RED}[!] Geçersiz seçim.{RESET}")

        elif secim == '8':
            if not names:
                print(f"{RED}[!] Kayıtlı profil bulunamadı.{RESET}")
            else:
                print(f"\n{CYAN}=== KAYITLI PROFİLLER ==={RESET}")
                for i, n in enumerate(names, 1):
                    print(f"[{i:02d}] {n}")
                try:
                    ch = int(input("\nİncelenecek Profil No: "))
                    wifi = names[ch - 1]
                    show_profile_details(wifi)
                except (ValueError, IndexError):
                    print(f"{RED}[!] Geçersiz seçim.{RESET}")

        else:
            print(f"{RED}[!] Geçersiz komut.{RESET}")

        input(f"\n{MAGENTA}Devam etmek için Enter'a basın...{RESET}")

if __name__ == "__main__":
    main()
