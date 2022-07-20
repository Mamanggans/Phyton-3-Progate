# latihan 2 mendefinisikan sebuah fungsion

# Definisikan function print_hand 
from inspect import Parameter
from random import randint
from unittest import result


def print_hand():
  print("Anda memilih: Batu")

# Panggil function print_hand 
print_hand()

# latihan 3 argument dan parameter 

# Tambahkan parameter untuk print_hand
def print_hand(hand): # hand adalah sebuah parameter adalah variable yang digunakan untuk sebuah parameter 
    # Gunakan parameter untuk mencetak 'Anda memilih: ___'
    print('Anda memilih: '+ hand)

# Panggil print_hand dengan 'Batu'
print_hand('Batu')

# Panggil print_hand dengan 'Kertas'
print_hand('Kertas')


# latihan 4 dengan banyak prameter 

# Tambahkan parameter ke print_hand

def print_hand(hand,name):
    # Ubah hasil ke '___ memilih: ___'
    print(name + ' memilih: ' + hand)

# Tambahkan argument ke dua ke print_hand
print_hand('Batu','Ninja Ken')

# Tambahkan argument ke dua ke print_hand
print_hand('Kertas','Komputer')


#latihan 5 default Parameter
# Tambahkan nilai default untuk name
def print_hand(hand, name='Tamu'): # name='tamu' adalah default parameter
    print(name + ' memilih: ' + hand)

# Tambahkan argument ke print_hand
print_hand('Batu')



# latihan 6 input name 
def print_hand(hand, name='Tamu'):
    print(name + ' memilih: ' + hand)

print('Memulai Permainan Batu Kertas Gunting!')

# Dapatkan input, dan tetapkan ke variable player_name
player_name = input('Masukkan nama Anda: ')

# Tambahkan argument ke dua ke print_hand
print_hand('Batu',player_name)



#latihan 7 menambahkan dictionary di dalam function 
def print_hand(hand, name='Tamu'):
    # Tetapkan list hands ke variable hands 
    hands =['Batu','Kertas','Gunting']
    
    # Memperbarui dengan menggunakan element dari variable hands 
    print(name + ' memilih: ' + hands[hand])

print('Memulai Permainan Batu Kertas Gunting!')
player_name = input('Masukkan nama Anda: ')
# Cetak 'Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)'
print('Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)')

# Dapatkan input, ubah, dan tetapkan ke variable player_hand 
player_hand = int(input('Masukkan nomor (0-2): ')) # ini cara ngambil imput yang isi nya bakalan jadi noomer 

# Ubah argument pertama ke player_hand
print_hand(player_hand, player_name)


#latihan 8 fungtion dengan nilai return 
# Definisikan function validate 
def validate (hand):
    # Tambahkan control flow berdasarkan nilai hand
    if hand < 0 or hand > 2:
      return False
    else:
      return True

def print_hand(hand, name='Tamu'):
    hands = ['Batu', 'Kertas', 'Gunting']
    print(name + ' memilih: ' + hands[hand])

print('Memulai permainan Batu Kertas Gunting!')
player_name = input('Masukkan nama Anda: ')

print('Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)')
player_hand = int(input('masukkan nomor (0-2): '))

# Tambahkan control flow berdasarkan nilai return dari function validate 
if validate(player_hand): # fungsi dulu baru variabel di dalam tanda kurung 
  player_hand == True
  print_hand
else:
  print('Mohon masukkan nomor yang benar')
  
print_hand(player_hand, player_name)


#latihan 9 simpler code cus 
def validate(hand):
    if hand < 0 or hand > 2:
        return False
    # Hapus else dan perbaiki indentasi
        return True

def print_hand(hand, name='Tamu'):
    hands = ['Batu', 'Kertas', 'Gunting']
    print(name + ' memilih: ' + hands[hand])

print('Memulai permainan Batu Kertas Gunting!')
player_name = input('Masukkan nama Anda: ')

print('Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)')
player_hand = int(input('Masukkan nomor (0-2): '))

if validate(player_hand):
    print_hand(player_hand, player_name)
else:
    print('Mohon masukkan nomor yang benar')


#latihan 10 lets start with game 
#latihan 10 lets start with game 
def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def print_hand(hand, name='Tamu'):
    hands = ['Batu', 'Kertas', 'Gunting']
    print(name + ' memilih: ' + hands[hand])

