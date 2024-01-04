import sqlite3
conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()

Jenis_hewan = 'Mamalia' 
cursor.execute(f"DELETE FROM HEWAN WHERE Jenis = ?", (Jenis_hewan,))
conn.commit()
if cursor.rowcount > 0:
    print(f"Data HEWAN dengan Jenis_hewan {Jenis_hewan} berhasil dihapus.")
else:
    print(f"Tidak ada data hewan dengan Jenis_hewan {Jenis_hewan}.")

conn.close()