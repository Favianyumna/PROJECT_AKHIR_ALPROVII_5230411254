import sqlite3
koneksi = sqlite3.connect('database_hewan.db')

#INSERT DATA KEDALAM TABEL HEWAN
koneksi.execute("INSERT INTO HEWAN (Nama_hewan, Jenis, Asal, Jumlah_sekarang, Tahun_ditemukan) VALUES ('Orangutan', 'Mamalia', 'Sumatera', 14000, 2021)")
koneksi.execute("INSERT INTO HEWAN (Nama_hewan, Jenis, Asal, Jumlah_sekarang, Tahun_ditemukan) VALUES ('Harimau Sumatera', 'Mamalia', 'Sumatera', 400, 2020)")
koneksi.execute("INSERT INTO HEWAN (Nama_hewan, Jenis, Asal, Jumlah_sekarang, Tahun_ditemukan) VALUES ('Komodo', 'Reptilia', 'Nusa Tenggara', 3000, 2019)")
koneksi.execute("INSERT INTO HEWAN (Nama_hewan, Jenis, Asal, Jumlah_sekarang, Tahun_ditemukan) VALUES ('Anoa', 'Mamalia', 'Sulawesi', 5000, 2022)")
koneksi.execute("INSERT INTO HEWAN (Nama_hewan, Jenis, Asal, Jumlah_sekarang, Tahun_ditemukan) VALUES ('Badak Jawa', 'Mamalia', 'Jawa', 72, 2021)")
koneksi.execute("INSERT INTO HEWAN (Nama_hewan, Jenis, Asal, Jumlah_sekarang, Tahun_ditemukan) VALUES ('Kuskus', 'Mamalia', 'Papua', 50, 2020)")
koneksi.execute("INSERT INTO HEWAN (Nama_hewan, Jenis, Asal, Jumlah_sekarang, Tahun_ditemukan) VALUES ('Trenggiling', 'Mamalia', 'Sumatera', 90, 2022)")
koneksi.execute("INSERT INTO HEWAN (Nama_hewan, Jenis, Asal, Jumlah_sekarang, Tahun_ditemukan) VALUES ('Burung Cendrawasih', 'Burung', 'Papua', 45, 2021)")
koneksi.execute("INSERT INTO HEWAN (Nama_hewan, Jenis, Asal, Jumlah_sekarang, Tahun_ditemukan) VALUES ('Penyu Hijau', 'Reptil', 'NTT', 20, 2022)")
koneksi.execute("INSERT INTO HEWAN (Nama_hewan, Jenis, Asal, Jumlah_sekarang, Tahun_ditemukan) VALUES ('Gajah Sumatera', 'Mamalia', 'Sumatera', 2500, 2023)")
koneksi.commit()

koneksi.close()