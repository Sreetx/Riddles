# main.py
#
# Copyright 2024-2025 Programmer
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
        import sys, os, time, optparse, webbrowser, random, zlib, itertools
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
    os.system('mkdir Extras/hasil')
    os.system('mkdir logs')
    os.system('cls || clear')
    try:
        import zipfile
        import rarfile
        from tqdm import tqdm
        import datetime
        import socket
        import pyzipper
        import lzma
        import zlib
        import bz2
        import datetime
    except ImportError:
        print(putih+' ['+banmerah+'!'+reset+putih+']'+borangekelip+' Module tidak lengkap'+reset)
        print(putih+' ['+banmerah+'!'+reset+putih+']'+reset+orange+' Module akan segera diinstall'+reset);time.sleep(1)
        if sys.platform in ['win32', 'win64']:
            os.system('pip install rarfile')
            os.system('pip install tqdm')
            os.system("pip install py7zr")
            os.system('pip install pyzipper')
            sys.exit()
        if sys.platform in ['linux', 'linux2']:
            os.system('pip install rarfile')
            os.system('pip install tqdm')
            os.system('pip install pyzipper')
            print(borange+' [*] Jika modul terpasang dengan baik tekan CTR+C, mulai Ulang script'+reset)
            enter = print(borange+" [*] Jika ada masalah dengan pip tekan enter untuk menginstall nya (for Debian and derivative users)"+reset)
            os.system('apt install python3-rarfile')
            os.system('apt install python3-tqdm')
            os.system('apt install python3-py7zr')
            print(kelabu+" ["+banorange+"!"+reset+kelabu+"]"+putih+" Module pyzipper tetap harus diinstall pake pip, kalo pip lu error pake virtual enviroment (venv)"+reset)
            sys.exit()
        else: pass
