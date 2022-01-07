import sqlite3

file = sqlite3.connect("kitapliq")
imlec = file.cursor()
menu = """
[1] Kitab ara
[2] Yazra ara 
"""
print(menu)
islem = input("Islem:")
if islem == "1":
    isim = input("Kitab ismi girin:")
    sorgu = "SELECT * FROM kitapliq WHERE kitap = '{}'".format(isim)
    imlec.execute(sorgu)
    veriler = imlec.fetchall()
    for i in veriler:
        print(i)
if islem == "2":
    isim = input("Yazar ismi girin:")
    sorgu = "SELECT * FROM kitapliq WHERE yazar = '{}'".format(isim)
    imlec.execute(sorgu)
    veriler = imlec.fetchall()
    for i in veriler:
        print(i)
file.close()