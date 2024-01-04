import sqlite3
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()
Nama_hewan = 'B%'  
kursor.execute(f"SELECT * FROM HEWAN WHERE Nama_hewan LIKE ?", (Nama_hewan,))
baris_table = kursor.fetchall()

print("Data hewan:")
print("===============================================================================================")
print("{:<5} {:<20} {:<15} {:<10} {:<18} {:<10}".format("Id", "Nama_hewan", "Jenis", "Asal", "Jumlah_sekarang", "Tahun_ditemukan"))
print("===============================================================================================")
for baris in baris_table:
    print("{:<5} {:<20} {:<15} {:<15} {:<15} {:<10}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

koneksi.close()