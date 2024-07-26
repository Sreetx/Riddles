# main.py
#
# Copyright 2024 Programmer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
try:
    try:
        import sys, os, time, optparse, webbrowser, random, zlib
        from Extras.banner import banner
        from Extras.color.warna import orange
        from Extras.color.warna import putih
        from Extras.color.warna import merah
        from Extras.color.warna import hijau
        from Extras.color.warna import biru
        from Extras.color.warna import borange
        from Extras.color.warna import bputih
        from Extras.color.warna import bhijau
        from Extras.color.warna import bbiru
        from Extras.color.warna import bmerah
        from Extras.color.warna import kelabu
        from Extras.color.warna import borangekelip
        from Extras.color.warna import banmerah
        from Extras.color.warna import banhijau
        from Extras.color.warna import banorange
        from Extras.color.warna import reset
    except ImportError:
        print(' [!] Harap install ulang script ini dari repository github kami!');sys.exit()
    os.system('mkdir hasil')
    os.system('mkdir logs')
    os.system('cls || clear')
    try:
        import zipfile
        import rarfile
        from tqdm import tqdm
        import datetime
        import socket

    except ImportError:
        print(putih+' ['+banmerah+'!'+reset+putih+']'+borangekelip+' Module tidak lengkap'+reset)
        print(putih+' ['+banmerah+'!'+reset+putih+']'+reset+orange+' Module akan segera diinstall'+reset);time.sleep(1)
        if sys.platform in ['win32', 'win64']:
            os.system('pip install rarfile')
            os.system('pip install tqdm')
            os.system("pip install py7zr")
            sys.exit()
        if sys.platform in ['linux', 'linux2']:
            os.system('pip install rarfile')
            os.system('pip install tqdm')
            os.system('pip install py7zr')
            print(borange+' [*] Jika modul terpasang dengan baik tekan CTR+C, mulai Ulang script'+reset)
            enter = print(borange+" [*] Jika ada masalah dengan pip tekan enter untuk menginstall nya (for Debian and derivative users)"+reset)
            os.system('apt install python3-rarfile')
            os.system('apt install python3-tqdm')
            os.system('apt install python3-py7zr')
            sys.exit()
        else: pass
except KeyboardInterrupt: print(bputih+' ['+banmerah+'!'+reset+bputih+']'+reset+merah+' Canceled by USER!'+reset);sys.exit()

