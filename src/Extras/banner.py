# banner.py
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
    import sys, os
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
banner = borange+"""
>==========================================================<
 | """+reset+putih+"""           Riddles - Archive File Cracker!!      """+borange+"""      |
<+========================================================+>
 |"""+reset+hijau+""" Creator:   """+putih+""" Sreetx  """+borange+"""                                   |
 |"""+reset+hijau+""" Language:  """+putih+""" Python3  """+borange+"""                                  |
 |"""+reset+hijau+""" Version:   """+putih+""" 1.5.13  """+borange+"""                                   |
 |"""+reset+hijau+""" Github:   """+putih+"""  https://github.com/Sreetx   """+borange+"""               |
 |"""+reset+hijau+""" YouTube: """+putih+"""   https://www.youtube.com/@linggachannel4781 """+borange+"""|
 >========================================================<"""+reset+bputih+"""

 [*] File wordlist bawaan ada di folder "word" di folder script ini!
 [*] Gunakan Algorithm untuk membuat file wordlist lu sendiri. Cek di Github gw!"""+reset
