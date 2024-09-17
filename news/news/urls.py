from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("nesw.urls")),
    path("news/", include("nesw.urls")),
    path("admin/", admin.site.urls),
]