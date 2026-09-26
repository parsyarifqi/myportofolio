from django.shortcuts import render

from main.models import Experience
from main.models import Education
from main.models import Project
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import ProjectForm, EducationForm, ExperienceForm
from django.forms import ModelForm, TextInput, Textarea, URLInput, Select
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
import datetime

# Create your views here.

def show_main(request):
    last_login = request.COOKIES.get('lasat_login', 'belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Parsya Rifqi Subhani Petrana",
        "npm": "2506535992",
        "study_program": "S1 Ilmu Komputer",
        "bio": ("Undergraduate Student at University of Indonesia Majoring in Computer Science. My interest includes AI, Data Engineering, and Machine Learning. Currently based in Depok, West Java, Indonesia."
        ),
        "last_login": last_login,
    }

    return render(request, "index.html", context)


"""Penjelasan kode:
- Experience.objects.all() mengambil seluruh objek Experience dari basis data dalam bentuk QuerySet.

- context adalah dictionary yang memetakan nama variable dengan data yang akan tersedia pada template

- render(request, "index.html", context) memproses templates/index.html menggunakan data dalam context lalu mengembalikan respons HTML.

- show_main mengirim data profil ke index.html, dan show_experience mengirimkan data experience ke experience.html.

- setiap view memiliki context sendiri, Nilai name pada show_experience dipakai oleh judul, header, dan footer halaman experience.

- request.COOKIES.get('last_login', ...) membaca nilai dari cookie bernama last_login. Kita menggunakan method .get() dengan nilai default agar aplikasi tidak melempar error (KeyError) jika pengunjung membuka halaman utama sebelum login atau jika cookie belum tersedia

- Nilai string tanggal tersebut kita masukkan ke dalam dictionary context dengan kunci "last_login".
"""

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Parsya Rifqi Subhani Petrana",
        "form": form,
    }
    return render(request, "projects_form.html", context)


def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Parsya Rifqi Subhani Petrana",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def update_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project berhasil diperbaharui")
            return redirect('main:show_projects')
    else:
        form = ProjectForm(instance=project)
    
    context = {
        'form': form,
        'project': project,  
        'name': 'Parsya Rifqi Subhani Petrana',
    }
    return render(request, "update_project.html", context)


#education
def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Education baru berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Parsya Rifqi Subhani Petrana",
        "form": form,
    }
    return render(request, "education_form.html", context)


def show_education(request):
    json_response = get_education_json(request)

    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    educations = [education.object for education in educations]
    institution_query = request.GET.get("institution", "").strip()

    context = {
        "name": "Parsya Rifqi Subhani Petrana",
        "education_list": educations,
        "institution_query": institution_query,
    }
    return render(request, "education.html", context)

def get_education_json(request):
    institution_query = request.GET.get("institution", "").strip()
    institutions = Education.objects.all()

    if institution_query:
        institutions = institutions.filter(institution__icontains=institution_query)

    institutions_json = serializers.serialize("json", institutions)
    return HttpResponse(institutions_json, content_type="application/json")

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")

def update_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            messages.success(request, "Educaiton berhasil diperbaharui")
            return redirect('main:show_education')
    else:
        form = EducationForm(instance=education)
    
    context = {
        'form': form,
        'education': education,  
        'name': 'Parsya Rifqi Subhani Petrana',
    }
    return render(request, "update_education.html", context)



#experience
def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Parsya Rifqi Subhani Petrana",
        "form": form,
    }
    return render(request, "experience_form.html", context)


def show_experience(request):
    json_response = get_experience_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Parsya Rifqi Subhani Petrana",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def update_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            messages.success(request, "Experience berhasil diperbaharui")
            return redirect('main:show_experience')
    else:
        form = ExperienceForm(instance=experience)
    
    context = {
        'form': form,
        'experience': experience,  
        'name': 'Parsya Rifqi Subhani Petrana',
    }
    return render(request, "update_experience.html", context)


def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method ==  "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan  login.")
        return redirect("main:login")

    context = {
        "name" : "Parsya Rifqi Subhani Petrana",
        "form" : form,
    }
    return render(request, "register.html", context)

"""
Penjelasan Kode

-Pada permintaan GET, form kosong ditampilkan. Pada POST, form menerima data dari request.POST.

-UserCreationForm menyediakan username, password1, dan password2. is_valid() memeriksa username, kecocokan kedua password, dan aturan password dari konfigurasi proyek.
 
-form.save() membuat akun dengan password yang sudah di-hash. Registrasi tidak langsung membuat pengguna login; pengguna
 diarahkan ke halaman login.
- Jika validasi gagal, form yang sama dirender kembali agar pesan kesalahannya bisa dibaca.
- messages.success() menyiapkan pesan untuk ditampilkan setelah pengalihan. Nilai name tetap nama pemilik portofolio; ganti Burhan dengan namamu sendiri.

Form autentikasi sudah tersedia, jadi main/forms.py tidak perlu diubah. ProjectForm yang kamu buat sebelumnya tetap dipakai untuk proyek.
"""

def login_user(request):
    form =  AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response
    context = {
        "name" : "Parsya Rifqi Subhani Petrana",
        "form" : form,
    }

    return render (request, "login.html", context)

"""
Penjelasan Kode

- AuthenticationForm menerima request sebagai argumen pertama dan data input melalui argumen data. is_valid() memeriksa kredensial menggunakan sistem autentikasi Django.

- Setelah validasi berhasil, form.get_user() memberikan objek pengguna yang sudah terautentikasi. Kita tidak perlu memanggil authenticate() lagi.

- login(request, user) mencatat pengguna dalam session. Pada permintaan berikutnya, Django dapat mengenali pengguna lewat request.user.

- Fungsi view diberi nama login_user agar tidak menimpa fungsi login yang kita impor.

- Implementasi ini selalu mengarahkan pengguna ke halaman profil setelah login. Parameter next belum diproses.

- Di baris response = redirect("main:show_main"), fungsi redirect() menghasilkan objek HttpResponseRedirect.

- Pada objek response tersebut, kita memanggil method .set_cookie(key, value). Method ini akan menambahkan header HTTP Set-Cookie: last_login=... pada paket respons yang dikirimkan ke browser.

- Format waktu kita seragamkan menggunakan format YYYY-MM-DD HH:MM:SS agar rapi dan mudah dibaca oleh pengguna.
"""

def logout_user(request):
    logout(request)
    return redirect("main:show_main")
"""
logout(request) menghapus data session saat ini, lalu pengguna diarahkan ke halaman profil. Akunnya tetap ada di database dan dapat digunakan untuk login kembali.
"""