except KeyboardInterrupt: print(bputih+' ['+banmerah+'!'+reset+bputih+']'+reset+merah+' Canceled by USER!'+reset);sys.exit()
waktu = datetime.datetime.now()
times = waktu.strftime("%H:%M:%S")
c = ""
def zips():
    try:
        def hasil(p, algort2, outp):
            hpst = socket.gethostname()
            date = datetime.datetime.now()
            timestamp = date.strftime("%Y%m%d_%H%M%S")
            tanggal = date.strftime("%D")
            jam = date.strftime("%H")
            menit = date.strftime("%M")
            logs = f"logs/succed_{timestamp}.txt"
            filed = """#LOG FILE
#PASSWORD FOUND

# MODE: ZIP Brute Force
# Time: """+tanggal+""" | """+jam+""":"""+menit+"""
# Desk: Year/M/D_clock/M/S
# Zip File: """+f.split("/")[-1]+"""
# Zip Encryption Type: """+str(outp)+"""
# Directory: """+f+"""
# Password: """+str(p).strip()+"""
# Device Model: """+hpst+"""

#################################
# Support Me!! IN YOUTUBE
"""
            try:
                print(reset+borange+"""
<=======================================>
 |"""+reset+putih+"""             Password Found    """+borange+"""       |
 >======================================<
 |"""+reset+""" Zip File: """+hijau+f.split("/")[-1]+reset+borange+"""
 |"""+reset+""" Zip Directory: """+hijau+f+borange+"""
 |"""+reset+""" Zip Encryption Type: """+hijau+str(outp)+reset)

                if algort2.lower() == "y" or algort2.lower() == "Y":
                    print(borange+""" |"""+reset+""" Password: """+banhijau+str(p)+reset)
                else:
                    print(borange+""" |"""+reset+""" Password: """+banhijau+p.decode().strip()+reset)
                    print(borange+""" |"""+reset+""" Wordlist Directory: """+hijau+tebak+reset)
                print(borange+""" |"""+reset+""" Log: """+hijau+"""~/logs/succed_"""+timestamp+reset+borange+"""
 |"""+reset+""" System: """+hijau+hpst+borange+"""
<=======================================>"""+reset+orange+"""
 [*] File sudah di ekstraksi dan disimpan di folder "hasil" di script ini
 [*] Terima Kasih karena telah menggunakan script ini"""+reset)
            except UnboundLocalError: pass
            bite = filed.encode('utf-8')
            with open(logs, 'wb') as fd:
                fd.write(bite)
            sys.exit()
            os.system("cls||clear")
    #EXECALGORITMA
        def jipa(algort2, outp):
            print(kelabu+" ["+banorange+"#"+reset+kelabu+"] Masuk ke brute force mode algoritma"+reset)
            print(putih+" ["+banorange+times+reset+putih+"] Lanjutkan dulu aktifitas anda karena ini mungkin akan sangat lama"+reset)
            if  algort2.lower() == "y" or algort2.lower() == "Y":
                with pyzipper.ZipFile(f) as z:
                    for lenght in range(1, + int(algoritma.total) + 1):
                        while True:
                            for passwodd in itertools.product(algoritma.abjad, repeat=int(algoritma.total)):
                                try:
                                    p = ''.join(passwodd)
                                    print(kelabu+"\r ["+banhijau+outp+reset+kelabu+"]"+orange+" Wordlist yang dibuat: "+reset+banhijau+str(p)+reset, end='', flush=True)
                                    z.extractall('hasil', pwd=p.encode("utf-8"))
                                    hasil(p, algort2, outp)
                                except (EOFError, KeyboardInterrupt): print(kelabu+'\n ['+banmerah+'!'+reset+kelabu+'] '+merah+' Dibatalkan!'+reset);sys.exit()
                                except (RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile, zlib.error, pyzipper.zipfile.BadZipFile): continue
            if algort2.lower() == "n" or algort2.lower() == "N":
                with pyzipper.ZipFile(f) as z:
                    for lenght in range(1, int(algoritma.total) + 1):
                        while True:
                            try:
                                p = ''.join    (random.choices(algoritma.abjad, k=int(algoritma.total)))
                                print(kelabu+"\r ["+banhijau+outp+reset+kelabu+"]"+orange+" Wordlist yang dibuat: "+reset+banhijau+str(p)+reset, end='', flush=True)
                                z.extractall('hasil', pwd=p.encode("utf-8"))
                                hasil(p, algort2, outp)
                            except (EOFError, KeyboardInterrupt): print(kelabu+'\n ['+banmerah+'!'+reset+kelabu+'] '+merah+' Dibatalkan!'+reset);sys.exit()
                            except (RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile, zlib.error, pyzipper.zipfile.BadZipFile): continue
    
    #EXECNORMAL
        def jip(outp):
            j = len(list(open(tebak, 'rb')))
            print(kelabu+' ['+banhijau+'*'+reset+kelabu+'] Jumlah kata yang akan dicek:'+hijau, j)
            algort2 = "n"
            with pyzipper.ZipFile(f) as z, open(tebak, 'rb') as p:
                for p in tqdm(p, total=j, unit='word', desc=outp):
                    try:
                        z.extractall('hasil', pwd=p.strip())
                        hasil(p, algort2, outp)
                    except (EOFError, KeyboardInterrupt): print(kelabu+' ['+banmerah+'!'+reset+kelabu+'] '+merah+' Dibatalkan!'+reset);sys.exit()
                    except (RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile, zlib.error, pyzipper.zipfile.BadZipFile): continue

    #EXEC ZIP AES NORMAL
        def zip_AES(outp):
            #input disni
            j = len(list(open(tebak, 'rb')))
            print(kelabu+' ['+banhijau+'*'+reset+kelabu+'] Jumlah kata yang akan dicek:'+hijau, j)
            algort2 = "n"
            with pyzipper.AESZipFile(f) as z, open(tebak, 'rb') as p:
                for p in tqdm(p, total=j, unit='word', desc=outp):
                    try:
                        z.extractall('hasil', pwd=p.strip())
                        hasil(p, algort2, outp)
                    except (EOFError, KeyboardInterrupt): print(kelabu+' ['+banmerah+'!'+reset+kelabu+'] '+merah+' Dibatalkan!'+reset);sys.exit()
                    except (RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile, zlib.error, pyzipper.zipfile.BadZipFile, lzma.LZMAError): continue

    #EXEC ZIP AES ALGORITMA
        def zip_AES_algoritma(algort2, outp):
            print(putih+ "["+banorange+"INFO"+reset+putih+"] Mode algroitma buat hash Zip AES blm tersedia"+reset)
            #input disini

    #ZIP
        print(banner)
        print(kelabu+"\n ["+banorange+"ZIP"+reset+kelabu+"] Anda masuk dalam mode ekstraksi ZIP"+reset)
        f = input(kelabu+' ['+hijau+'>'+reset+kelabu+'] Masukkan lokasi file zip anda: '+reset)
        f = f.strip()
        algort = input(putih+" ["+banorange+">"+reset+putih+"] Gunakan algoritma? [y/n]: "+reset)
        if algort.lower() == "y" or algort.lower() == "Y":
            algort2 = input(putih+" ["+banorange+">"+reset+putih+"] Gunakan algoritma tersusun? [y/n]: "+reset)
            try:
             from Extras import algoritma
            except ImportError as e:
                print(putih+" ["+banmerah+"!"+reset+putih+"] "+merah+"Modul hiang! Install ulang script ini dari repositori gw"+reset);sys.exit()
        elif algort.lower() == "n":
            tebak = input(kelabu+' ['+hijau+'>'+reset+kelabu+'] Masukkan lokasi file wordlist anda: '+reset)
            tebak = tebak.strip()
            if tebak is c:
                print(borange+' ['+reset+banmerah+'!'+reset+borange+'] '+merah+' Perhatikan penulisan path wordlist'+reset);sys.exit()
        else:
            tebak = input(kelabu+' ['+banhijau+'>'+reset+kelabu+'] Masukkan lokasi file wordlist anda: '+reset)
            if tebak is c:
                print(borange+' ['+reset+banmerah+'!'+reset+borange+'] '+merah+' Perhatikan penulisan path wordlist'+reset);sys.exit()
        print(putih+' \n['+banorange+'INFO'+reset+putih+'] '+orange+'Jika proses penebakan berhenti, itu artinya script menemukan kata yang tepat dan script mencoba untuk mengekstrak file tersebut'+reset)
        print(putih+'['+banorange+'INFO'+reset+putih+'] '+orange+'Ekstraksi akan segera dilakukan setelah password ditemukan\n'+reset)
      
