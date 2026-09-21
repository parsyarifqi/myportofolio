Nama : Parsya Rifqi Subhani Petrana
NPM : 2506535992

Nama : Parsya Rifqi Subhani Petrana
NPM : 2506535992
Kelas : PBP E

### Tugas 1

### Pertanyaan Reflektif
1. ya, saya menggunakan elemen <section> dan <article> dalam pembuatan web portofolio saya. Penggunaan <section> bertujuan sebagai wadah yang menampung riwayat pendidikan saya pada section Education dan riwayat experience saya pada section Experience, Ini membuat tampilan HTML menjadi lebih rapi dan terstruktur karena dengan melihat tag <section> kita bisa langsung tahu bahwa elemen yang ada di dalam tag tersebut merupakan penyusun dari suatu section. Selain itu, Penggunaan <section> juga membuat saya dapat menambahkan shortcut pada navbar sehingga orang yang mengunjungi web saya dapat langsung lompat ke section yang mereka ingin lihat tanpa harus mencari, walaupun web saya sekarang hanya mengandung beberapa section namun jika web yang saya buat mengandung banyak section, ini akan sangat memudahkan pengunjung untuk menavigasikan web saya. Selain <section>, penggunaan <article> juga sangat berguna sebagai wadah untuk menampung secara individu entri-entri pada section Education dan Experience saya.

2.tantangan layout yang saya dapati mungkin berhubungan dengan section Education pada bagian garis timeline dimana pada saat beralih ke tampilan mobile, garisnya menjadi panjang kebawah. cara saya mengatasi ini adalah dengan menggunakan fungsi calc() untuk menghitung height. saya menggunakan calc(100% + 3 rem). Dengan menggunakan fungsi ini, ketika mengubah ke tampilan mobile, garis timeline tersebut memiliki panjang yang pas dan tidak memanjang ke bawah. Selain itu juga ukuran font menjadi tantangan ketika diubah ke tampilan mobile terutama di bagian header dari masing-masing section. ketika tampilan dipersempit, ukuran fontnya terlihat terlalu besar dan kurang rapi, Namun dengan menggunakan fungsi clamp(min, ideal, max) pada css untuk mengatur height membuat tampilan menjadi lebih responsif karena ukurannya menyesuaikan dengan layar dengan tidak lebih kecil dari ukuran min dan tidak lebih besar dari ukuran max.

3. batasan yang saya rasakan mungkin adalah ketika ingin merubah atau menambahkan entri pada section experience atau education masih harus dilakukan perubahan di file html secara langsung. untuk selanjutnya saya ingin menerapkan fungsionalitas database agar apabila perlu menambahkan atau mengubah entri pada section education dan experience bisa dilakukan pada file json tanpa merombak file html.

### –AI DISCLOSURE–:
Pada tugas ini saya menggunakan bantuan AI Claude untuk membantu pengerjaan saya. Strategi yang saya gunakan dalam menggunakan AI ini adalah saya meminta claude untuk menjadi pembimbing saya dalam menuliskan kode saya. Karena saya merupakan tipe yang learn by doing jadi saya lebih memilih menyuruh AI sebagai pembimbing saya dalam mempraktekan penulisan kode HTML. Saya hanya meminta kepada claude untuk menjelaskan kepada saya bagaimana melakukan sesuatu dalam html dan css lalu berdasarkan penjelasan claude, saya mencoba menulis kode saya sendiri. Pada chat terakhir dari percakapan claude yang saya gunakan untuk tugas ini, saya telah menyuruh Claude untuk memberikan penjelasan strategi yang saya gunakan dalam menggunakan AI. berikut adalah linknya: https://claude.ai/share/bb25c62d-75b4-4978-9069-3b03c7506459 

### Tugas 1 end


### Tugas 2

