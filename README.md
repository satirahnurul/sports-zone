tautan PWS : https://satirah-nurul-sportszone.pbp.cs.ui.ac.id/

Tugas 2

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

Tugas 3

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data yang ada pada database server biasanya akan dikirimkan dari server atau backend ke frontend pada tampilan platform. Data delivery tersebut diperlukan agar aplikasi pada projek Django dapat bertukar data dengan format yang dapat dipahami mau dari sisi user ataupun mesin.

Terdapat beberapa tujuan utama penggunaan data delivery ini. Pertama, untuk meningkatkan efisiensi operasional. Data delivery mengefisiensi proses pengiriman data dari server ke client-side. Kedua, menjaga akurasi data yang dikirim. Data delivery akan memastikan data yang sedang dikirimkan akurat sesuai apa yang dibuat di server secara akurat. Ketiga, meningkatkan kepuasaan pengguna platform. Data delivery memungkinkan data terkirim dengan cepat dan akurat, sehingga platform dapat menyediakan pelayanan yang baik dan secara real-time.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Pada saat saya memeriksa data yang ada pada JSON dan XML, penyajian data pada JSON lebih mudah dibaca oleh user karena tampilannya mirip dengan dictionary di python. Sedangkan, XML sedikit lebih kompleks dalam menyajikan datanya. Lalu, dalam sintaksisnya, JSON memerlukan lebih sedikit baris kode sehinggan ukuran filenya lebih kecil daripada XML padahal mereka sama-sama menyajikan data yang sama. Jadi, JSON lebih ringan dan lebih cepat dikirim ke frontend dibanding XML. Lalu, JSON menggunakan standar format untuk pertukaran data di API web modern karena JSON sesuai dengan Java Script dan memudahkan pengembangan web dibanding XML. Penggunaan JSON jauh lebih luas dibanding XML karena JSON dapat digunakan dikebanyakan platform yang memerlukan pertukaran data dengan cepat seperti perangkat IoT dan aplikasi obrolan. Jadi, JSON lebih populer dan lebih baik penggunaannya karena efisiensi dan kecepatannya yang lebih unggul dibanding XML. Namun, XML masih digunakan di beberapa sistem legacy atau jika dibutuhkan fitur tambahan seperti namespace dan skema validasi.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

method is_valid() pada form Django tersebut berfungsi untuk memeriksa semua informasi dalam formulir atau serializer. Jadi, method ini akan memvalidasi apakah semua data formulir sesuai dengan aturan yang ditetapkan contohnya seperti tipe data yang ada di models.py, panjang karakter, atau field yang sesuai di forms.py. Jika ada data yang tidak sesuai dengan aturan atau terdapat kesalahan, method ini akan mengembalikan False.

Pada tugas 3 ini, kita membutuhkan method is_valid() untuk memeriksa kebenaran dan keakuratan dari database yang akan masuk ke frontend. Jadi nanti alurnya, data sebelum dikirim sebagai response, data akan divalidasi, setelah benar, baru akan mengirim permintaan POST.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token adalah suatu token unik yang akan otomatis dibuat oleh  Django untuk setiap sesi user. Token ini nantinya akan digunakan untuk memastikan setiap request yang dikirim melalui form atau data delivery ini benar-benar berasal dari pengguna yang sah melalui aplikasi yang sudah kita buat di projek Django, bukan dari sumber yang tidak jelas atau pun website eksternal lainnya.

Jika kita tidak menambahkan csrf_token dalam proses data delivery ini, resiko terjadinya serangan pada website frontend menjadi lebih tinggi. Biasanya csrf_token ini akan mencegah serangan CSRF (Cross-Site Request Forgery) untuk menyerang website. Serangan CSRF merupakan serangan dimana penyerang akan mencoba membuat pengguna yang sedang login di sebuah aplikasi atau platform otomatis mengirimkan request yang merugikan. Gambarannya itu seperti contoh ketika seorang pengguna sedang login di aplikasi bank, tanpa adanya csrf_token nantinya penyerang bisa membuat website palsu yang tanpa sepengetahuan pengguna, akan mengirimkan request transfer uang dari pengguna itu ke penyerang.

Mekanisme penggunaan csrf_token ini yaitu pada saat user add products, Django akan otomatis masuk ke csrf_token,bisa dilihat di templates create_product ada bagian `{% csrf_token %}`. Setelah user mengisi form dan submit produk, request tersebut membawa token ke server bersama data form. Lalu, akan diperiksa apakah token yang dikirim sama dengan token yang disimpan disaat user tadi mengisi form. Kalo sama, request diproses, jika tidak sama, Django akan error dan menolak request. 

Jadi, csrf_token ini berfungsi sebagai lapisan keamanan ekstra untuk memastikan bahwa hanya request sah dari aplikasi kita yang bisa diproses.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.

Berikut langkah-langkah yang saya lakukan dalam mengimplementasi Tugas 3 ini:
    1. Pertama saya membuat templates di direktori utama untuk membuat base.html yang menjadi base templates pada app main nantinya.
    2. Lalu membuat model, atribut, dan method-method propertynya pada models.py
    3. Setelah itu membuat forms.py untuk membuat struktur form tampilan di paltformnya. Masukkan juga field pada models yang akn ditampilkan.
    4. Lalu pada views.py, buat method yang akan membuat produk nantinya akan ada validasi data, lalu baru membuat produk. Kedua, membuat method show_product untuk mengambil produk dan digunakan nanti pada tempat product_details
    5. Lalu membuat templates, main.html untuk template tampilan form utama, create_product untuk tampilan pada saat menambahkan produk dan product_detail untuk tampilan saat menampilkan detail produk yang sudah ditambahkan.
    6. Lalu disetting untuk konfigurasinya.
    7. Terakhir, membuat 4 fungsi yaitu fungsi untuk melihat data XML dan JSON, serta fungsi yg menampilkan data XML dan JSON berdasarkan id produknya.
    8. Lalu, setting juga path nya di urls supaya web dapat mengakses dan menampilkan data XML dan JSON tersebut.
    9. Di commit dan push ke repository github dan deploy ke repository pws.

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

Sejauh ini sudah sangat membantu kak tiap penjelasan di tutorial. Tiap penjelasan juga bisa dipahami dan dibaca-baca lagi untuk memahami materi lebih lanjut. Selain dari saran aku yang sebelumnya, sudah tidak ada lagi kak.

Berikut ini hasil screenshot dari Postman:
    https://drive.google.com/drive/folders/17UfFkrnKoyjxJH6Ukj0iGXMLd2sVQXdD?usp=sharing
