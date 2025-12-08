from django.shortcuts import render

def home(request):
    return render(request, "clinica/home.html")