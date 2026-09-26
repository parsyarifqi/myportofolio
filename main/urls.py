from django.urls import path
from main.views import show_main, show_experience, create_experience, get_experience_json, delete_experience, update_experience, show_education, create_education, get_education_json, update_education, delete_education, create_project, show_projects, get_projects_json, delete_project, update_project, register, login_user, logout_user, toggle_star

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/update/",update_experience,name="update_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/delete/",delete_experience,name="delete_experience"),
    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_education"),
    path("education/<uuid:education_id>/update/",update_education,name="update_education"),
    path("api/education/", get_education_json, name="get_projects_json"),
    path("education/<uuid:education_id>/delete/",delete_education,name="delete_education"),
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project"),
    path("projects/<uuid:project_id>/update/",update_project,name="update_project"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<uuid:project_id>/star/", toggle_star, name="toggle_star"),
]


"""
Penjelasan kode:

- app_name = "main" memberikan namespace pada URL milik aplikasi main.
- Pola URL "" berarti halaman utama aplikasi tanpa tambahan path.
- Pola URL "experience/" mengarahkan permintaan /experience/ ke show_experience.
- name="show_main" dan name="show_experience" memberi nama pada rute agar dapat dirujuk melalui navigasi dan test tanpa menulis URL secara langsung.
"""