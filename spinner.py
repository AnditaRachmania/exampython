
# return function dengan 1 argumen yang dapat memutar list angka
# >> putaran 1x counter clockwise

list_awal = [[1,2,3],[4,5,6],[7,8,9]]

# 1:
# [[3,6,9],
# [2,5,8],
# [1,4,7]]


def counterclokwise(x):
    # if x == '1':
    z = ''
    for i in range(3, 0, -1):   # list baris setelah diputar balik jarum jam
        for j in range(0, 9, 3): # list kolom setelah diputar balik jarum jam
            z += str(i + j) + ' '
        z += '\n'

    print(z)

print("List Awal: ")
print(f'''[[1,2,3],
[4,5,6],
[7,8,9]]''')
print()

print("Setelah dirotasi 1x counterclockwise: ")
counterclokwise(1)

# belum bisa hasil dimasukkan dalam bentuk list