### Pertanayaan Reflektif
1. - Pengguna mengakses web portofolio dan mengirimkan HTTP request 
- urls.py pada tingkat proyek akan meneruskan request ke urls.py tingkat app.
- urls tingkat app akan mencocokkan url (jika “” maka ke profile, jika “/experience” maka ke experience, jika “/education” maka ke education)
- setelah dicocokkan di urls.py tingkat app maka fungsi show_main / show_education / show_experience akan dipanggil sesuai url yang dicocokkan
-views.py kemudian akan merender template html dari section yang dipanggil dan mengambil data dari models.py untuk ditampilkan
- template html kemudian akan diisi dengan data yang telah diambil melalui models.py.
-views.py kemudian mengembalikan template html yang telah diisi dengan data yang sesuai melalui HTTP response.
2. Data yang disimpan pada model merupakan bentuk penerapan separation of concerns. templates html sekarang hanya fokus berperan sebagai kerangka dari website dan tinggal diisi dengan data yang disimpan pada models. ini membuat pembaruan pada templates html itu sendiri lebih aman tanpa potensi merusak data yang tersimpan, sebaliknya perubahan pada data yang disimpan juga tidak akan berpotensi mengacaukan tampilan html saat ditampilkan. Selain itu jika ada masalah maka kita dapat melihat dengan jelas dari mana asal masalahnya, apakah dari kode htmlnya atau dari data yang tersimpan karena keduanya terpisah satu sama lain. Ini akan memudahkan pengembangan dan pemeliharaan karena kita dapat fokus hanya pada bagian tertentu tanpa mempengaruhi bagian lain. Selain itu apabila data yang perlu ditampilkan sangat banyak, ini akan sangat mempersingkat kode html kita karena kita hanya perlu looping seluruh data pada models untuk menampilkan seluruh data yang perlu ditampilkan.
3. makemigrations berfungsi mencatat perubahan apa saja yang perlu dilakukan pada models dan membuat file yang berisi instruksi perubahan yang akan dilakukan. migrate kemudian membaca instruksi perubahan yang telah dibuat setelah menjalankan makemigrations dan menerapkan perubahan tersebut. Perubahan yang dibuat oleh migrate akan mempengaruhi seluruh data yang disimpan di database. Contoh kasus yang memerlukan makemigrations dan migrate adalah ketika kita menambahkan/mengubah/menghapus field pada model yang ada pada models.py.
Menambahkan/mengubah/menghapus field akan mengubah struktur data yang disimpan sehingga diperlukan makemigrations dan migrate untuk menerapkan perubahan tersebut.

### -AI DISCLOSURE-:
Pengerjaan tugas mandiri 2 ini dibantu oleh AI yaitu Claude model Sonnet 5 dengan effort medium. Prompt awal yang saya berikan adalah: "saya ingin anda berperan STRICTLY sebagai pembimbing saya dalam mengerjakan proyek ini. anda TIDAK DIPERKENANKAN memberikan jawaban secara mentah. saya akan melakukan proses kodingnya, anda cukup membimbing dan mengkoreksi saya." jadi dalam pengerjaan ini penggunaan AI berperan sebagai pembimbing, karena saya adalah tipe orang yang learn by doing  jadi saya perlu feedback langsung yang dalam kasus ini berasal dari AI untuk membantu saya. Berikut adalah percakapan claude yang saya gunakan untuk mengerjakan tugas individu 2 ini: https://claude.ai/share/0c79e5d9-be8d-4f0e-8d0a-087af7d64a84
saya telah memberikan prompt pada claude agar menjelaskan lebih lanjut mengenai peran penggunaan AI dalam pengerjaan tugas saya yang berada pada chat paling terakhir.

### Instruksi Setup Mingguan:
membuat branch baru sesuai dengan tugas/tutorial yang diberikan
menjalankan virtual environment
melakukan instruksi yang diberikan tugas atau tutorial dan commit berkala
melakukan makemigrations dan migrate apabila terdapat perubahan pada struktur data yang disimpan
merge branch to main agar sinkron dengan branch utama


### Progres Mingguan
12 september: menambahkan model Education pada models.py pada app main
13 september: 
section education sekarang mengambil data dari model lalu memasukkan ke context, data tidak lagi di hardcode dalam html, section education sekarang memiliki file html terpisah (Education.html) dan dapat di akses dari bar navigasi.
mengatur logo institusi di section education yang sebelumnya terlalu besar ke ukuran yang sesuai.
14 september: 
mengatasi masalah section education dan experience di web pws yang error ketika dibuka dengan mengubah argumen os.getenv() dengan env var names dengan fallback values
menambahkan ulang data pada section education dan experience lewat shell di terminal pws
menambahkan fitur darkmode kedalam web
menambahkan test case untuk modul education
mengerjakan pertanyaan reflektif

### Tugas 2 end

### Tugas 3

### Pertanyaan Reflektif:
1. Karena penggunaan ModelForm menghubungkan langsung form dengan Model maka kita tidak perlu membuat field html secara manual karena ModelForm sudah mebuat field yang sesuai dengan Model secara otomatis, selain itu kita tidak perlu melakukan seluruh proses validasi data karena ModelForm melalui form.is_valid sudah melakukan validasi secara otomatis. Penggunaan {% csrf_token %} mencegah terjadinya Cross-Site Request Forgery dimana penyerang mengirimkan request dari sesi pengguna yang terautentikasi untuk melakukan tindakan yang tidak diinginkan. Csrf token adalah string acak yang unik yang dibuat pada saat halaman dimuat. Csrf harus diikutsertakan sebagai bentuk verifikasi saat pengguna ingin mengirim data. Server akan mencocokkan token csrf yang diterima dengan token yang disimpan di sesi pengguna. Jika token yang diterima cocok barulah pengiriman data oleh pengguna akan diterima oleh server.

