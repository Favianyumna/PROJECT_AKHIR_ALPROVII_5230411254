import sqlite3
conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()
cursor.execute(f"UPDATE HEWAN SET Nama_hewan = 'Orangutan', Jumlah_sekarang='900' WHERE Id= 1")
conn.commit()
if cursor.rowcount > 0:
    print(f"Data Orangutan berhasil diupdate.")
else:
    print(f"Tidak ada data Orangutan.")

conn.close()