from django.shortcuts import render

from main.models import Experience

# Create your views here.

def show_main(request):
    context = {
        "name": "Parsya Rifqi Subhani Petrana",
        "npm": "2506535992",
        "study_program": "S1 Ilmu Komputer",
        "bio": ("Undergraduate Student at University of Indonesia Majoring in Computer Science. My interest includes AI, Data Engineering, and Machine Learning. Currently based in Depok, West Java, Indonesia."
        )
    }

    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Parsya Rifqi Subhani Petrana",
        "experience_list": Experience.objects.all(),
    }

    return render(request, "experience.html", context)

"""Penjelasan kode:
- Experience.objects.all() mengambil seluruh objek Experience dari basis data dalam bentuk QuerySet.

- context adalah dictionary yang memetakan nama variable dengan data yang akan tersedia pada template

- render(request, "index.html", context) memproses templates/index.html menggunakan data dalam context lalu mengembalikan respons HTML.

- show_main mengirim data profil ke index.html, dan show_experience mengirimkan data experience ke experience.html.

- setiap view memiliki context sendiri, Nilai name pada show_experience dipakai oleh judul, header, dan footer halaman experience.
"""