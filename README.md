# Nama Proyek

Tebak Warna UDP

## Deskripsi

Proyek ini adalah server sederhana yang menggunakan UDP (User Datagram Protocol) untuk berkomunikasi dengan klien. Server ini mengimplementasikan permainan di mana klien harus menebak warna yang dipilih secara acak oleh server.

## Cara Kerja Server.py

1. **Inisialisasi Soket Server**: Program membuat soket UDP dan mengikatnya ke alamat dan port tertentu.
2. **Fungsi `handle_game`**: Menangani setiap koneksi dari klien. Mulai dari mengirim pesan selamat datang hingga memberikan poin berdasarkan jawaban yang diberikan klien.
3. **Fungsi `accept_connections`**: Menerima koneksi dari klien dan memulai permainan ketika jumlah klien mencapai batas maksimum.
4. **Input Jumlah Maksimal Koneksi**: Pengguna diminta untuk memasukkan jumlah maksimal koneksi yang diinginkan.
5. **Inisialisasi Objek Warna**: Objek warna dibuat untuk setiap warna yang mungkin dengan metode untuk mengembalikan warna, jawaban yang benar, dan memberikan poin berdasarkan jawaban yang diberikan.
6. **Mulai Menerima Koneksi**: Program mulai menerima koneksi dari klien dan memulai permainan saat jumlah klien terhubung mencapai batas maksimum.
7. **Thread untuk Setiap Klien**: Untuk setiap klien yang terhubung, server membuat thread baru yang menjalankan fungsi `handle_game`.
8. **Penutupan Soket**: Setelah semua permainan selesai, soket server ditutup.

## Cara Kerja Client.py
1. **Inisialisasi Soket UDP**: Script ini membuat soket UDP dan mengirimkan kode koneksi ke server.

2. **Menerima Respons dari Server**: Menerima respons awal dari server dan melakukan print.

3. **Menerima Informasi Awal**: Klien menerima dan mencetak pesan awal dari server terkait dengan permainan.

4. **Menerima Informasi Warna**: Klien menerima informasi tentang warna saat ini dan mencetaknya.

5. **Memulai Thread Input**: Sebuah thread terpisah dimulai untuk menunggu masukan dari pengguna.

6. **Menunggu Masukan atau Timeout**: Klien menunggu pengguna untuk memberikan masukan atau hingga timeout terjadi.

7. **Penanganan Timeout**: Jika timeout terjadi sebelum pengguna memberikan masukan, klien mengirim sinyal TIMEOUT ke server.

8. **Memeriksa Hasil dari Server**: Klien menerima hasil dari server dan mencetaknya.

9. **Penyelesaian Program**: Setelah menerima hasil dari server, klien menutup soket dan keluar.


## Penggunaan

1. Jalankan program server terlebih dahulu.
2. Jalankan program klien setelah server berjalan.
3. Ikuti instruksi pada program klien untuk berpartisipasi dalam permainan.
