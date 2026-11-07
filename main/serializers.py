from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Project, Experience, Education


class ProjectSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id", "title", "description", "tech_stack",
            "project_url", "project_image_url",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value)

    def validate_tech_stack(self, value):
        return strip_tags(value)

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())
    
    """
    Penjelasan Kode

    -ModelSerializer membaca definisi model untuk membentuk field dan implementasi dasar create/update. Meta.model menunjuk model yang sudah ada; tidak membuat tabel baru.

    -fields adalah daftar informasi yang sengaja kita sediakan. Kita tidak mengirim password, email, atau seluruh objek User. Nama akun pemberi star memang ditampilkan secara publik pada Tutorial 05; starred_by_names mempertahankan perilaku tersebut.

    -read_only_fields membuat id tidak dapat ditentukan melalui input API. Tiga SerializerMethodField juga otomatis hanya dapat dibaca. Masing-masing memanggil method get_<nama_field> untuk menghitung nilainya.

    -context membawa informasi tambahan yang tidak disimpan pada model. get_is_starred memakai request agar hasilnya sesuai akun yang sedang melihat, dan menghasilkan False jika tidak ada request atau belum login.

    -validate_title sepadan dengan peran clean_title di ProjectForm. Input berupa spasi ditolak oleh validasi field; input yang menjadi kosong setelah tag dibuang ditolak oleh validasi tambahan ini.

"""   

class ExperienceSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()
    is_ongoing = serializers.ReadOnlyField()

    class Meta:
        model = Experience
        fields = [
            "id", "title", "description", "category", "thumbnail",
            "started_at", "ended_at", "is_ongoing",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value).strip()

    def validate(self, attrs):
        started_at = attrs.get("started_at", getattr(self.instance, "started_at", None))
        ended_at = attrs.get("ended_at", getattr(self.instance, "ended_at", None))
        if started_at and ended_at and ended_at < started_at:
            raise serializers.ValidationError(
                {"ended_at": "End date cannot be earlier than start date."}
            )
        return attrs

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())
        

class EducationSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()
    
    class Meta:
        model = Education
        fields = [
            "id","institution","faculty",
            "thumbnail","started_at","ended_at",
            "star_count","is_starred","starred_by_names",
        ]
        read_only_fields = ["id"]
    
    def validate_institution(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Institution name cannot be empty")
        return value
    
    def validate_faculty(self, value):
        if value is None:
            return None
        value = strip_tags(value).strip()

        return value or None
    
    def validate_thumbnail(self, value):
        if value is None:
            return None
        value = strip_tags(value).strip()
            
        return value or None
    
    def validate(self, attrs):
        started_at = attrs.get("started_at", getattr(self.instance, "started_at", None))
        ended_at = attrs.get("ended_at", getattr(self.instance, "ended_at", None))
        if started_at and ended_at and ended_at < started_at:
            raise serializers.ValidationError(
                {"ended_at": "End date cannot be earlier than start date."}
            )
        return attrs
    
    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())
        