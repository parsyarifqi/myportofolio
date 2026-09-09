import uuid
from django.db import models


# Create your models here.
class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research','Research'),
        ('volunteer','Volunteer'),
        ('part-time','Part-time'),
        ('full-time','Full-time'),
        ('freelance','Freelance'),
        ('academics', 'Academics'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

"""Penjelasan kode:

- models.Model adalah kelas dasar yang digunakan untuk mendefinisikan model dalam Django.

- Experience adalah nama model yang kamu definisikan.

- EXPERIENCE_CHOICES adalah tuple yang mendefinisikan pilihan kategori pengalaman yang tersedia.

- id adalah field bertipe UUIDField yang digunakan sebagai primary key dan nilainya di-generate otomatis menggunakan uuid.uuid4.

- title adalah field bertipe CharField untuk judul pengalaman, dengan panjang maksimal 255 karakter.

- description adalah field bertipe TextField untuk deskripsi pengalaman yang dapat menampung teks panjang.

- category adalah field bertipe CharField dengan pilihan terbatas sesuai EXPERIENCE_CHOICES, dengan nilai default 'full-time'.

- thumbnail adalah field bertipe URLField untuk menyimpan URL gambar thumbnail pengalaman (opsional).

- started_at adalah field bertipe DateTimeField yang otomatis berisi tanggal dan waktu saat data dibuat.

- ended_at adalah field bertipe DateTimeField yang dapat dibiarkan kosong dan nilainya dapat diatur ke None.

- Method __str__ digunakan untuk mengembalikan representasi string dari objek (dalam hal ini judul pengalaman).

- Decorator @property digunakan untuk membuat atribut read-only yang nilainya merupakan hasil perhitungan dari atribut lain. Dalam kasus ini, is_ongoing akan bernilai True jika ended_at adalah None.

"""