tautan PWS : https://satirah-nurul-sportszone.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Aktifkan environment
- Membuat proyek baru, repositori baru di git, dan mendeploy pws 
- Lalu membuat aplikasi di direktori yang sama, dan menambahkan applikasi di settings.py
- Lalu membuat template HTML untuk tampilan aplikasi
- Lalu membuat models.py yang berisikan atribut data-data yang diperlukan aplikasi, ataupun method-method yang akan berlaku di aplikasi. Dan lakukan migrasi model agar data dapat diaplikasikan.
- Lalu membuat views.py yang akan menampilkan apa yg ada di template pada pengguna. Intinya disini akan diatur saat ada request dari user, request dikirim ke template dan ditampilkan ke pengguna.
- Terakhir, menkonfigurasikan routing url proyek dengan tujuan untuk melakukan pemetaan ke rute URL pada aplikasi sehingga link URL bisa mengarah ke tampilan aplikasi.
- Di push ke git dan pws

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Request -> urls -> View -> Model -> View -> Template -> Response

Penjelasan :
saat user search link pattern, request akan dikirim ke django server dan masuk ke urls.py, lalu di urls akan mengarah ke show_main di views.py. Pada views.py, logika request-an di handle dan akan memanggil model, mempersiapkan data (context), dan mengatur template mana yang akan dirender untuk ditampilkan. Pada proses sebelum dan sesudah views juga terjadi konfigurasi pada settings.py yg memproses request. Lalu views ke models, disini dibuat dan disiapkan data yang akan dikirim ke views untuk mempersiapkan context. Lalu views akan ke template untuk merender tampilan yang ada di template HTML. Terakhir, akan dihasilkan HTML final yang akan dikirim ke client-side sebagai response.

3. Jelaskan peran settings.py dalam proyek Django!
= Pada proyek Django untuk menambahkan aplikasi, diperlukan untuk menambahkan nama aplikasi di berkas settings.py, settings.py ini merupakan file konfigurasi utama yg mengatur fungsi-fungsi pada proyek Django contohnya mengatur aplikasi apa aja yg berjalan atau aktif.

4. Bagaimana cara kerja migrasi database di Django?
= Migrasi model ini bertujuan untuk melacak tiap perubahan pada model proyek Django. Pertama, buat migrasi model dengan perintah makemigrations untuk menbuat berkas migrasi yang berisi perubahan model yg blm diaplikasikan ke basis data. Kedua, aplikasikan migrasi ke basis data lokal dengan perintah migrate.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
= Dikarenakan proses pengembangannya yang terbilang lebih mudah karena bahasa pemrogramannya menggunakan python, lalu juga sudah ada fitur yang siap-pakai dalam pengembangannya. Lalu juga dalam hal keamanan, Django memiliki fitur keamanan yang terintegrasi dan terkini. Skala proyek yang dikerjakan juga besar, karena banyak proyek yg bisa dibuat dengan Django.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
= Kalau boleh memberikan saran, tiap step di tutorial semoga bisa memberikan contoh berupa screenshot dari pengaplikasian caranya