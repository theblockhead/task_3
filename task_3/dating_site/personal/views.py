from django.shortcuts import render

def home(request):
    context = {}
    return render (request, "personal/home_.html", context )