# HASH
        try:
            with pyzipper.AESZipFile(f, 'r') as zf:
                for info in zf.infolist():
                    if info.flag_bits & 0x1:
                        if info.extract_version >= 51:
                            outp = "AES"
                        else:
                            outp = "ZipCrypto"
        except pyzipper.zipfile.BadZipFile: print(" [!] Zip FIle rusak")
        except FileNotFoundError: print(borange+' ['+reset+banmerah+'!'+reset+borange+'] '+merah+'Terdeteksi bukan file zip atau anda salah memasukkan path. Koreksi penulisan path'+reset);sys.exit()
        
        try:
            if outp is str('AES'):
                if algort.lower() == "y" or algort.lower() == "Y":
                    zip_AES_algoritma(algort2, outp)
                else:
                    zip_AES(outp)
                print('Wordlist Habis')
            if outp is str('ZipCrypto'):
                if algort.lower() == "y" or algort.lower() == "Y":
                    jipa(algort2, outp)
                else:
                    jip(outp)
                print('Wordlist Habis')
        
        except ImportError: print(putih+" ["+banmerah+"!"+reset+putih+"] "+merah+"Modul hiang! Install ulang script ini dari repositori gw"+reset);sys.exit()

    except (KeyboardInterrupt, EOFError): print(merah+'\n [!] CTRL+C Terdeteksi, keluar dari program....'+reset);sys.exit()
                
