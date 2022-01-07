import sqlite3
veriler = [
    ("fagan salmanov","sql lite"),
    ("bextiyyar vahabzade","ana"),
    ("celil memmmedquluzade","buz")]
file = sqlite3.connect("kitapliq")
imlec = file.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS kitapliq (yazar,kitap)")
for i in veriler:
    imlec.execute("INSERT INTO kitapliq VALUES (?,?)",i)
file.commit()
file.close()