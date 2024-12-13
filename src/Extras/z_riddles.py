try:
    import sys, os, time, random, zlib, itertools, socket
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
#Depedensi
try:
    import py7zr
    from tqdm import tqdm
    import lzma
    import datetime
except ImportError:
    print(kelabu+" ["+banmerah+"!"+reset+kelabu+"]"+borangekelip+" Library yg dibutuhkan tidak lengkap!"+reset)
    print(kelabu+" ["+banmerah+"!"+reset+kelabu+"]"+borange+" Library akan segera diinstall"+reset)
    if sys.platform in ['linux', 'linux2']:
        os.system('apt install python3-py7zr')
        os.system('apt install tqdm')
        enter = input(putih+"["+orange+"CTRL+C(close)"+putih+"] Kalo di repo apt lu gk ada kita pakek pip. Enter untuk lanjut installasi pake pip")
        if enter.lower() == '':
            os.system('apt update')
            os.system('apt install pip')
            os.system('pip install tqdm py7zr')
            print(putih+" ["+hijau+"#"+putih+"] Kalo pip lu bermasalah, harap aktifkan venv dan mulai ulang tools!")
            print(putih+" ["+hijau+"*"+putih+"] Restart tools nya!");sys.exit()
    if sys.paltform in ['win32']:
        os.system('pip install tqdm py7zr')
        print(putih+" ["+hijau+"*"+putih+"] Restart tools nya!");sys.exit()

script_path = os.path.abspath(__file__)

def hasil(p, algort2, path, word):
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
# 7-Zip File: """+path.split("/")[-1]+"""
# 7-Zip Encryption Type: AES
# Directory: """+path+"""
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
 |"""+reset+""" 7-Zip File: """+hijau+path.split("/")[-1]+reset+borange+"""
 |"""+reset+""" 7-Zip Directory: """+hijau+path+borange+"""
 |"""+reset+""" 7-Zip Encryption Type: """+hijau+"""AES"""+reset)

        if algort2.lower() == "y" or algort2.lower() == "Y":
            print(borange+""" |"""+reset+""" Password: """+banhijau+str(p)+reset)
        else:
            print(borange+""" |"""+reset+""" Password: """+banhijau+p.decode().strip()+reset)
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

try:
    from Extras.data import path
    from Extras.data import word
except ImportError:
    print('Error')
j = len(list(open(word, 'rb')))
print(kelabu + ' [' + banhijau + '*' + reset + kelabu + '] Jumlah kata yang akan dicek:' + hijau, j)
algort2 = "n"

with open(word, 'rb') as wordlist:
    for password in tqdm(wordlist, total=j, unit="word"):
        p = password.strip()  # Hapus karakter whitespace
        try:
            with py7zr.SevenZipFile(path, mode='r', password=p.decode()) as archive:
                archive.extractall(path="hasil")
            hasil(p, algort2, path, word)
        except (py7zr.exceptions.Bad7zFile, lzma.LZMAError): continue
        except KeyboardInterrupt:
            print("[!] Operasi dibatalkan")
            sys.exit()
    print("[-] Password tidak ditemukan dalam wordlist")

