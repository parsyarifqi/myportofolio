from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

"""
ModelForm adalah builtins library yang telah disediakan oleh Django untuk membuat boilerplate suatu form. Struktur dari form sendiri dapat dikustomasi menggunakan metadata atau class Meta.

Penjelasan Kode

- model digunakan untuk menentukan model Django yang menjadi sumber data dan struktur dari ModelForm. Field pada form akan dibuat berdasarkan field yang terdapat pada model tersebut.
- fields digunakan untuk menentukan field model yang ingin ditampilkan pada form. Field dapat ditulis secara eksplisit, seperti ["title", "description"], atau menggunakan "__all__" untuk menampilkan seluruh field yang tersedia.
- widgets digunakan untuk mengatur tampilan dan jenis elemen HTML yang digunakan oleh setiap field pada form. Pada kode di atas, TextInput digunakan untuk field teks satu baris, Textarea digunakan untuk field deskripsi yang membutuhkan area teks lebih besar, dan URLInput digunakan untuk field yang berisi URL. Atribut di dalam attrs, seperti placeholder, maxlength, dan rows, digunakan untuk teks petunjuk, batas jumlah karakter, serta tinggi area input.
"""