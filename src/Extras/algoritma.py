
from Extras.color.warna import kelabu
from Extras.color.warna import banorange
from Extras.color.warna import reset
from Extras.color.warna import banhijau
from Extras.color.warna import borange

import random, os, sys

print(kelabu+"""["""+banorange+"""SELECT"""+reset+kelabu+"""] Pilih salah satu!"""+borange+"""
    (1) Gunakan huruf saja
    (2) Gunakan angka saja
    (3) Gunakan angka dan huruf saja
    (4) Gunakan semua termasuk simbol"""+reset)
number = input(kelabu+" ["+banhijau+"?"+reset+kelabu+"] Pilih salah satu?: "+reset)
total = input(kelabu+" ["+banhijau+"?"+reset+kelabu+"] Jumlah kata Wordlist yang akan digunakan: "+reset)

if number.lower() == "4":
    abjad = '''abcdefghijklmnopqrstuvwxyz1234567890@#$_&-+()/*"':;!?~`|•√π÷×¶∆\}{=°^¥€¢£%©®™✓[]"'''
if number.lower() == "1":
    abjad = "abcdefghijklmnopqrstuvwxyz"
if number.lower() == "2":
    abjad = "1234567890"
if number.lower() == "3":
    abjad = "abcdefghijklmnopqrstuvwxyz1234567890"

    