c = ""
def zips():
    try:
        def hasil(p):
            hpst = socket.gethostname()
            date = datetime.datetime.now()
            timestamp = date.strftime("%Y%m%d_%H%M%S")
            logs = f"logs/succed_{timestamp}.txt"
            filed = """#LOG FILE
#PASSWORD FOUND

# MODE: ZIP Brute Force
# Time: """+timestamp+"""
# Desk: Year/M/D_clock/M/S
# Zip File: """+f.split("/")[-1]+"""
# Directory: """+f+"""
# Password: """+p.decode().strip()+"""
# Device Model: """+hpst+"""

#################################
# Support Me!! IN YOUTUBE
"""
            print(reset+borange+"""
<=======================================>
 |"""+reset+putih+"""             Password Found    """+borange+"""       |
 >======================================<
 |"""+reset+""" Zip File: """+hijau+f.split("/")[-1]+reset+borange+"""
 |"""+reset+""" Zip Directory: """+hijau+f+borange+"""
 |"""+reset+""" Password: """, banhijau+p.decode().strip()+reset+borange+"""
 |"""+reset+""" Wordlist Directory: """+hijau+tebak+borange+"""
 |"""+reset+""" Log: """+hijau+"""~/logs/succed_"""+timestamp+reset+borange+"""
 |"""+reset+""" System: """+hijau+hpst+borange+"""
<=======================================>"""+reset+orange+"""
 [*] File sudah di ekstraksi dan disimpan di folder "hasil" di script ini
 [*] Terima Kasih karena telah menggunakan script ini"""+reset)
            bite = filed.encode('utf-8')
            with open(logs, 'wb') as fd:
                fd.write(bite)
            sys.exit()
            os.system("cls||clear")
    #EXECALGORITMA
        #TIME 
        waktu = datetime.datetime.now()
        times = waktu.strftime("%H%:%M%:%S")
        def jipa():
            print(kelabu+" ["+banorange+"#"+reset+kelabu+"] Masuk ke brute force mode algoritma"+reset)
            print(putih+" ["+banorange+times+reset+putih+"] Lanjutkan dulu aktifitas anda karena ini mungkin akan sangat lama"+reset)
            with zipfile.ZipFile(f) as z:
                for lenght in range(1, int(algoritma.total) + 1):
                    while True:
                        try:
                            p = ''.join(random.choices(algoritma.abjad, k=int(algoritma.total)))
                            print(kelabu+"\r ["+banhijau+"#"+reset+kelabu+"]"+orange+" Wordlist yang dibuat: "+reset+banhijau+str(p)+reset, end='', flush=True)
                            z.extractall('hasil', pwd=p.encode('utf-8'))
                            hasil(p)
                        except (EOFError, KeyboardInterrupt): print(kelabu+'\n ['+banmerah+'!'+reset+kelabu+'] '+merah+' Dibatalkan!'+reset);sys.exit()
                        except (RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile, zlib.error): continue
    
    #EXECNORMAL
        def jip():
            j = len(list(open(tebak, 'rb')))
            print(kelabu+' ['+banhijau+'*'+reset+kelabu+'] Jumlah kata yang akan dicek:'+hijau, j)
            with zipfile.ZipFile(f) as z, open(tebak, 'rb') as p:
                for p in tqdm(p, total=j, unit='word'):
                    try:
                        z.extractall('hasil', pwd=p.strip())
                        hasil(p)
                    except (EOFError, KeyboardInterrupt): print(kelabu+' ['+banmerah+'!'+reset+kelabu+'] '+merah+' Dibatalkan!'+reset);sys.exit()
                    except (RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile, zlib.error): continue
    #ZIP
        print(banner)
        print(kelabu+"\n ["+banorange+"ZIP"+reset+kelabu+"] Anda masuk dalam mode ekstraksi ZIP"+reset)
        f = input(kelabu+' ['+banhijau+'?'+reset+kelabu+'] Masukkan lokasi file zip anda: '+reset)
        algort = input(putih+" ["+banorange+"?"+reset+putih+"] Gunakan algoritma? [y/n]: "+reset)
        if algort.lower() == "y" or algort.lower() == "Y":
            try:
                from Extras import algoritma
            except ImportError as e:
                print(e)
                print(putih+" ["+banmerah+"!"+reset+putih+"] "+merah+"Modul hiang! Install ulang script ini dari repositori gw"+reset);sys.exit()
        elif algort.lower() == "n":
            tebak = input(kelabu+' ['+banhijau+'?'+reset+kelabu+'] Masukkan lokasi file wordlist anda: '+reset)
            if tebak is c:
                print(borange+' ['+reset+banmerah+'!'+reset+borange+'] '+merah+' Perhatikan penulisan path wordlist'+reset);sys.exit()
        else:
            tebak = input(kelabu+' ['+banhijau+'?'+reset+kelabu+'] Masukkan lokasi file wordlist anda: '+reset)
            if tebak is c:
                print(borange+' ['+reset+banmerah+'!'+reset+borange+'] '+merah+' Perhatikan penulisan path wordlist'+reset);sys.exit()
        print(putih+' \n['+banorange+'INFO'+reset+putih+'] '+orange+'Jika proses penebakan berhenti, itu artinya script menemukan kata yang tepat dan script mencoba untuk mengekstrak file tersebut'+reset)
        print(putih+'['+banorange+'INFO'+reset+putih+'] '+orange+'Ekstraksi akan segera dilakukan setelah password ditemukan\n'+reset)
      
# HASH
        try:
            param = zipfile.ZipFile(f)
        except (FileNotFoundError, zipfile.BadZipFile): print(borange+' ['+reset+banmerah+'!'+reset+borange+'] '+merah+'Terdeteksi bukan file zip atau anda salah memasukkan path. Koreksi penulisan path'+reset);sys.exit()
        
        if algort.lower() == "y" or algort.lower() == "Y":
            jipa()
        if algort.lower() == "n":
            jip()
        else:
            jip()
        print('Wordlist Habis')
    except (KeyboardInterrupt, EOFError): print(merah+'\n [!] CTRL+C Terdeteksi, keluar dari program....'+reset);sys.exit()
                
