from django.urls import path
from webapp import views

urlpatterns = [

    path("inicio",views.inicio, name="inicio"),
    path("servicios",views.servicios, name="servicios"),
    path("tienda",views.tienda, name="tienda"),
    path("blog",views.blog, name="blog"),
    path("contacto", views.contacto, name="contacto")
]
