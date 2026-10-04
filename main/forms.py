from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateTimeInput

from main.models import Project, Education, Experience

from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

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
    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data["tech_stack"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

"""
Penjelasan Kode

- Method dengan pola nama clean_<nama_field> dijalankan otomatis oleh Django saat form.is_valid() dipanggil, setelah validasi bawaan field tersebut lolos. Nilai yang dikembalikan menggantikan isi cleaned_data untuk field itu, dan nilai inilah yang disimpan oleh form.save().

- strip_tags menghapus semua tag HTML dari teks sehingga Halo <b>dunia</b> disimpan sebagai Halo dunia.

- clean_title menolak judul yang menjadi kosong setelah tag dihapus, misalnya payload <img ...> tadi, dan pesan kesalahannya akan tampil di toast.

Karena create_project dan create_project_ajax sama-sama memakai ProjectForm, pembersihan ini berlaku untuk kedua jalur penambahan proyek sekaligus.
"""

"""
ModelForm adalah builtins library yang telah disediakan oleh Django untuk membuat boilerplate suatu form. Struktur dari form sendiri dapat dikustomasi menggunakan metadata atau class Meta.

Penjelasan Kode

- model digunakan untuk menentukan model Django yang menjadi sumber data dan struktur dari ModelForm. Field pada form akan dibuat berdasarkan field yang terdapat pada model tersebut.
- fields digunakan untuk menentukan field model yang ingin ditampilkan pada form. Field dapat ditulis secara eksplisit, seperti ["title", "description"], atau menggunakan "__all__" untuk menampilkan seluruh field yang tersedia.
- widgets digunakan untuk mengatur tampilan dan jenis elemen HTML yang digunakan oleh setiap field pada form. Pada kode di atas, TextInput digunakan untuk field teks satu baris, Textarea digunakan untuk field deskripsi yang membutuhkan area teks lebih besar, dan URLInput digunakan untuk field yang berisi URL. Atribut di dalam attrs, seperti placeholder, maxlength, dan rows, digunakan untuk teks petunjuk, batas jumlah karakter, serta tinggi area input.
"""

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "institution",
            "faculty",
            "thumbnail",
            "started_at",
            "ended_at",
        ]

        labels = {
            "institution": "Nama Institusi",
            "faculty": "Nama Fakultas",
            "thumbnail": "Logo institusi",
            "started_at": "Tahun dimulainya pendidikan",
            "ended_at": "Tahun berakhirnya pendidikan",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Lembaga Pendidikan",
                    "maxlength": 255,
                }
            ),
            "faculty": Textarea(
                attrs={
                    "placeholder": "Fakultas yang dipilih (opsional jika ada)",
                    "rows": 3,
                }
            ),
            "thumbnail": TextInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
            "started_at": TextInput(
                attrs={
                    "placeholder": "2025",
                }
            ),
            "ended_at": TextInput(
                attrs={
                    "placeholder": "2026",
                }
            ),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "started_at",
            "ended_at",
        ]

        labels = {
            "title" : "Nama Pengalaman",
            "description" : "Deskripsi Pengalaman",
            "category" : "Kategori Pengalaman",
            "thumbnail" : "Thumbnail Pengalaman",
            "started_at" : "Waktu Dimulainya Pengalaman",
            "ended_at" : "Waktu Berakhirnya Pengalaman",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Judul pengalaman anda",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pengalaman anda",
                    "rows": 3,
                }
            ),
            "category": Select(
                attrs={"class": "form-control"}),
                "thumbnail": URLInput(attrs={
                "class": "form-control", 
                "placeholder": "https://example.com/image.png (Opsional)"
                }
            ),
            "started_at": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                },
                format='%Y-%m-%dT%H:%M',
            ),
            "ended_at": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }
            ),
        }