def rars():
    try:
        def hasil(pas, r, algort2):
            hpst = socket.gethostname()
            date = datetime.datetime.now()
            timestamp = date.strftime("%Y%m%d_%H%M%S")
            logs = f"logs/succed_{timestamp}.txt"
            filed = """#LOG FILE
#PASSWORD FOUND

# MODE: RAR Brute Force
# Time: """+timestamp+"""
# Desk: Year/M/D_clock/M/S
# Rar File: """+r.split("/")[-1]+"""
# Directory: """+r+"""
# Password: """+str(pas).strip()+"""
# Device Model: """+hpst+"""

#################################
# Support Me!! IN YOUTUBE
"""
            try:
                print(reset+borange+"""
<=======================================>
 |"""+reset+putih+"""             Password Found    """+borange+"""       |
 >======================================<
 |"""+reset+""" RAR File: """+hijau+r.split("/")[-1]+reset+borange+"""
 |"""+reset+""" RAR Directory: """+hijau+r+borange)

                if algort2.lower() == "y" or algort2.lower() == "Y":
                    print(borange+""" |"""+reset+""" Password: """+banhijau+str(pas)+reset)
                else:
                    print(borange+""" |"""+reset+""" Password: """+banhijau+pas.decode().strip()+reset)
                    print(borange+""" |"""+reset+""" Wordlist Directory: """+hijau+word+reset)
                print(borange+""" |"""+reset+""" Log: """+hijau+"""~/logs/succed_"""+timestamp+reset+borange+"""
 |"""+reset+""" System: """+hijau+hpst+borange+"""
<=======================================>"""+reset+orange+"""
 [*] File sudah di ekstraksi dan disimpan di folder "hasil" di script ini
 [*] Terima Kasih karena telah menggunakan script ini"""+reset)
            except UnboundLocalError: pass
            bite = filed.encode('utf-8')
            with open(logs, 'wb') as fd:
                fd.write(bite)
            sys.exit()
        #EXECALGORITMA
        def rara(algort2):
            from Extras import algoritma
            print(kelabu+" ["+banorange+"#"+reset+kelabu+"] Masuk ke RAR brute force mode algoritma"+reset)
            print(putih+" ["+banorange+times+reset+putih+"] Lanjutkan dulu aktifitas anda karena ini mungkin akan sangat lama"+reset)
            if  algort2.lower() == "y" or algort2.lower() == "Y":
                with rarfile.RarFile(r) as rr:
                    for lenght in range(1, + int(algoritma.total) + 1):
                        while True:
                            for passwodd in itertools.product(algoritma.abjad, repeat=int(algoritma.total)):
                                try:
                                    pas = ''.join(passwodd)
                                    print(kelabu+"\r ["+banhijau+"#"+reset+kelabu+"]"+orange+" Wordlist yang dibuat: "+reset+banhijau+str(pas)+reset, end='', flush=True)
                                    rr.extractall('hasil', pwd=pas.encode("utf-8"))
                                    hasil(pas, r, algort2)
                                except (RuntimeError, rarfile.BadRarFile, rarfile.PasswordRequired): continue
                                except rarfile.RarCannotExec:
                                    print(kelabu+" ["+banmerah+"!"+reset+kelabu+"] "+reset+merah+"Utilitas yang dibutuhkan rarfile tidal tersedia. Install sendiri! (unrar)"+reset)
                                    enter = input(kelabu+" ["+banorange+"DONWLOAD"+reset+kelabu+"]"+putih+" Enter untuk masuk ke halaman unduhan"+reset);sys.exit()
            if algort2.lower() == "n" or algort2.lower() == "N":
                with rarfile.RarFile(r) as z:
                    for lenght in range(1, int(algoritma.total) + 1):
                        while True:
                            try:
                                pas = ''.join(random.choices(algoritma.abjad, k=int(algoritma.total)))
                                print(kelabu+"\r ["+banhijau+"#"+reset+kelabu+"]"+orange+" Wordlist yang dibuat: "+reset+banhijau+str(pas)+reset, end='', flush=True)
                                z.extractall('hasil', pwd=pas.encode("utf-8"))
                                hasil(pas, r, algort2)
                            except (EOFError, KeyboardInterrupt): print(kelabu+'\n ['+banmerah+'!'+reset+kelabu+'] '+merah+' Dibatalkan!'+reset)
                            except (RuntimeError, rarfile.BadRarFile, rarfile.PasswordRequired): continue
                            except rarfile.RarCannotExec: 
                                print(kelabu+" ["+banmerah+"!"+reset+kelabu+"] "+reset+merah+"Utilitas yang dibutuhkan rarfile tidal tersedia. Install sendiri! (unrar)"+reset)
                                enter = input(kelabu+" ["+banorange+"DONWLOAD"+reset+kelabu+"]"+putih+" Enter untuk masuk ke halaman unduhan"+reset);sys.exit()
        #EXECNORMAL
        def rarj():
            algort2 = "n"
            print(kelabu+' ['+banhijau+'*'+reset+kelabu+'] Jumlah kata yang akan dicek:'+hijau, ttl)
            with rarfile.RarFile(r) as rr, open(word, 'rb') as rarf:
                rarf.seek(0)
                for pas in tqdm(rarf, total=ttl, unit='word'):
                    try:
                        rr.extractall('hasil', pwd=pas.rstrip())
                        hasil(pas, r, algort2)
                    except KeyboardInterrupt:
                        print(merah+"\n [!] Dibatalkan!"+reset)
                        sys.exit()
                    except (RuntimeError, rarfile.BadRarFile, rarfile.PasswordRequired): continue
                    except rarfile.RarCannotExec: 
                        print(kelabu+" ["+banmerah+"!"+reset+kelabu+"] "+reset+merah+"Utilitas yang dibutuhkan rarfile tidal tersedia. Install sendiri! (unrar)"+reset)
                        enter = input(kelabu+" ["+banorange+"DONWLOAD"+reset+kelabu+"]"+putih+" Enter untuk masuk ke halaman unduhan"+reset)
                        if enter.lower() == "":
                            import webbrowser
                            webbrower.open("https://www.rarlab.com/rar_add.htm")
                        sys.exit()
    #RAR
        rarfile.UNRAR_TOOL ="unrar"
        os.system("cls||clear")
        print(banner)
        print(kelabu+"\n ["+banorange+"RAR"+reset+kelabu+"] Anda masuk dalam mode ekstraksi RAR"+reset)
        r = input(kelabu+' ['+hijau+'>'+reset+kelabu+'] Masukkan lokasi file RAR anda: '+reset)
        algort = input(putih+" ["+banorange+">"+reset+putih+"] Gunakan algoritma? [y/n]: "+reset)
        if algort.lower() == "y" or algort.lower() == "Y":
            algort2 = input(putih+" ["+banorange+">"+reset+putih+"] Gunakan algoritma tersusun? [y/n]: "+reset)
        else:
            word = input(kelabu+' ['+hijau+'>'+reset+kelabu+'] Masukkan lokasi file wordlist: '+reset)
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
        if algort.lower() == "y" or algort.lower() == "Y":
            rara(algort2)
        else:
            rarj()
    except (KeyboardInterrupt, EOFError): print(merah+'\n [!] CTRL+C Terdeteksi, keluar dari program....'+reset);sys.exit()

