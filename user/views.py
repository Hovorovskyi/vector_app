from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    if request.method == 'POST':
        return auth_views.LoginView.as_view(template_name='user/login.html')(request)
    else:
        return render(request, 'user/login.html')


def logout_view(request):
    return auth_views.LogoutView.as_view()(request)


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login')
        else:
            return render(request, 'user/register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'user/register.html', {'form': form})
