from django.shortcuts import render

def google_auth(request):
    return render(request, 'users/google_auth.html',)
