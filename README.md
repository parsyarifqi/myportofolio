Nama : Parsya Rifqi Subhani Petrana
NPM : 2506535992

Nama : Parsya Rifqi Subhani Petrana
NPM : 2506535992
Kelas : PBP E

### Tugas 1
1. ya, saya menggunakan elemen <section> dan <article> dalam pembuatan web portofolio saya. Penggunaan <section> bertujuan sebagai wadah yang menampung riwayat pendidikan saya pada section Education dan riwayat experience saya pada section Experience, Ini membuat tampilan HTML menjadi lebih rapi dan terstruktur karena dengan melihat tag <section> kita bisa langsung tahu bahwa elemen yang ada di dalam tag tersebut merupakan penyusun dari suatu section. Selain itu, Penggunaan <section> juga membuat saya dapat menambahkan shortcut pada navbar sehingga orang yang mengunjungi web saya dapat langsung lompat ke section yang mereka ingin lihat tanpa harus mencari, walaupun web saya sekarang hanya mengandung beberapa section namun jika web yang saya buat mengandung banyak section, ini akan sangat memudahkan pengunjung untuk menavigasikan web saya. Selain <section>, penggunaan <article> juga sangat berguna sebagai wadah untuk menampung secara individu entri-entri pada section Education dan Experience saya.

2.tantangan layout yang saya dapati mungkin berhubungan dengan section Education pada bagian garis timeline dimana pada saat beralih ke tampilan mobile, garisnya menjadi panjang kebawah. cara saya mengatasi ini adalah dengan menggunakan fungsi calc() untuk menghitung height. saya menggunakan calc(100% + 3 rem). Dengan menggunakan fungsi ini, ketika mengubah ke tampilan mobile, garis timeline tersebut memiliki panjang yang pas dan tidak memanjang ke bawah. Selain itu juga ukuran font menjadi tantangan ketika diubah ke tampilan mobile terutama di bagian header dari masing-masing section. ketika tampilan dipersempit, ukuran fontnya terlihat terlalu besar dan kurang rapi, Namun dengan menggunakan fungsi clamp(min, ideal, max) pada css untuk mengatur height membuat tampilan menjadi lebih responsif karena ukurannya menyesuaikan dengan layar dengan tidak lebih kecil dari ukuran min dan tidak lebih besar dari ukuran max.

3. batasan yang saya rasakan mungkin adalah ketika ingin merubah atau menambahkan entri pada section experience atau education masih harus dilakukan perubahan di file html secara langsung. untuk selanjutnya saya ingin menerapkan fungsionalitas database agar apabila perlu menambahkan atau mengubah entri pada section education dan experience bisa dilakukan pada file json tanpa merombak file html.

–AI DISCLOSURE–
Pada tugas ini saya menggunakan bantuan AI Claude untuk membantu pengerjaan saya. Strategi yang saya gunakan dalam menggunakan AI ini adalah saya meminta claude untuk menjadi pembimbing saya dalam menuliskan kode saya. Karena saya merupakan tipe yang learn by doing jadi saya lebih memilih menyuruh AI sebagai pembimbing saya dalam mempraktekan penulisan kode HTML. Saya hanya meminta kepada claude untuk menjelaskan kepada saya bagaimana melakukan sesuatu dalam html dan css lalu berdasarkan penjelasan claude, saya mencoba menulis kode saya sendiri. Pada chat terakhir dari percakapan claude yang saya gunakan untuk tugas ini, saya telah menyuruh Claude untuk memberikan penjelasan strategi yang saya gunakan dalam menggunakan AI. berikut adalah linknya: https://claude.ai/share/bb25c62d-75b4-4978-9069-3b03c7506459 

### Tugas 1 end


