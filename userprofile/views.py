from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def loginPage(request):
    data = {'title': 'Login',}

    if request.user.is_authenticated:
        return redirect("profilePage")
    else:
        if request.method == "POST":
            input_username = request.POST.get("inputUsername")
            input_password = request.POST.get("inputPassword")
            user = authenticate(username=input_username, password=input_password)
            if user is not None:
                login(request, user)
                return redirect('profilePage')
            else:
                data['message'] = 'Invalid Username or Password.'

    return render(request, 'login.html', data)

def registerPage(request):
    data = {'message': '',
            'title': 'Register',}
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if(password1 != password2):
            data['message'] = 'Password do not match.'
        elif(User.objects.filter(username=username).exists()):
            data['message'] = 'Username already exists.'
        else:
            user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, email = email, password = password1)
            user.save()
            return redirect('loginPage')
   
    return render(request, 'register.html', data)

def profilePage(request):
    data = {'title': 'Profile',}
    return render(request, 'profile.html', data)

def editpProfilePage(request):
    data = {'title': 'Edit Profile',}
    return render(request, 'edit_profile.html', data)

def logoutPage(request):
    logout(request)
    return redirect('loginPage')