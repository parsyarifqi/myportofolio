from django.urls import path
from main.views import show_main, show_experience

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
]

"""
Penjelasan kode:

- app_name = "main" memberikan namespace pada URL milik aplikasi main.
- Pola URL "" berarti halaman utama aplikasi tanpa tambahan path.
- Pola URL "experience/" mengarahkan permintaan /experience/ ke show_experience.
- name="show_main" dan name="show_experience" memberi nama pada rute agar dapat dirujuk melalui navigasi dan test tanpa menulis URL secara langsung.
"""