from django.shortcuts import render, redirect
# Create your views here.
def home_page_base(request):
    return render(request, "base.html" ,{})


def Accueil(request):
    return render(request, "Accueil.html")

def Gestion_utilisateur(request):
    return render(request, "Gestion_utilisateur.html")

def Statistique(request):
    return render(request,"Statistique.html")

def Addusers(request):
    return render(request,"Addusers.html")

def reinitialisation(request):
    return render(request,"reinitialisation.html")