def helpp():
    print(banner)
    print(putih+"\n[*] OPTIONS")
    print(orange+"   --rar  "+reset+"Digunakan untuk masuk ke opsi brute force password file rar")
    print(orange+"   --zip  "+reset+"Digunakan untuk masuk ke opsi brute force password file zip")
    print(orange+"   --hh   "+reset+"Digunakan untuk masuk ke opsi TAMPILAN UTAMA INI")
    print(orange+"   --7z   "+reset+"Digunakan untuk masuk ke opsi Brute Force password file 7z")
    print(orange+"   --update    Untuk update script ini")
    print(orange+"   --update-module    Untuk update module pada script ini"+reset)
    print(putih+"\n[*] USAGE")
    print(orange+"   python3 "+sys.argv[0]+" --zip")
    print(orange+"   python3 "+sys.argv[0]+" --rar"+reset)
    print(orange+"   python3 "+sys.argv[0]+" --7z"+reset)
    print(orange+"   python3 "+sys.argv[0]+" --update"+reset)
    print(orange+"   python3 "+sys.argv[0]+" --update-module"+reset)
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
    
menu = optparse.OptionParser()
menu.add_option('--zip', dest="zipp", action='store_true', default=False)
menu.add_option('--rar', dest="rarr", action='store_true', default=False)
menu.add_option('--hh', dest="hh", action='store_true', default=False)
menu.add_option('--7z', dest='szip', action="store_true", default=False)
menu.add_option('--update', dest="update", action='store_true', default=False)
menu.add_option("--update-module", dest="update_module", action="store_true", default=False)

