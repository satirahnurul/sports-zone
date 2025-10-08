# tautan PWS : https://satirah-nurul-sportszone.pbp.cs.ui.ac.id/

## Tugas 2

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Aktifkan environment
- Membuat proyek baru, repositori baru di git, dan mendeploy pws 
- Lalu membuat aplikasi di direktori yang sama, dan menambahkan applikasi di settings.py
- Lalu membuat template HTML untuk tampilan aplikasi
- Lalu membuat models.py yang berisikan atribut data-data yang diperlukan aplikasi, ataupun method-method yang akan berlaku di aplikasi. Dan lakukan migrasi model agar data dapat diaplikasikan.
- Lalu membuat views.py yang akan menampilkan apa yg ada di template pada pengguna. Intinya disini akan diatur saat ada request dari user, request dikirim ke template dan ditampilkan ke pengguna.
- Terakhir, menkonfigurasikan routing url proyek dengan tujuan untuk melakukan pemetaan ke rute URL pada aplikasi sehingga link URL bisa mengarah ke tampilan aplikasi.
- Di push ke git dan pws

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Request -> urls -> View -> Model -> View -> Template -> Response

Penjelasan :
saat user search link pattern, request akan dikirim ke django server dan masuk ke urls.py, lalu di urls akan mengarah ke show_main di views.py. Pada views.py, logika request-an di handle dan akan memanggil model, mempersiapkan data (context), dan mengatur template mana yang akan dirender untuk ditampilkan. Pada proses sebelum dan sesudah views juga terjadi konfigurasi pada settings.py yg memproses request. Lalu views ke models, disini dibuat dan disiapkan data yang akan dikirim ke views untuk mempersiapkan context. Lalu views akan ke template untuk merender tampilan yang ada di template HTML. Terakhir, akan dihasilkan HTML final yang akan dikirim ke client-side sebagai response.

### 3. Jelaskan peran settings.py dalam proyek Django!
= Pada proyek Django untuk menambahkan aplikasi, diperlukan untuk menambahkan nama aplikasi di berkas settings.py, settings.py ini merupakan file konfigurasi utama yg mengatur fungsi-fungsi pada proyek Django contohnya mengatur aplikasi apa aja yg berjalan atau aktif.

### 4. Bagaimana cara kerja migrasi database di Django?
= Migrasi model ini bertujuan untuk melacak tiap perubahan pada model proyek Django. Pertama, buat migrasi model dengan perintah makemigrations untuk menbuat berkas migrasi yang berisi perubahan model yg blm diaplikasikan ke basis data. Kedua, aplikasikan migrasi ke basis data lokal dengan perintah migrate.

### 5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
= Dikarenakan proses pengembangannya yang terbilang lebih mudah karena bahasa pemrogramannya menggunakan python, lalu juga sudah ada fitur yang siap-pakai dalam pengembangannya. Lalu juga dalam hal keamanan, Django memiliki fitur keamanan yang terintegrasi dan terkini. Skala proyek yang dikerjakan juga besar, karena banyak proyek yg bisa dibuat dengan Django.

### 6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
= Kalau boleh memberikan saran, tiap step di tutorial semoga bisa memberikan contoh berupa screenshot dari pengaplikasian caranya

## Tugas 3

### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data yang ada pada database server biasanya akan dikirimkan dari server atau backend ke frontend pada tampilan platform. Data delivery tersebut diperlukan agar aplikasi pada projek Django dapat bertukar data dengan format yang dapat dipahami mau dari sisi user ataupun mesin.

Terdapat beberapa tujuan utama penggunaan data delivery ini. Pertama, untuk meningkatkan efisiensi operasional. Data delivery mengefisiensi proses pengiriman data dari server ke client-side. Kedua, menjaga akurasi data yang dikirim. Data delivery akan memastikan data yang sedang dikirimkan akurat sesuai apa yang dibuat di server secara akurat. Ketiga, meningkatkan kepuasaan pengguna platform. Data delivery memungkinkan data terkirim dengan cepat dan akurat, sehingga platform dapat menyediakan pelayanan yang baik dan secara real-time.

#### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Pada saat saya memeriksa data yang ada pada JSON dan XML, penyajian data pada JSON lebih mudah dibaca oleh user karena tampilannya mirip dengan dictionary di python. Sedangkan, XML sedikit lebih kompleks dalam menyajikan datanya. Lalu, dalam sintaksisnya, JSON memerlukan lebih sedikit baris kode sehinggan ukuran filenya lebih kecil daripada XML padahal mereka sama-sama menyajikan data yang sama. Jadi, JSON lebih ringan dan lebih cepat dikirim ke frontend dibanding XML. Lalu, JSON menggunakan standar format untuk pertukaran data di API web modern karena JSON sesuai dengan Java Script dan memudahkan pengembangan web dibanding XML. Penggunaan JSON jauh lebih luas dibanding XML karena JSON dapat digunakan dikebanyakan platform yang memerlukan pertukaran data dengan cepat seperti perangkat IoT dan aplikasi obrolan. Jadi, JSON lebih populer dan lebih baik penggunaannya karena efisiensi dan kecepatannya yang lebih unggul dibanding XML. Namun, XML masih digunakan di beberapa sistem legacy atau jika dibutuhkan fitur tambahan seperti namespace dan skema validasi.

#### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

method is_valid() pada form Django tersebut berfungsi untuk memeriksa semua informasi dalam formulir atau serializer. Jadi, method ini akan memvalidasi apakah semua data formulir sesuai dengan aturan yang ditetapkan contohnya seperti tipe data yang ada di models.py, panjang karakter, atau field yang sesuai di forms.py. Jika ada data yang tidak sesuai dengan aturan atau terdapat kesalahan, method ini akan mengembalikan False.

Pada tugas 3 ini, kita membutuhkan method is_valid() untuk memeriksa kebenaran dan keakuratan dari database yang akan masuk ke frontend. Jadi nanti alurnya, data sebelum dikirim sebagai response, data akan divalidasi, setelah benar, baru akan mengirim permintaan POST.

### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token adalah suatu token unik yang akan otomatis dibuat oleh  Django untuk setiap sesi user. Token ini nantinya akan digunakan untuk memastikan setiap request yang dikirim melalui form atau data delivery ini benar-benar berasal dari pengguna yang sah melalui aplikasi yang sudah kita buat di projek Django, bukan dari sumber yang tidak jelas atau pun website eksternal lainnya.

Jika kita tidak menambahkan csrf_token dalam proses data delivery ini, resiko terjadinya serangan pada website frontend menjadi lebih tinggi. Biasanya csrf_token ini akan mencegah serangan CSRF (Cross-Site Request Forgery) untuk menyerang website. Serangan CSRF merupakan serangan dimana penyerang akan mencoba membuat pengguna yang sedang login di sebuah aplikasi atau platform otomatis mengirimkan request yang merugikan. Gambarannya itu seperti contoh ketika seorang pengguna sedang login di aplikasi bank, tanpa adanya csrf_token nantinya penyerang bisa membuat website palsu yang tanpa sepengetahuan pengguna, akan mengirimkan request transfer uang dari pengguna itu ke penyerang.

Mekanisme penggunaan csrf_token ini yaitu pada saat user add products, Django akan otomatis masuk ke csrf_token,bisa dilihat di templates create_product ada bagian `{% csrf_token %}`. Setelah user mengisi form dan submit produk, request tersebut membawa token ke server bersama data form. Lalu, akan diperiksa apakah token yang dikirim sama dengan token yang disimpan disaat user tadi mengisi form. Kalo sama, request diproses, jika tidak sama, Django akan error dan menolak request. 

Jadi, csrf_token ini berfungsi sebagai lapisan keamanan ekstra untuk memastikan bahwa hanya request sah dari aplikasi kita yang bisa diproses.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.

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

### 6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

Sejauh ini sudah sangat membantu kak tiap penjelasan di tutorial. Tiap penjelasan juga bisa dipahami dan dibaca-baca lagi untuk memahami materi lebih lanjut. Selain dari saran aku yang sebelumnya, sudah tidak ada lagi kak.

