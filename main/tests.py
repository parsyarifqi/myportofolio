from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience
from main.models import Education


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="PT. Balai Lelang Sempurna",
            description="Admin Assistant",
            category="internship",
            started_at='2025-08-19 00:00:00',
        )

        self.education = Education.objects.create(
            institution="Universitas Indonesia",
            faculty="Computer Science",
            thumbnail="/static/img/fasilkom.png",
            started_at=2025,
        )

    def get_api_json(self, url_name):
        """Mengambil daftar data dari API sebagai JSON (data kini tidak lagi ada di HTML)."""
        response = self.client.get(reverse(url_name), HTTP_ACCEPT="application/json")
        self.assertEqual(response.status_code, 200)
        return response.json()

    # ----- Tidak terpengaruh perubahan DRF -----------------------------

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertContains(response, f'href="{reverse("main:show_education")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "PT. Balai Lelang Sempurna")
        self.assertEqual(self.experience.category, "internship")
        self.assertTrue(self.experience.is_ongoing)

    def test_education_model(self):
        self.assertEqual(str(self.education), "Universitas Indonesia")
        self.assertEqual(self.education.faculty, "Computer Science")
        self.assertTrue(self.education.is_ongoing)

    # ----- Halaman: kini hanya kerangka, data diambil lewat API --------

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        # Kerangka AJAX dan endpoint API yang dipakai script
        self.assertContains(response, 'id="grid"')
        self.assertContains(response, reverse("api:experience-list"))
        # Data TIDAK ada di HTML awal; dimuat browser lewat fetch
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, f'href="{reverse("main:show_education")}"')

    def test_education_page(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")
        self.assertContains(response, 'id="grid"')
        self.assertContains(response, reverse("api:education-list"))
        self.assertNotContains(response, self.education.institution)
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    # ----- Data: diperiksa lewat API -----------------------------------

    def test_experience_data_comes_from_api(self):
        data = self.get_api_json("api:experience-list")

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["title"], self.experience.title)
        self.assertEqual(data[0]["description"], self.experience.description)
        self.assertEqual(data[0]["category"], "internship")
        self.assertTrue(data[0]["is_ongoing"])
        self.assertIsNone(data[0]["ended_at"])

    def test_education_data_comes_from_api(self):
        data = self.get_api_json("api:education-list")

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["institution"], self.education.institution)
        self.assertEqual(data[0]["faculty"], self.education.faculty)
        self.assertEqual(data[0]["started_at"], 2025)
        self.assertIsNone(data[0]["ended_at"])

    def test_empty_experience_page(self):
        Experience.objects.all().delete()

        self.assertEqual(self.get_api_json("api:experience-list"), [])
        page = self.client.get(reverse("main:show_experience"))
        self.assertContains(page, 'id="empty"')

    def test_empty_education_page(self):
        Education.objects.all().delete()

        self.assertEqual(self.get_api_json("api:education-list"), [])
        page = self.client.get(reverse("main:show_education"))
        self.assertContains(page, 'id="empty"')

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        data = self.get_api_json("api:experience-list")

        self.assertFalse(self.experience.is_ongoing)
        self.assertFalse(data[0]["is_ongoing"])
        self.assertIsNotNone(data[0]["ended_at"])

    def test_completed_education(self):
        self.education.ended_at = timezone.now().year
        self.education.save()
        data = self.get_api_json("api:education-list")

        self.assertFalse(self.education.is_ongoing)
        self.assertEqual(data[0]["started_at"], self.education.started_at)
        self.assertEqual(data[0]["ended_at"], self.education.ended_at)