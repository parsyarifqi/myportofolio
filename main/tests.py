from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="PT. Balai Lelang Sempurna",
            description="Admin Assistant",
            category="internship",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "PT. Balai Lelang Sempurna")
        self.assertEqual(self.experience.category, "internship")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Internship")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

"""
Semua method yang namanya diawali test_ akan dijalankan otomatis oleh Django. Method setUp() dijalankan sebelum setiap test sehingga tiap test memperoleh data awal yang bersih.

Enam test tersebut memeriksa hal yang berbeda:

1.) Halaman profil dapat diakses, memakai index.html, tidak menampilkan kartu pengalaman, dan memiliki tautan ke halaman Experience.
2.) URL yang tidak terdaftar menghasilkan status 404 Not Found.
3.) Model menyimpan nilai dan menghitung is_ongoing dengan benar.
4.) Halaman Experience memakai experience.html, menampilkan data model beserta kategori dan statusnya, serta memiliki tautan kembali ke profil.
5.) Halaman Experience menampilkan pesan yang sesuai ketika belum ada data.
6.) Pengalaman dengan ended_at terisi menampilkan status Selesai.

reverse() mencari URL berdasarkan app_name dan name yang telah dibuat di main/urls.py, sama seperti tag {% url %} pada template. Cara ini membuat tautan dan test tetap mengikuti rute jika path berubah. assertNotContains memastikan teks tertentu tidak muncul dalam respons, sedangkan timezone.now() memberikan waktu saat ini untuk mengisi ended_at pada test pengalaman yang sudah selesai.
"""