Berikut ini hasil screenshot dari Postman:
    https://drive.google.com/drive/folders/17UfFkrnKoyjxJH6Ukj0iGXMLd2sVQXdD?usp=sharing

## Tugas 4

### 1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

Django AuthenticationForm merupakan salah satu class dalam Django yang berbentuk (form) built-in yang akan mengkhususkan diri untuk menerima kredensial login seperti usernama dan password user. Form ini bertanggung jawab untuk memvalidasi data tersebut dan mencoba untuk mengautentikasi user dengan sistem autentikasi bawaan Django, yang melibatkan pengecekan akun pengguna, grup, dan izin mereka.

Kelebihan Django AuthenticationForm, yaitu:
- AuthenticationForm dapat memastikan proses login telah melewati validasi keamanan standar yang  disediakan oleh Dajngo untuk mengurangi resiko lemahnya keamanan sehingga terjadi penyerangan.
- AuthenticationForm sudah menyediakan fungsionalitas dasar untuk proses login, seperti validasi kredensial dan penanganan kesalahan, yang dapat digunakan secara langsung atau ditambahkan dengan sedikit penyesuaian.
- AuthenticationForm terintegrasi secara langsung dengan sistem autentikasi Django yang sudah lengkap dan kuat dalam memvalidasi, menangani sesi, pengguna, dan izin tanpa perlu menulis kode tambahan lagi.

Kekurangan Django AuthenticationForm, yaitu:
- AuthneticaationForm sudah built-in dengan fitur dan kelengkapan yang banyak, sehingga membutuhkan kerangka kerja yang lebih besar dan pengembang baru mungkin akan memerlukan waktu lebih lama untuk memahami form ini lebih dalam terkait teknis dan cara memodifikasinya.
- Meskipun AuthenticationForm merupakan sistem yang kuat, sistem autentikasi ini cukup generik dan tidak menyediakan banyak fitur spesifik yang umum ditemukan di sistem autentikasi web lain, yang mungkin membutuhkan solusi pihak ketiga untuk kebutuhan yang lebih canggih. 

### 2. Apa perbedaan antara autentikasi dan otorisasi? Bagaimana Django mengimplementasikan kedua konsep tersebut?

Autentikasi merupakan proses memverifikasi akun siapa yang hendak login. Sedangkan, otorisasi merupakan proses memverifikasi suatu akun berhak mengakses kebagian mana saja. 

Contoh yang memperlihatkan perbedaannya yaitu ketika seorang mahasiswa ingin masuk ke akun SIAK-NG nya, proses autentikasi akan memverifikasi yang masuk sebagai mahasiswa, sedangkan proses otorisasi akan memverifikasi mahasiswa tersebut dapat mengakses halaman IRS, Ringkasan, Pembayaran, dll.

Pada Django, ketika user memasukkan data kredensial seperti usernama dan password, data tersebut dikirim ke aplikasi Django. Lalu Django akan memverifikasi kredensial ini menggunakan backend autentikasi yang sudah built-in di dalam Django. Jika data kredensial benar, Django akan membuat sesi untuk user, menyimpan informasi pengguna, dan menyimpannya dalam cookie yang dikirim ke platform. Setelah login yang pertama kali, selanjutnya pada permintaan berikutnya, cookie akan berisi ID sesi yang dikirim ke server. Django akan menggunakan ID ini untuk mengambil data sesi, yang memungkinkan request.user menjadi pengguna yang diautentikasi. Terakhir, Django akan mengaplikasikan otorisasi menggunakan atribut request.user.is_authenticated untuk menentukan apakah pengguna telah masuk dan mengizinkan tindakan tertentu sesuai dengan izin pengguna.

### 3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

Dalam menyimpan state di aplikasi web, session dan cookie mempunyai kelebihan dan kekurangan sendiri.

