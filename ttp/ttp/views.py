from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .code import affichage
from .code import change_deroulante

def index_view(request):
    #return HttpResponse('Hello World hehehe')
    return render(request,"index.html")

@csrf_exempt
def compute(request):
    lieu = request.POST.get("lieu")
    choix_dep = request.POST.get("choix_dep")
    choix_ville = request.POST.get("choix_ville")
    choix_fil = request.POST.get("choix_fil")
    result = affichage(lieu,choix_dep,choix_ville,choix_fil)
    return JsonResponse({"operation_result": result})

@csrf_exempt
def change_liste(request):
    lieu = request.POST.get("lieu")
    choix_dep = request.POST.get("choix_dep")
    choix_ville = request.POST.get("choix_ville")
    choix_fil = request.POST.get("choix_fil")
    result = change_deroulante(lieu,choix_dep,choix_ville,choix_fil)
    return JsonResponse({"change_result": result})




