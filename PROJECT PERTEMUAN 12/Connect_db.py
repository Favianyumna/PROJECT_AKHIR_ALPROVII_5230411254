# Koneksi 
import sqlite3
koneksi = sqlite3.connect('database_hewan.db')
# DATABASE HEWAN
koneksi.execute('''
                 CREATE TABLE HEWAN(
                 Id INTEGER PRIMARY KEY AUTOINCREMENT,
                 Nama_hewan VARCHAR(50),
                 Jenis VARCHAR(50),
                 Asal VARCHAR(50),
                 Jumlah_sekarang INTEGER(10),
                 Tahun_ditemukan INTEGER(10)
                )
                ''')

koneksi.close()  