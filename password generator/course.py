import os, random
os.system("clear")

def password(length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$&*!?£¢€¥^%'
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password

print("buat kata sandi sepanjang 6 karakter.")
length = int(input("jumlah karakter : "))
print("\nhasil : ", password(length))
print("\nselesai...")
print("silahkan copy password anda !")

password(length)