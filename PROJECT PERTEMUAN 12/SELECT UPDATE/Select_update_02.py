import sqlite3
conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()
cursor.execute(f"UPDATE HEWAN SET Nama_hewan = 'Komodo', Asal = 'Nusa Tenggara Timur' WHERE Id= 3")
conn.commit()
if cursor.rowcount > 0:
    print(f"Data Komodo berhasil diupdate.")
else:
    print(f"Tidak ada data Komodo.")

conn.close()