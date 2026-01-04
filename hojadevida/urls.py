from django.contrib import admin
from django.urls import path
from paginasusuario import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.paginabienvenida, name="bienvenida"),
    path("hoja-de-vida/", views.hojadevida, name="hojadevida"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )


