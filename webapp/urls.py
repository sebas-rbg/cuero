from django.urls import path

from webapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("",views.inicio, name="inicio"),
    path("servicios",views.servicios, name="servicios"),
    path("tienda",views.tienda, name="tienda"),
    path("blog",views.blog, name="blog"),
    path("contacto", views.contacto, name="contacto")
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
