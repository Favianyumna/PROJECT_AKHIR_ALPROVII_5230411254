import sqlite3
conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM HEWAN ")
rows = cursor.fetchall()

print("Data hewan:")
print("===============================================================================================")
print("{:<5} {:<20} {:<15} {:<14} {:<20} {:<20}".format("Id", "Nama_hewan", "Jenis", "Asal", "Jumlah_sekarang", "Tahun_ditemukan"))
print("===============================================================================================")
for row in rows:
    print("{:<5} {:<20} {:<15} {:<20} {:<21} {:<10}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
 
conn.close()