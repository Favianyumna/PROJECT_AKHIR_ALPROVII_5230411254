import sqlite3
conn = sqlite3.connect('database_hewan.db')

cursor = conn.cursor()
cursor.execute("SELECT SUM(Jumlah_sekarang) FROM HEWAN")
total_Jumlah_sekarang = cursor.fetchone()[0]
print(f"Total Jumlah_sekarang: {total_Jumlah_sekarang}")

conn.close()