from django.urls import path
from encargado_app import views
urlpatterns = [
    path("",views.listadoEncargado,name="listadoEncargado")
]