2. Karena JSON memiliki format yang lebih ringan, cepat, dan mudah serta memiliki readability dan yang lebih baik dibandingkan XML. JSON menyimpan data dengan struktur key:value yang lebih intuitif sedangkan XML menyimpan data dalam struktur Tree yang lebih rumit dan lebih sulit dibaca dibanding JSON. Selain itu juga JSON sudah terintegrasi dengan JavaScript yang banyak digunakan sehingga kita tidak perlu melakukan parsing yang rumit.

3. menggunakan alur get_project_json() sebagai contoh. pada get_project_json(), pertama, get_project_json() menerima request dari client. lalu title_query mengambil title dari project yang ingin dikembalikan. selanjutnya kita mengambil seluruh object project menggunakan Project.objects.all(). jika title_query bernilai true (artinya terdapat parameter title pada request) maka kita akan memfilter berdasarkan parameter title yang disimpan di title_query menggunakan title__icontains=title_query. Kedua, kita mengubah object proeject yang disimpan dalam model django menjadi bentuk json menggunakan serializers.serialize("json", projects) yang disimpan kedalam projects_json. ketiga, kita mengembalikan http response: return HttpResponse(projects_json, content_type="application/json") yang berupa object project yang disimpan dalam model django yang telah dirubah ke json sebelumnya. proses serialization disini berfungsi mengubah object yang disimpan dalam Model django kedalam bentuk JSON.

### -AI DISCLOSURE-:
Saya menyatakan bahwa pengerjaan individual assignemnt 3 ini saya kerjakan menggunakan AI Claude. Saya menggunakan AI Claude untuk melakukan proses debug. Berikut adalah penjelasan dari chat Claude AI yang saya gunakan dalam pengerjaan tugas ini tentang bagaimana saya menggunakannya:

"Ringkasan penggunaan AI (Claude) dalam pengerjaan tugas ini

Selama sesi ini, saya (mahasiswa) yang menulis seluruh kode — model, form, view, URL routing, dan template HTML — secara mandiri. Peran AI di sini murni sebagai reviewer/debugger, bukan penulis kode:

Saya upload kode yang sudah saya tulis (forms.py, models.py, views.py, urls.py, template HTML), lalu minta AI mengidentifikasi kesalahan.
AI tidak pernah menuliskan kode implementasi untuk saya. Setiap bug yang ditemukan dijelaskan penyebabnya (misal: field non-editable dimasukkan ke ModelForm, nama fungsi tidak konsisten antara urls.py dan views.py, key request.GET tidak cocok dengan name input di form HTML), lalu saya yang menentukan dan menulis perbaikannya sendiri.
Ketika ada keputusan desain (misalnya soal field started_at di model Experience — apakah otomatis atau bisa diisi manual), AI memberi opsi dan trade-off-nya, saya yang memutuskan lalu mengimplementasikan sendiri, termasuk migrasi database.
Beberapa bug ditemukan lewat proses iteratif: saya jalankan kode, dapat error dari Django (NoReverseMatch, 404, dll), tempel error itu ke chat, AI bantu telusuri baris mana yang jadi penyebab, saya perbaiki, lalu diverifikasi ulang.

Jenis kesalahan yang berhasil diidentifikasi antara lain: import yang belum lengkap, field model yang tidak editable tapi dipaksa masuk form, penamaan fungsi/URL yang tidak konsisten (menyebabkan NoReverseMatch), parameter request.GET yang tidak match dengan atribut form, dan kesalahan menyalin (copy-paste) antar-file yang membuat referensi salah."

untuk link percakapan AI Claude yang saya gunakan: https://claude.ai/share/83cad79b-7cda-4c31-9e1f-8162b22d343f

### Instruksi setup mingguan:
membuat branch baru sesuai dengan tugas/tutorial yang diberikan
menjalankan virtual environment
melakukan instruksi yang diberikan tugas atau tutorial dan commit berkala
melakukan makemigrations dan migrate apabila terdapat perubahan pada struktur data yang disimpan
merge branch to main agar sinkron dengan branch utama

### Progress Mingguan
16 september: refactor berkas html yang identik disetiap berkas html dengan meng extend ke base.html
20 september: membuat ModelForm EducationForm untuk section Education di forms.py
20 september: membuat ModelForm ExperienceForm untuk section Experience di forms.py
21 september: menambahkan fungsi fungsi operasi CRUD (Create, Read, Update, Delete) untuk section education di views.py main
21 september: menambahkan fungsi fungsi operasi CRUD (Create, Read, Update, Delete) untuk section education di views.py main
21 september: memperbaiki typo dan kode yang redundan
21 september: melakukan perubahan pada models.py Experience field started_at agar dapat diedit.
21 september: menambahkan fitur untuk mencari dan menghapus data pada section education dan experience.
21 september: menambahkan fitur untuk menambahkan data pada section education dan experience
21 september: menambahkan fitur untuk mengedit data pada section education, experience, dan project


### Tugas 3 End ###
