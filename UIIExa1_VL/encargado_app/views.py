from django.shortcuts import render
from .models import Encargado
# Create your views here.
def listadoEncargado(request):
    losencargados=Encargado.objects.all()
    return render(request,"gestionarEncargado.html",{"misencargados":losencargados})