def rars():
    try:
        def hasil(pas, r, word):
            hpst = socket.gethostname()
            date = datetime.datetime.now()
            timestamp = date.strftime("%Y%m%d_%H%M%S")
            logs = f"logs/succed_{timestamp}.txt"
            filed = f"""#LOG FILE
#PASSWORD FOUND

# MODE: RAR Brute Force
# Time: {timestamp}
# Desk: Year/M/D_clock/M/S
# Rar File: {r.split("/")[-1]}
# Directory: {r}
# Password: {pas.decode().strip()}
# Device Model: {hpst}

#################################
# Support Me!! IN YOUTUBE
"""
            print(reset+borange+"""
<=======================================>
 |"""+reset+putih+"""             Password Found    """+borange+"""       |
 >======================================<
 |"""+reset+""" RAR File: """+hijau+r.split("/")[-1]+reset+borange+"""
 |"""+reset+""" RAR Directory: """+hijau+r+borange+"""
 |"""+reset+""" Password: """+banhijau+pas.decode().strip()+reset+borange+"""
 |"""+reset+""" Wordlist Directory: """+hijau+word+borange+"""
 |"""+reset+""" Log: """+hijau+"""~/logs/succed_"""+timestamp+reset+borange+"""
 |"""+reset+""" System: """+hijau+hpst+borange+"""
<=======================================>"""+reset+orange+"""
 [*] File sudah di ekstraksi dan disimpan di folder "hasil" di script ini
 [*] Terima Kasih karena telah menggunakan script ini"""+reset)
            bite = filed.encode('utf-8')
            with open(logs, 'wb') as fd:
                fd.write(bite)
            sys.exit()
            
    #RAR
        rarfile.UNRAR_TOOL ="unrar"
        os.system("cls||clear")
        print(banner)
        print(kelabu+"\n ["+banorange+"RAR"+reset+kelabu+"] Anda masuk dalam mode ekstraksi RAR"+reset)
        r = input(kelabu+' ['+banhijau+'?'+reset+kelabu+'] Masukkan lokasi file RAR anda: '+reset)
        word = input(kelabu+' ['+banhijau+'?'+reset+kelabu+'] Masukkan lokasi file wordlist: '+reset)
        try:
            ttl = len(list(open(word, "rb")))
        except FileNotFoundError:
            print(borange+' ['+reset+banmerah+'!'+reset+borange+'] '+merah+' Perhatikan penulisan path wordlist'+reset);sys.exit()
        try:
            param = rarfile.RarFile(r)
        except (FileNotFoundError, rarfile.BadRarFile, rarfile.NotRarFile):  print(borange+'\n ['+reset+banmerah+'!'+reset+borange+'] '+merah+'Terdeteksi bukan file RAR atau anda salah memasukkan path. Koreksi penulisan path!'+reset);sys.exit()
        print(putih+' \n['+banorange+'INFO'+reset+putih+'] '+orange+'Jika proses penebakan berhenti, itu artinya script menemukan kata yang tepat dan script mencoba untuk mengekstrak file tersebut'+reset)
        print(putih+'['+banorange+'INFO'+reset+putih+'] '+orange+'Ekstraksi akan segera dilakukan setelah password ditemukan\n'+reset)
        
    # HASH RAR
        print(kelabu+' ['+banhijau+'*'+reset+kelabu+'] Jumlah kata yang akan dicek:'+hijau, ttl)
        with rarfile.RarFile(r) as rr, open(word, 'rb') as rarf:
            rarf.seek(0)
            for pas in tqdm(rarf, total=ttl, unit='word'):
                try:
                    rr.extractall('hasil', pwd=pas.rstrip())
                    hasil(pas, r, word)
                except KeyboardInterrupt:
                    print(merah+"\n [!] Dibatalkan!"+reset)
                    sys.exit()
                except (RuntimeError, rarfile.BadRarFile, rarfile.PasswordRequired):
                    continue
                except rarfile.RarCannotExec: 
                    print(kelabu+" ["+banmerah+"!"+reset+kelabu+"] "+reset+merah+"Utilitas yang dibutuhkan rarfile tidal tersedia. Install sendiri! (unrar)"+reset)
                    enter = input(kelabu+" ["+banorange+"DONWLOAD"+reset+kelabu+"]"+puith+" Enter untuk masuk ke halaman unduhan"+reset)
                    if chose.lower() == "":
                        import webbrowser
                        webbrower.open("https://www.rarlab.com/rar_add.htm")
                    sys.exit()

    except (KeyboardInterrupt, EOFError): print(merah+'\n [!] CTRL+C Terdeteksi, keluar dari program....'+reset);sys.exit()

