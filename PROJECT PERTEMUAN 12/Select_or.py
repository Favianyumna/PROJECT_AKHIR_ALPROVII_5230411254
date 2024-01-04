import sqlite3
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()
kursor.execute(f"SELECT * FROM HEWAN WHERE Asal = 'Sumatera' OR Jumlah_sekarang > '500'")
baris_table = kursor.fetchall()

print("Data hewan:")
print("================================================================================================")
print("{:<5} {:<20} {:<15} {:<16} {:<20} {:<20}".format("Id", "Nama_hewan", "Jenis", "Asal", "Jumlah_sekarang", "Tahun_ditemukan"))
print("================================================================================================")
for baris in baris_table:
    print("{:<5} {:<20} {:<15} {:<20} {:<20} {:<10}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))
    
koneksi.close() 