a. Cookies
Kelebihan :
- Cookies dapat digunakan untuk menyimpan prefensi user seperti contohnya kapan terakhir kali user login seperti yang diaplikasikan pada tugas 4 ini.
- Cookies disimpan di client-side atau browser sehingga data tidak memberatkan server karena semua informasi tersimpan di perangkat user. Pada server-side, cookies hanya dibaca saat ada request.
- Cookies mudah diakses baik dari sisi client maupun server karena cookies bisa dibaca melalui JavaScript di browser maupun dikirim otomatis ke server saat request.
Kekurangan:
- Cookies tidak dapat digunakan untuk menyimpand data yang besar. Cookies hanya bisa menyimpan data 4 KB per cookie.
- Cookies akan selalu dikirim setiap request ke server, ketika jumlah dan ukuran cookies banyak, bisa menimbulkan beban dan lag pada jaringan.
- Dikarenakan cookies tersimpan di browser, user bisa mengedit cookies lewat DevTools dan dapat menimbulkan resiko terjadinya data dipalsukan.

b. Session
Kelebihan:
- Ketika session dibuat, data session akan disimpan di server. User hanya menyimpan session ID di cookies. Data asli ada di server, jadi lebih sulit bagi user untuk mengubahnya dan menjadi lebih aman dari resiko manipulasi data.
- Session bisa menyimpan data lebih besar karena penyimpanan dilakukan di server (misalnya di database, file, atau cache), tidak terbatas 4 KB.
Kekurangan:
- Jika ada banyak user yang membuat session, server harus menyimpan session tiap user. Ini bisa membebani penyimpanan dan efektifitas kerja pada server.
- Session bbergantung pada mekanisme session expiration,jadi ketika session tidak dikelola dengan penghapusan atau cleaning data, data session bisa menumpuk dan membuat server penuh.

### 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Seperti yang sudah dijelaskan di nomor 3, salah satu kekurangan cookies yaitu disimpan pada browser sehingga data yang kredensial atau sensitif dapat mudah dimodifikasi. Ada beberapa resiko yang potensial disebabkan oleh cookies, yaitu seperti manipulasi ketika user bisa mengubah isi cookies yang terlihat dengan menggunakan DevTools, lalu juga ada kemungkinan session ID dicuri dan ada orang yg menyamar jadi user aslinya, atau juga serangan seperti CSRF karena cookies dikirim otomatis ke server sehingga bisa saja disalahgunakan oleh penyamar.

Untuk mengatasi permasalahan tersebut, Django memiliki beberapa cara yaitu pertama Django sendiri akan mengenkripsi cookies tertentu sehingga tidak bisa diubah sembarangan seperti conthnya signed cookies yaitu Django menggunakan hashing untuk memastikan data cookie tidak dimodifikasi di client-side. Kedua, Django menyediakan [SESSION_COOKIE_HTTPONLY = True] yang berfungsi supaya cookies tidak dapat diakses melalui JavaScript untuk mengurangi resiko pencurian session ID dan juga [SESSION_COOKIE_SECURE = True] yang akan memastikan cookies hanya dikirim lewat HTTPS. Ketiga, Django akan menambahkan token CSRF untuk mencegah request yang tidak sesuai dengan pengguna atau peramban sah nya. 

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Berikut langkah-langkah yang saya lakukan untuk mengimplementasikan checlist tugas 4,
1. Pertama untuk melakukan autentikasi dibuat fungsi registrasi pada views.py dengan membuat form atau layout tampilan register pada halaman websitenya, lalu atur tampilan di file register.html, dan atur urls supaya fungsi register dapat tersampaikan ke user atau client-side
2. Kedua, membuat fungsi login dan logout, sama seperti langkah pertama yaitu membuat fungsi di views.py, lalu mengatur tampilan login di login.html dan logout di main.html karena logout hanya sekedar keluar dari halaman utama bukan suatu form yg baru. Bagian login dan logout disini ditambahkan otorisasi Django supaya web hanya dapat diakses oleh user sebenarnya.
3. Ketiga, mengimplementasikan cookies dan session pada proses autentikasi ini. Cookies ini digunakan untuk preferensi bagi user, sehingga kita dapat melihat kapan terakhir kali login menggunakan akun tersebut. Jadi pada views.py di fungsi login, disimpan cookies untuk menyimpan informasi login yang baru dilakukan dan disetting pada fungsi show_main di context agar terlihat di web bagian last_login termasuk mengatur tampilan di file main.html nya jg. Lalu, untuk menghapus data informasi login yg telah dilakukan saat logout, ditambahkan bagian delete_cookie pada fungsi logout.
4. Terakhir menghubungkan product dengan user agar tiap produk yg ditambahkan oeh suatu akun tertentu dapat tertulis pada product_details. Disini, saya mengatur models.py agar model produk dapat diakses oleh user sedang login, lalu dimigrasi, dan mengatur fungsi create_product di views.py agar tambahan produk user itu merupakan user yang memang sedang login, diatur juga pada templates htmlnya agar terlihat akun yg menambah produk tersebut. Mengatur juga bagian halaman utama agar namanya sesuai dengan akun yg sedang login. Lalu juga memisahkan bagian semua produk dengan bagian yang hanya produk akun kita sendiri dengan filter "My" dan "All" dan diatur juga pada templates html.

