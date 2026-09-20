from django.urls import path
from main.views import show_main, show_experience, create_experience, get_experience_json, delete_experience, show_education, create_education, get_education_json, delete_education, create_project, show_projects, get_projects_json, delete_project

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_project"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/delete/",delete_experience,name="delete_experience"),
    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_project"),
    path("api/education/", get_education_json, name="get_projects_json"),
    path("education/<uuid:project_id>/delete/",delete_education,name="delete_project"),
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project"),
    
]


"""
Penjelasan kode:

- app_name = "main" memberikan namespace pada URL milik aplikasi main.
- Pola URL "" berarti halaman utama aplikasi tanpa tambahan path.
- Pola URL "experience/" mengarahkan permintaan /experience/ ke show_experience.
- name="show_main" dan name="show_experience" memberi nama pada rute agar dapat dirujuk melalui navigasi dan test tanpa menulis URL secara langsung.
"""