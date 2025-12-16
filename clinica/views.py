from django.shortcuts import render

def home(request):
    return render(request, "clinica/home.html")

def sobre(request):
    return render(request, "clinica/sobre.html")