## Tugas 5

### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Ketika suatu elemen di HTML memiliki beberapa aturan CSS yang diterapkan, browser atau platform akan menentukan aturan mana yg akan digunakan terlebih dahulu berdasarkan tingkat prioritas pengambilan css selector dan juga cascade. Urutan prioritas tersebut meliputi, pertama adalah Inline styles atau gaya sebaris yang diterapkan langsung pada elemen HTML menggunakan atribut style. Kedua yaitu ID Selector atau pemilih ID seperti #header. Ketiga yaitu pemilih kelas, atribut, dan pseudo-kelas, kombinasi ketiga jenis ini memiliki bobot prioritas yang sama dan lebih rendah dari ID Selector. Terakhir adalah Element Selector atau pemilih elemen/tag yang merupakan selector dengan bobot spesifisitas paling rendah di antara yang utama diatasnya.

Lebih lanjut lagi terdapat faktor lainnya yang mempengaruhi prioritas CSS Selector. Terdapat aturan yaitu !importan rule yaitu aturan yang ditambahkan !important pada suatu selector akan memiliki prioritas paling tinggi, bahkan lebih tinggi dari prioritas pertama tadi yaitu Inline styles.

Terakhir, ada juga urutan dalam penulisan. Jika dua aturan memiliki spesifisitas yang sama, aturan yang dituliskan terakhir dalam lembar gaya yang akan diterapkan. 

### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

Responsive design adalah konsep pengembangan web yang memastikan tampilan website dapat menyesuaikan ukuran layar perangkat yang berbeda, baik itu smartphone, tablet, maupun desktop. Hal ini penting karena mayoritas pengguna internet sekarang mengakses website melalui perangkat mobile. Tanpa responsive design, website bisa terlihat berantakan, teks terlalu kecil, atau tombol sulit ditekan. Contoh aplikasi yang sudah menerapkan responsive design adalah Instagram atau Tokopedia, di mana tampilan grid produk atau feed akan menyesuaikan layar tanpa kehilangan kenyamanan. Sebaliknya, beberapa situs lama seperti forum jadul atau website sekolah lama sering tidak menerapkan responsive design, sehingga tampilannya hanya bagus di desktop tetapi rusak saat dibuka di HP.

### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

Dalam CSS box model, margin, border, dan padding adalah tiga komponen penting yang mengatur ruang di sekitar elemen. Margin adalah ruang di luar elemen, berfungsi untuk memberi jarak antar elemen yang berbeda. Border adalah garis tepi yang membungkus elemen, bisa diatur ketebalannya, warnanya, atau bentuknya. Padding adalah ruang di dalam elemen, yaitu jarak antara konten (teks/gambar) dengan border elemen tersebut. Misalnya pada tombol, margin dipakai untuk memberi jarak antar tombol, border memberi bingkai di sekitar tombol, dan padding membuat teks di dalam tombol tidak terlalu mepet dengan pinggiran. Implementasinya cukup dengan properti margin, border, dan padding di CSS.

### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox (Flexible Box Layout) adalah sistem layout di CSS yang dirancang untuk mengatur elemen dalam satu dimensi, baik secara horizontal (row) maupun vertikal (column). Kegunaannya sangat praktis untuk membuat elemen sejajar rapi, mengatur distribusi ruang, atau membuat tampilan responsif yang fleksibel. Contoh penggunaan flexbox adalah menyusun tombol aksi (Detail, Edit, Delete) agar sejajar secara horizontal. Sementara itu, Grid Layout adalah sistem layout dua dimensi yang memungkinkan kita membagi halaman menjadi baris dan kolom. Grid cocok digunakan ketika ingin membuat layout yang lebih kompleks seperti galeri produk, dashboard, atau halaman dengan banyak bagian yang perlu diatur secara presisi. Dengan grid, kita bisa dengan mudah menentukan elemen tertentu berada di baris dan kolom mana, sehingga struktur halaman lebih terorganisir.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

Berikut langkah-langkah yang saya lakukan dalam menyelesaikan checklist tugas 5,
1. Menambahkan fungsi atau button yang dapat menghapus dan mengedit product yang ada pada "My Products". Pertama membuat fungsi edit_product pada views.py yang nanti akan merefer ke data detail produk yang bisa dimodifikasi atau diubah dan masukkan path fungsi tersebut di urls.py supaya request bisa masuk ke views. Lalu juga menambahkan fungsi delete_product pada views.py yang akan mengambil objek produk dan menjalankan method delete yang akan menghapus data objek produk tersebut serta memasukkan path fungsi nya juga di urls.py supaya request delete bisa diakses dan dieksekusi di views.
2. Lalu menambahkan navigasi bar pada halaman main atau homepage yang dapat ditampilkan pada desktop dan juga mobile. Di file html nya diatur bar yang ada pada atas tampilan seperti pilihan fitur, juga atur bagian pada user yang bisa melihat views, terus juga atur login, register, dan logout, serta juga bagian menu-menu button seperti detail, edit, delete.
3. Terakhir, styling tampilan tiap page atau form pada platform dengan menggunakan css dan tailwind. Penampilan produk atau homepage disini digunakan css, dengan menambahkan class product-card pada global.css. Pada class ini diatur styling yang meliputi pengaturan shadow, jarak antar button, warna tombol, layout, dll. Lalu, dilanjut pada product_card.html yang berisi struktur HTML dari kartu product yang menyusun konten dan elemen tanpa tampilan yg sudah di-styling. HTML tersebut perlu diikat ke aturan-aturan di file CSS supaya tampilan platform rapi dan indah. Lalu, mengatur juga style pada form login, register, detail produk, form tambah produk, edit produk, tampilan jika belum ada produk menggunakan tailwind langsung divisualisasikan di html nya tanpa membuat class atau card dl.

## Tugas 6

### 1. Perbedaan antara synchronous request dan asynchronous request

Perbedaan utama antara synchronous request dan asynchronous request terletak pada cara browser berkomunikasi dengan server dan bagaimana halaman web meresponsnya. Pada synchronous request, ketika pengguna mengirimkan permintaan ke server (misalnya saat menekan tombol “Submit” pada form), browser akan menunggu hingga server selesai memproses dan mengembalikan respons. Selama proses itu, halaman web tidak dapat digunakan dan biasanya akan melakukan reload secara penuh ketika respons diterima. Sebaliknya, pada asynchronous request—yang umumnya diimplementasikan menggunakan AJAX (Asynchronous JavaScript and XML)—permintaan dikirim ke server di latar belakang tanpa harus memuat ulang seluruh halaman. Browser tetap bisa digunakan sambil menunggu respons, dan hanya bagian tertentu dari halaman yang diperbarui. Inilah yang membuat AJAX mampu memberikan pengalaman yang lebih cepat dan interaktif dibandingkan permintaan sinkron biasa.

### 2. Bagaimana AJAX bekerja di Django (alur request–response)

