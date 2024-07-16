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
        import sys, os, time
        from color.warna import orange
        from color.warna import putih
        from color.warna import merah
        from color.warna import hijau
        from color.warna import biru
        from color.warna import borange
        from color.warna import bputih
        from color.warna import bhijau
        from color.warna import bbiru
        from  color.warna import bmerah
        from color.warna import kelabu
        from color.warna import borangekelip
        from color.warna import banmerah
        from color.warna import banhijau
        from color.warna import banorange
        from color.warna import reset
    except ImportError:
        print(' [!] Harap install ulang script ini dari repository github kami!');sys.exit()
    os.system('mkdir hasil')
    os.system('mkdir logs')
    os.system('cls || clear')
    try:
        import zipfile
        from tqdm import tqdm
        import datetime
        import socket
    except ImportError:
        print(putih+' ['+banmerah+'!'+reset+putih+']'+borangekelip+' Module tidak lengkap'+reset)
        print(putih+' ['+banmerah+'!'+reset+putih+']'+reset+orange+' Module akan segera diinstall'+reset);time.sleep(1)
        if sys.platform in ['win32', 'win64']:
            os.system('pip install zipfile')
            os.system('pip install tqdm')
            sys.exit()
        if sys.platform in ['linux', 'linux2']:
            os.system('pip install zipfile')
            os.system('pip install tqdm')
            enter = input(borange+' [*] Jika modul terpasang dengan baik tekan CTR+C, mulai Ulang script'+reset)
            os.system('apt install python3-zipfile')
            os.system('apt install python3-tqdm')
            sys.exit()
        else: pass
except KeyboardInterrupt: print(bputih+' ['+banmerah+'!'+reset+bputih+']'+reset+merah+' Canceled by USER!'+reset);sys.exit()

try:
    banner = borange+"""
>==========================================================<
 | """+reset+putih+"""            Riddles - Zip File Cracker!!      """+borange+"""         |
<+========================================================+>
 |"""+reset+hijau+""" Creator:   """+putih+""" Sreetx  """+borange+"""                                   |
 |"""+reset+hijau+""" Language:  """+putih+""" Python3  """+borange+"""                                  |
 |"""+reset+hijau+""" Version:   """+putih+""" 0.0.2  """+borange+"""                                    |
 |"""+reset+hijau+""" Github:   """+putih+"""  https://github.com/Sreetx   """+borange+"""               |
 |"""+reset+hijau+""" YouTube: """+putih+"""   https://www.youtube.com/@linggachannel4781 """+borange+"""|
 >========================================================<"""+reset
    print(banner)
    f = input(kelabu+'\n ['+banhijau+'?'+reset+kelabu+'] Masukkan lokasi file zip anda: '+reset)
    tebak = input(kelabu+' ['+banhijau+'?'+reset+kelabu+'] Masukkan lokasi file wordlist anda: '+reset)
    print(putih+' \n['+banorange+'INFO'+reset+putih+'] '+orange+'Jika proses penebakan berhenti, itu artinya script menemukan kata yang tepat dan script mencoba untuk mengekstrak file tersebut'+reset)
    print(putih+'['+banorange+'INFO'+reset+putih+'] '+orange+'Ekstraksi akan segera dilakukan setelah password ditemukan\n'+reset)
    def hasil(p):
        hpst = socket.gethostname()
        date = datetime.datetime.now()
        timestamp = date.strftime("%Y%m%d_%H%M%S")
        logs = f"logs/succed_{timestamp}.txt"
        filed = """#LOG FILE
#PASSWORD FOUND

# Time: """+timestamp+"""
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
 |"""+reset+""" Log: """+hijau+"""~/log/succed_"""+timestamp+reset+borange+"""
 |"""+reset+""" System: """+hijau+hpst+borange+"""
<=======================================>"""+reset+orange+"""
 [*] File sudah di ekstraksi dan disimpan di forder "hasil" di script ini
 [*] Terima Kasih karena telah menggunakan script ini"""+reset)
        bite = filed.encode('utf-8')
        with open(logs, 'wb') as fd:
            fd.write(bite)
        sys.exit()
# HASH
    try:
        param = zipfile.ZipFile(f)
    except (FileNotFoundError, zipfile.BadZipFile):  print(borange+' ['+reset+banmerah+'!'+reset+borange+'] '+merah+'Terdeteksi bukan file zip atau anda salah memasukkan path. Koreksi penulisan path'+reset);sys.exit()
    if tebak is None:
        print(borange+' ['+reset+banmerah+'!'+reset+borange+'] '+merah+' Perhatikan penulisan path wordlist'+reset);sys.exit()
    j = len(list(open(tebak, 'rb')))
    print(kelabu+' ['+banhijau+'*'+reset+kelabu+'] Jumlah kata yang akan dicek:'+hijau, j)
    with zipfile.ZipFile(f) as z, open(tebak, 'rb') as p:
        for p in tqdm(p, total=j, unit='word'):
            try:
                z.extractall('hasil',pwd=p.strip())
                hasil(p)
            except KeyboardInterrupt: print(kelabu+' ['+banmerah+'!'+reset+kelabu+'] '+merah+' Dibatalkan!'+reset);sys.exit()
            except (RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile): continue
            else:
               print('Wordlist Habis')
except (KeyboardInterrupt, EOFError): print(merah+'\n [!] CTRL+C Terdeteksi, keluar dari program....'+reset);sys.exit()
                
