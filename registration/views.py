from django.shortcuts import render,redirect
import urllib
from django.views import generic
from django.contrib.auth.models import User,auth
# from django.contrib.auth.forms import UserCreationForm,UserChangeForm
# from django.urls import reverse_lazy
# from .forms import  SignUpForm

# Create your views here.

# class UserRegisterView(generic.CreateView):
#     form_class = SignUpForm
#     template_name = 'registration/register.html'
#     success_url = reverse_lazy('login')


def CreateMember(request):
    content = {}
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if password1 == password2 :
            if User.objects.filter(username=username).exists():
                content['error'] = "Username exist"
            elif User.objects.filter(email=email).exists():
                content['error'] = "Email exist"
            else:
                user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password1
                )
                user.save()
                content['success'] = "Successfully Creating"

                # return redirect('login')
                return render(request,'registration/login.html',content)

        else:
            content['error'] = "Password doesnot match!"

    return render(request, 'registration/register.html', content)

def LoginMember(request):
    content = {}
    if request.method == 'POST':
        # email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:

            if User.objects.filter(username=username).exists():
                user_password = User.objects.get(username=username).password
                if user_password != password:
                    content['error'] = "Password is wrong!"
            else :
                content['error'] = "There is no like an user!"

            return render(request, 'registration/login.html', content)
            # return redirect('login')
    else:
        return render(request, 'registration/login.html', content)

def LogoutMember(request):
    auth.logout(request)
    return redirect('/')

def EditProfile(request):
    content = {}
    user = User.objects.get(pk=request.user.id)
    content['user'] = user

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        if user.username == username:
            content['error'] = "Username exist"

        elif user.email == email:
            content['error'] = "Email exist"

        else:
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            content['success'] = "Profile Successfully updated"


    return render(request, 'registration/edit_profile.html', content)

def ResetPassword(request):
    content = {}
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.id)
        username = user.username
        print("user is ",user)
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        check_password = user.check_password(password1) #True or False

        if check_password:
            content['error'] = "Password Same as before"
        # if user.password == password1 :
        #
        elif password1 != password2:
            content['error'] = "Password doesnot match!"
        else:
            print("else icindeyim")
            user.set_password(password1)
            user.save()
            user = User.objects.get(username = username)
            auth.login(request, user)
            # auth.authenticate(username=user.username, password=password1)
            content['success'] = "Your password Successfully updated"
            # return render(request,'registration/login.html',content)

    return render(request,'registration/reset_password.html', content)
