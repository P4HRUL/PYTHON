import calendar

bulan = int(input("Masukkan bulan (1-12) : "))
tahun = int(input("Masukkan tahun : "))

print(calendar.month(tahun, bulan))