Dalam konteks Django, AJAX bekerja dengan cara menghubungkan JavaScript di sisi frontend dengan view Django di sisi backend tanpa harus me-reload halaman. Ketika pengguna melakukan suatu aksi di halaman web—misalnya menekan tombol untuk menambah komentar—JavaScript akan menangkap peristiwa tersebut dan mengirimkan HTTP request ke URL tertentu (biasanya endpoint yang disiapkan untuk AJAX), menggunakan metode seperti fetch() atau $.ajax(). Django kemudian menerima permintaan tersebut melalui fungsi view, memproses datanya (misalnya menyimpan komentar baru ke database), dan mengirimkan kembali respons dalam format JSON. Setelah itu, JavaScript menerima data JSON dari Django dan menampilkan hasilnya langsung ke halaman web, misalnya dengan menambahkan elemen HTML baru. Dengan alur seperti ini, pengguna dapat melihat hasil aksi mereka secara langsung tanpa meninggalkan atau me-refresh halaman.

### 3. Keuntungan menggunakan AJAX dibandingkan render biasa di Django

Penggunaan AJAX dalam Django memberikan sejumlah keuntungan signifikan dibandingkan dengan proses render halaman secara penuh. AJAX memungkinkan pembaruan sebagian halaman secara dinamis tanpa perlu me-reload seluruh laman, sehingga proses menjadi lebih cepat dan efisien. Hal ini menghemat bandwidth karena hanya data yang dibutuhkan (biasanya dalam format JSON) yang dikirim, bukan seluruh halaman HTML. Selain itu, aplikasi web menjadi lebih interaktif dan responsif, membuat pengguna merasa seperti menggunakan aplikasi desktop atau mobile. AJAX juga sangat berguna untuk fitur-fitur yang membutuhkan pembaruan real-time seperti sistem komentar, tombol like, notifikasi, atau dashboard data. Sementara render biasa cenderung lebih lambat karena setiap perubahan kecil tetap memerlukan pemuatan ulang seluruh halaman dari awal.

### 4. Cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django

Keamanan adalah hal penting ketika menggunakan AJAX, terutama untuk fitur sensitif seperti login dan register. Langkah pertama yang wajib dilakukan adalah memastikan setiap request AJAX disertai dengan CSRF token, karena Django secara default melindungi aplikasi dari serangan Cross-Site Request Forgery. Token ini biasanya dikirimkan melalui header atau hidden input field dalam form. Selain itu, komunikasi harus menggunakan protokol HTTPS agar data seperti kata sandi tidak bocor selama transmisi. Validasi input juga harus dilakukan di sisi server, bukan hanya di sisi klien, agar pengguna tidak bisa melewati pemeriksaan dengan memanipulasi JavaScript. Django juga menyediakan decorator seperti @login_required dan @require_POST untuk membatasi siapa yang boleh mengakses endpoint tertentu. Terakhir, jangan pernah mengembalikan data sensitif dalam respons JSON, serta pertimbangkan penggunaan rate limiting atau CAPTCHA untuk mencegah serangan brute-force pada proses login dan pendaftaran.

### 5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience)

Penggunaan AJAX memiliki dampak besar terhadap peningkatan User Experience (UX) di sebuah website. Dengan AJAX, interaksi antar pengguna dan sistem menjadi lebih cepat karena tidak perlu menunggu pemuatan ulang halaman setiap kali terjadi perubahan. Halaman terasa lebih hidup dan responsif, karena data dapat diperbarui secara langsung tanpa mengganggu aktivitas pengguna. Misalnya, ketika pengguna menekan tombol “Like” atau menambah komentar, hasilnya langsung muncul di layar tanpa perpindahan halaman, sehingga menciptakan pengalaman yang mulus dan efisien. Selain itu, AJAX memungkinkan pengembangan fitur real-time seperti notifikasi langsung, chat box, atau pembaruan data secara otomatis. Namun demikian, pengembang juga perlu memastikan bahwa setiap respons AJAX ditangani dengan baik, termasuk menampilkan pesan kesalahan atau indikator pemuatan, agar pengguna tidak merasa bingung jika terjadi kegagalan pada proses di latar belakang.