def helpp():
    print(banner)
    print(putih+"\n[*] OPTIONS")
    print(orange+"   --rar    "+reset+"Digunakan untuk masuk ke opsi brute force password file rar")
    print(orange+"   --zip    "+reset+"Digunakan untuk masuk ke opsi brute force password file zip")
    print(orange+"   --hh    "+reset+"Digunakan untuk masuk ke opsi TAMPILAN UTAMA INI")
    print(putih+"\n[*] USAGE")
    print(orange+"   python3 "+sys.argv[0]+" --zip")
    print(orange+"   python3 "+sys.argv[0]+" --rar"+reset)
    print(orange+"   python3 "+sys.argv[0]+" --7z"+reset)
    sup = input(kelabu+" ["+banhijau+"?"+reset+kelabu+"] Yuk support Kami di YouTube ["+banhijau+"y/n"+reset+kelabu+"]: "+reset)
    if sup.lower() == "y" or sup.lower() == "Y":
        print(kelabu+" ["+banhijau+"*"+reset+kelabu+"]"+putih+" Terima kasih karena sudah support Kami... :)"+reset)
        webbrowser.open("https://www.youtube.com/@linggachannel4781")
        sys.exit()
    else: pass
    
def info():
    print(kelabu+"["+banhijau+"!"+reset+kelabu+"] "+putih+" Ketikan python3 "+sys.argv[0]+" --hh Untuk info lebih lanjut(Gk bisa otomatis bjir)\n"+reset)
    
def updates():
    try:
        import requests
        import socket
    except ImportError:
        print(putih+" ["+banmerah+"!"+reset+putih+"] python3-requests not found!"+reset)
        os.system("apt install python3-requests")
        os.system("pip install requests")
    print(kelabu+" ["+banorange+"UPDATE"+reset+kelabu+"]"+putih+" Checking Update..."+reset);time.sleep(0.2)
    print(kelabu+" ["+banorange+"UPDATE"+reset+kelabu+"]"+putih+" Installing Update..."+reset);time.sleep(0.2)
    req = requests.get("https://raw.githubusercontent.com/Sreetx/Riddles/master/src/main.py")
    req_str = req.content.decode("utf-8")
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        req.raise_for_status()
        with open(sys.argv[0], "w", encoding="utf-8") as fle:
            fle.write(req_str)
    except (socket.timeout, socket.gaierror): print(putih+" ["+banmerah+"!"+reset+putih+"] Cek koneksi internet kamu"+reset);sys.exit()
    print(kelabu+" ["+banorange+"UPDATE"+reset+kelabu+"]"+putih+" Succed..."+reset);sys.exit()
    
menu = optparse.OptionParser(info())
menu.add_option('--zip', dest="zipp", action='store_true', default=False)
menu.add_option('--rar', dest="rarr", action='store_true', default=False)
menu.add_option('--hh', dest="hh", action='store_true', default=False)
menu.add_option('--7z', dest='szip', action="store_true", default=False)
menu.add_option('--update', dest="update", action='store_true', default=False)

(option, args) = menu.parse_args()
rarr = option.rarr
zipp = option.zipp
hh = option.hh
sz = option.szip
update = option.update

if hh:
    os.system("cls||clear")
    helpp()
if zipp:
    os.system("cls||clear")
    zips()
if rarr:
    os.system("cls||clear")
    rars()
if sz:
    os.system("cls||clear")
    print(banner)
    try:
        import sevenzippy
        sevenzip.Sxc()
    except ImportError:
        szz = input(putih+" ["+banmerah+"!"+reset+putih+"]"+orange+" Install Riddles - 7Zip Cracker? "+kelabu+"["+banhijau+"y/n"+reset+kelabu+"]: "+reset)
        if szz.lower() == "y" or szz.lower() == "Y":
            try:
                import requests
                req = requests.get("https://raw.githubusercontent.com/Sreetx/Riddles/master/src/Extras/sevenzippy.py")
                req_str = req.content.decode("utf-8")
                with open("~/Riddles/src/Extras/sevenzippy.py", "w", encode="utf-8") as file:
                        file.write(req_str)
                print(borange+" [*] Terinsall! Mulai ulang script sekarang!");sys.exit()
            except ImportError:
                print(merah+" [+] Python3-requests akan diinstall terlebih dahulu untuk mengunduh script ini"+reset)
                os.system("pip install requests")
                enter = input(kelabu+" ["+banhijau+"?"+reset+kelabu+"] "+orange+"Jika requests terinstall dengan baik, tekan CTRL+C untuk keluar. Jika memikiki masalah dengan pip, tekan enter(for Debian and derivative users")
                os.system("apt install python3-requests")
        else:
            pass
if update:
    updates()
