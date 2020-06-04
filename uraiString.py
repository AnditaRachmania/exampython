
# 2 buah return function dengan 1 argumen yang dapat digunakan untuk mengurai dan merajut string
## contoh urai:
# code
# >> CCoCodCode
# C
# Co
# Cod
# Code

# Python
# >> PPyPytPythPythoPython
# P
# Py
# Pyt
# Pyth
# Pytho
# Python

## contoh rajut:
# CCoCodCode >> Code
# PPyPytPythPythoPython >> Python


def urai(n):
    for i in range(0, len(n)):
        for j in range(0, i+1):
            print((n[j]), end='')

def rajut(n):
    potong = n.split(n[0])
    print(f"{n[0]+potong[-1]}")
            

greet = "** Operator Urai dan Rajut Kata **"

awal = True
while awal:
    print('='*len(greet))
    print(greet)
    print('='*len(greet))
    
    print("Pilih Menu: \n1) Urai \n2. Rajut \n3. Keluar")
    print()
    pilih = input("Menu yang dipilih [1 | 2 | 3]: ")
    if pilih == '1':
        kata = input("Masukkan kata: ")
        print()
        print('Hasil uraian kata:')
        urai(kata)
        
        print()
        awal = True
    elif pilih == '2': # rajut
        kata = input("Masukkan kata: ")
        print()
        print('hasil rajutan kata: ')
        rajut(kata)
        awal = True
    elif pilih == '3':
        print('** Terimakasih **')
        awal = False
    else:
        print("Input yang Anda masukkan salah")
        awal = True