(option, args) = menu.parse_args()
rarr = option.rarr
zipp = option.zipp
hh = option.hh
sz = option.szip
update = option.update
upgort = option.update_module

if upgort:
    try:
        import socket
        import requests
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print(kelabu+" ["+banorange+"UPDATE"+reset+kelabu+"]"+putih+" Checking Update..."+reset);time.sleep(0.2)
        req1 = requests.get("https://raw.githubusercontent.com/Sreetx/Riddles/master/src/Extras/algoritma.py")
        req2 = requests.get("https://raw.githubusercontent.com/Sreetx/Riddles/master/src/Extras/banner.py")
        req3 = requests.get("https://raw.githubusercontent.com/Sreetx/Riddles/refs/heads/master/src/Extras/z_riddles.py")
        req4 = requests.get("https://raw.githubusercontent.com/Sreetx/Riddles/master/src/Extras/color/warna.py")
        req1_str = req1.content.decode("utf-8")
        req2_str = req2.content.decode("utf-8")
        req3_str = req3.content.decode("utf-8")
        req4_str = req4.content.decode("utf-8")
        os.makedirs('Extras', exist_ok=True)
        print(kelabu+"\n ["+banorange+"UPDATE"+reset+kelabu+"]"+putih+" Installing Algoritma..."+reset);time.sleep(0.2)
        with open("Extras/algoritma.py", "w", encoding="utf-8") as a:
            a.write(req1_str)
        print(kelabu+" ["+banorange+"UPDATE"+reset+kelabu+"]"+putih+" Installing banner..."+reset);time.sleep(0.2)
        with open("Extras/banner.py", "w", encoding="utf-8") as b:
            b.write(req2_str)
        print(kelabu+" ["+banorange+"UPDATE"+reset+kelabu+"]"+putih+" Installing 7z-File Brute force"+reset);time.sleep(0.2)
        with open("Extras/sevenzippy.py", "w", encoding="utf-8") as c:
            c.write(req3_str)
        print(kelabu+" ["+banorange+"UPDATE"+reset+kelabu+"]"+putih+" Installing Warna"+reset);time.sleep(0.2)
        with open("Extras/color/warna.py", "w", encoding="utf-8") as d:
            d.write(req4_str)
        print(putih+"\n ["+banhijau+"UPDATE"+reset+putih+"] Update Succed!"+reset);sys.exit()
    except (socket.timeout, socket.gaierror): print(putih+" ["+banmerah+"!"+reset+putih+"] Cek koneksi internet"+reset);sys.exit()
    print(kelabu+" ["+banorange+"UPDATE"+reset+kelabu+"]"+putih+" Succed..."+reset);sys.exit()
elif hh:
    os.system("cls||clear")
    helpp()
elif zipp:
    os.system("cls||clear")
    zips()
elif rarr:
    os.system("cls||clear")
    rars()
elif sz:
    os.system("cls||clear")
    print(banner)
    print(kelabu+"\n ["+banorange+"7-ZIP"+reset+kelabu+"] Anda masuk dalam mode ekstraksi 7-Zip"+reset)
    path = input(kelabu+" ["+hijau+">"+reset+kelabu+"]"+putih+" Masukkan path file 7z: ")
    word = input(kelabu+" ["+hijau+">"+reset+kelabu+"]"+putih+" Masukkan path file wordlist: ")
    path = path.strip()
    word = word.strip()
    with open('Extras/data.py', 'w') as data:
        data.write("""path = '"""+path+"""'
word = '"""+word+"""'""")
    try:
        from Extras import z_riddles
    except ImportError:
        print(kelabu+" ["+orange+"#"+kelabu+"]"+putih+" Module untuk 7z Archive Cracker tidak ditemukan!")
        print(kelabu+" ["+orange+"#"+kelabu+"]"+putih+" Coba ketikan < python3 main.py --update > *tanpa tanda < >");sys.exit()
elif update:
    updates()
else:
    helpp()
