from django.shortcuts import render

def loginPage(request):
    return render(request, 'login.html')

def registerPage(request):
    return render(request, 'register.html')
