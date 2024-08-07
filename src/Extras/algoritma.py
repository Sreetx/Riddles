# algoritma.py
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

    
