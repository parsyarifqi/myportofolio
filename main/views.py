from django.shortcuts import render

from main.models import Experience
from main.models import Education
from main.models import Project
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import ProjectForm

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

def show_education(request):
    context = {
        "name": "Parsya Rifqi Subhani Petrana",
        "education_list": Education.objects.all(),
    }

    return render(request, "education.html", context)

"""Penjelasan kode:
- Experience.objects.all() mengambil seluruh objek Experience dari basis data dalam bentuk QuerySet.

- context adalah dictionary yang memetakan nama variable dengan data yang akan tersedia pada template

- render(request, "index.html", context) memproses templates/index.html menggunakan data dalam context lalu mengembalikan respons HTML.

- show_main mengirim data profil ke index.html, dan show_experience mengirimkan data experience ke experience.html.

- setiap view memiliki context sendiri, Nilai name pada show_experience dipakai oleh judul, header, dan footer halaman experience.
"""

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience baru berhasil ditambahkan!")
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