print('Memulai permainan Batu Kertas Gunting!')
player_name = input('Masukkan nama Anda: ')

print('Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)')
player_hand = int(input('Masukkan nomor (0-2): '))

if validate(player_hand):
    # Tetapkan 1 ke variable computer_hand 
    computer_hand = 1 
    
    print_hand(player_hand, player_name)
    # Panggil function print_hand dengan computer_hand dan 'Komputer' sebagai argument
    print_hand(computer_hand,'Komputer') # doi mengupdate fungsi diatas (fungsi print_hand) 
    
    
else:
    print('Mohon masukkan nomor yang benar')


#latihan 11 
def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def print_hand(hand, name='Tamu'):
    hands = ['Batu', 'Kertas', 'Gunting']
    print(name + ' memilih: ' + hands[hand])

# Definisikan function judge 
def judge(player,computer):
# Tambahkan control flow berdasarkan perbandingan antara player dan computer
  if player == computer:
    return 'Seri'
  elif player == 0 and computer == 1:
    return 'Kalah'
  elif player == 1 and computer == 2:
    return 'Kalah'
  elif player == 2 and computer == 0:
    return 'Kalah'
  else:
    return 'Menang'

print('Memulai permainan Batu Kertas Gunting!')
player_name = input('Masukkan nama Anda: ')

print('Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)')
player_hand = int(input('Masukkan nomor (0-2): '))

if validate(player_hand):
    computer_hand = 1
    
    print_hand(player_hand, player_name)
    print_hand(computer_hand, 'Komputer')
    
    # Tetapkan nilai return dari judge ke variable result 
    result = judge (player_hand,computer_hand)
    print('Hasil:'+result)
    # Cetak variable result 
else:
    print('Mohon masukkan nomor yang benar')


#latihan 12 pisah 2 file 

#file script.py
# import module utils
import utils
print('Memulai permainan Batu Kertas Gunting!')
player_name = input('Masukkan nama Anda: ')

print('Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)')
player_hand = int(input('Masukkan nomor (0-2): '))

# Panggil function validate milik module utils
if utils.validate(player_hand):
    computer_hand = 1
    
    # Panggil function print_hand milik module utils 
    utils.print_hand(player_hand, player_name)
    utils.print_hand(computer_hand, 'Komputer')
    
    # Panggil function judge milik module utils 
    result = utils.judge(player_hand, computer_hand)
    print('Hasil: ' + result)
else:
    print('Mohon masukkan nomor yang benar')

# file utils
def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def print_hand(hand, name='Tamu'):
    hands = ['Batu', 'Kertas', 'Gunting']
    print(name + ' memilih: ' + hands[hand])

def judge(player, computer):
    if player == computer:
        return 'Seri'
    elif player == 0 and computer == 1:
        return 'Kalah'
    elif player == 1 and computer == 2:
        return 'Kalah'
    elif player == 2 and computer == 0:
        return 'Kalah'
    else:
        return 'Menang'


#latihan 13 randint adalah fungsi yang berfungsi untuk mengajak suatu variable
#file script.py
import utils
# import module random
import random

print('Memulai permainan Batu Kertas Gunting!')
player_name = input('Masukkan nama Anda: ')

print('Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)')
player_hand = int(input('Masukkan nomor (0-2): '))

if utils.validate(player_hand):
    # Tetapkan nomor acak antara 0 dan 2 ke computer_hand menggunakan randint
    computer_hand = random.randint(0,2)
    
    utils.print_hand(player_hand, player_name)
    utils.print_hand(computer_hand, 'Komputer')

    result = utils.judge(player_hand, computer_hand)
    print('Hasil: ' + result)
else:
    print('Mohon masukkan nomor yang benar')

# file utils
def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def print_hand(hand, name='Tamu'):
    hands = ['Batu', 'Kertas', 'Gunting']
    print(name + ' memilih: ' + hands[hand])

def judge(player, computer):
    if player == computer:
        return 'Seri'
    elif player == 0 and computer == 1:
        return 'Kalah'
    elif player == 1 and computer == 2:
        return 'Kalah'
    elif player == 2 and computer == 0:
        return 'Kalah'
    else:
        return 'Menang'
