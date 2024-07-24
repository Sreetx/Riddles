try:
    import sys, os, time
    from banner import banner
    from color.warna import orange
    from color.warna import putih
    from color.warna import merah
    from color.warna import hijau
    from color.warna import biru
    from color.warna import borange
    from color.warna import bputih
    from color.warna import bhijau
    from color.warna import bbiru
    from color.warna import bmerah
    from color.warna import kelabu
    from color.warna import borangekelip
    from color.warna import banmerah
    from color.warna import banhijau
    from color.warna import banorange
    from color.warna import reset
except ImportError:
    print(' [!] Harap install ulang script ini dari repository github kami!');sys.exit()
try:
    import py7zr
except ImportError: print(" [!] Module tidak lengkap!. Unduh module py7z sendiri");sys.exit()

def Sxc():
    try:
        def hasil(pas, files, word):
            hpst = socket.gethostname()
            date = datetime.datetime.now()
            timestamp = date.strftime("%Y%m%d_%H%M%S")
            logs = f"logs/succed_{timestamp}.txt"
            filed = """#LOG FILE
#PASSWORD FOUND

# MODE: ZIP Brute Force
# Time: """+timestamp+"""
# 7Zip File: """+files.split("/")[-1]+"""
# Directory: """+files+"""
# Password: """+pas.decode().strip()+"""
# Device Model: """+hpst+"""

#################################
# Support Me!! IN YOUTUBE
"""
            print(reset+borange+"""
<=======================================>
 |"""+reset+putih+"""             Password Found    """+borange+"""       |
 >======================================<
 |"""+reset+""" 7Zip File: """+hijau+files.split("/")[-1]+reset+borange+"""
 |"""+reset+""" 7Zip Directory: """+hijau+files+borange+"""
 |"""+reset+""" Password: """, banhijau+pas+reset+borange+"""
 |"""+reset+""" Wordlist Directory: """+hijau+tebak+borange+"""
 |"""+reset+""" Log: """+hijau+"""~/logs/succed_"""+timestamp+reset+borange+"""
 |"""+reset+""" System: """+hijau+hpst+borange+"""
<=======================================>"""+reset+orange+"""
 [*] File sudah di ekstraksi dan disimpan di forder "hasil" di script ini
 [*] Terima Kasih karena telah menggunakan script ini"""+reset)
            bite = filed.encode('utf-8')
            with open(logs, 'wb') as fd:
                fd.write(bite)
            sys.exit()
            os.system("cls||clear")
            
    #7Zip
        os.system("cls||clear")
        print(banner)
        print(putih+" ["+banorange+"#"+reset+putih+"]"+merah+" 7-Zip file cracker BETA!! (fitur nya masih belum jelas!)"+reset)
        print(kelabu+"\n ["+banorange+"7Zip"+reset+kelabu+"] Anda masuk dalam mode ekstraksi 7Zip"+reset)
        files = input(kelabu+' ['+banhijau+'?'+reset+kelabu+'] Masukkan lokasi file 7Zip anda: '+reset)
        word = input(kelabu+' ['+banhijau+'?'+reset+kelabu+'] Masukkan lokasi file wordlist: '+reset)
        try:
            total = len(list(open(word, "rb")))
        except FileNotFoundError:
            print(borange+' ['+reset+banmerah+'!'+reset+borange+'] '+merah+' Perhatikan penulisan path wordlist'+reset);sys.exit()
            
        print(putih+' \n['+banorange+'INFO'+reset+putih+'] '+orange+'Jika proses penebakan berhenti, itu artinya script menemukan kata yang tepat dan script mencoba untuk mengekstrak file tersebut'+reset)
        print(putih+'['+banorange+'INFO'+reset+putih+'] '+orange+'Ekstraksi akan segera dilakukan setelah password ditemukan\n'+reset)
        
    #7ZIP HASH
        try:
            with open(files, 'rb') as sz, open(wordlist, 'rb') as passz:
                passz.seek(0)
                for pas in tqdm(passz, total=total, unit='word'):
                    pas = passz.rstrip()
                    try:
                        pas.extractall('hasil', password=pas)
                        hasil(pas, files, word)
                    except KeyboardInterrupt:
                        print(merah + "\n [!] Dibatalkan!" + reset)
                        sys.exit()
                    except (RuntimeError, py7zr.Bad7zFile, py7zr.PasswordRequired, py7zr.PasswordError):
                        continue
            print("Wordlist Habis")
        except py7zr.Bad7zFile:
            print(borange+'\n ['+reset+banmerah+'!'+reset+borange+'] '+merah+'Terdeteksi bukan file RAR atau anda salah memasukkan path. Koreksi penulisan path!'+reset);sys.exit()
    except (KeyboardInterrupt, EOFError): print(merah+'\n [!] CTRL+C Terdeteksi, keluar dari program....'+reset);sys.exit()