### Tugas 2
- Pengguna mengakses web portofolio dan mengirimkan HTTP request
-  urls.py pada tingkat proyek akan meneruskan request ke urls.py tingkat app.
- urls tingkat app akan mencocokkan url (jika “” maka ke profile, jika “/experience” maka ke experience, jika “/education” maka ke education)
- setelah dicocokkan di urls.py tingkat app maka fungsi show_main / show_education / show_experience akan dipanggil sesuai url yang dicocokkan)
-views.py kemudian akan merender template html dari section yang dipanggil dan mengambil data dari models.py untuk ditampilkan
- template html kemudian akan diisi dengan data yang telah diambil melalui models.py.
-views.py kemudian mengembalikan template html yang telah diisi dengan data yang sesuai melalui HTTP response.
Data yang disimpan pada model merupakan bentuk penerapan separation of concerns. templates html sekarang hanya fokus berperan sebagai kerangka dari website dan tinggal diisi dengan data yang disimpan pada models. ini membuat pembaruan pada templates html itu sendiri lebih aman tanpa potensi merusak data yang tersimpan, sebaliknya perubahan pada data yang disimpan juga tidak akan berpotensi mengacaukan tampilan html saat ditampilkan. Selain itu jika ada masalah maka kita dapat melihat dengan jelas dari mana asal masalahnya, apakah dari kode htmlnya atau dari data yang tersimpan karena keduanya terpisah satu sama lain. Ini akan memudahkan pengembangan dan pemeliharaan karena kita dapat fokus hanya pada bagian tertentu tanpa mempengaruhi bagian lain. Selain itu apabila data yang perlu ditampilkan sangat banyak, ini akan sangat mempersingkat kode html kita karena kita hanya perlu looping seluruh data pada models untuk menampilkan seluruh data yang perlu ditampilkan.
makemigrations berfungsi mencatat perubahan apa saja yang perlu dilakukan pada models dan membuat file yang berisi instruksi perubahan yang akan dilakukan. migrate kemudian membaca instruksi perubahan yang telah dibuat setelah menjalankan makemigrations dan menerapkan perubahan tersebut. Perubahan yang dibuat oleh migrate akan mempengaruhi seluruh data yang disimpan di database. Contoh kasus yang memerlukan makemigrations dan migrate adalah ketika kita menambahkan/mengubah/menghapus field pada model yang ada pada models.py.
Menambahkan/mengubah/menghapus field akan mengubah struktur data yang disimpan sehingga diperlukan makemigrations dan migrate untuk menerapkan perubahan tersebut.

### AI DISCLOSURE:
Pengerjaan tugas mandiri 2 ini dibantu oleh AI yaitu Claude model Sonnet 5 dengan effort medium. Prompt awal yang saya berikan adalah: "saya ingin anda berperan STRICTLY sebagai pembimbing saya dalam mengerjakan proyek ini. anda TIDAK DIPERKENANKAN memberikan jawaban secara mentah. saya akan melakukan proses kodingnya, anda cukup membimbing dan mengkoreksi saya." jadi dalam pengerjaan ini penggunaan AI berperan sebagai pembimbing, karena saya adalah tipe orang yang learn by doing  jadi saya perlu feedback langsung yang dalam kasus ini berasal dari AI untuk membantu saya. Berikut adalah percakapan claude yang saya gunakan untuk mengerjakan tugas individu 2 ini: https://claude.ai/share/0c79e5d9-be8d-4f0e-8d0a-087af7d64a84
saya telah memberikan prompt pada claude agar menjelaskan lebih lanjut mengenai peran penggunaan AI dalam pengerjaan tugas saya yang berada pada chat paling terakhir.

### Instruksi setup mingguan:
membuat branch baru sesuai dengan tugas/tutorial yang diberikan
menjalankan virtual environment
melakukan instruksi yang diberikan tugas atau tutorial dan commit berkala
melakukan makemigrations dan migrate apabila terdapat perubahan pada struktur data yang disimpan
merge branch to main agar sinkron dengan branch utama

### Progress tugas 2:

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

### Progress tugas 3:
16 september: refactor berkas html yang identik disetiap berkas html dengan meng extend ke base.html
20 september: membuat ModelForm EducationForm untuk section Education di forms.py
20 september: membuat ModelForm ExperienceForm untuk section Experience di forms.py
21 september: menambahkan fungsi fungsi operasi CRUD (Create, Read, Update, Delete) untuk section education di views.py main
21 september: menambahkan fungsi fungsi operasi CRUD (Create, Read, Update, Delete) untuk section education di views.py main
21 september: memperbaiki typo dan kode yang redundan