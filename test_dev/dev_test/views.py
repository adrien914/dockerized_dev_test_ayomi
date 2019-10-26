from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegForm, UsernameUpdateForm, EmailUpdateForm, PasswordUpdateForm

def home(request):
    template_name = "index.html"
    return render(request, template_name, {})

def register(request):
    template_name = "registration.html"    
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            if user is not None:
                login(request, user)
                return redirect('/infos')
    else:
        form = RegForm()
    return render(request, template_name, {'form':form })


    
def connect(request):
    template_name = "connection.html"    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/infos')
        else:
            messages.error(request, 'Identifiants incorrects', extra_tags="alert alert-danger")
            return redirect('/connect')
    else:
        return render(request, template_name, {})


def Logout(request):
    template_name = "index.html"
    logout(request)
    return redirect('home')

@login_required
def infos(request):
    template_name = "infos.html"
    if request.method == "POST":
        if 'username' in request.POST:
            username_form = UsernameUpdateForm(request.POST, instance=request.user)
            email_form = EmailUpdateForm(instance=request.user)
            password_form = PasswordUpdateForm(instance=request.user)
            if username_form.is_valid():
                username_form.save()
        if 'email' in request.POST:
            username_form = UsernameUpdateForm(instance=request.user)
            email_form = EmailUpdateForm(request.POST, instance=request.user)
            password_form = PasswordUpdateForm(instance=request.user)
            if email_form.is_valid():
                email_form.save()
        if 'password' in request.POST:
            username_form = UsernameUpdateForm(instance=request.user)
            email_form = EmailUpdateForm(instance=request.user)
            password_form = PasswordUpdateForm(request.POST, instance=request.user)
            if password_form.is_valid():
                request.user.set_password(request.POST['password'])
                request.user.save();
                messages.success(request, 'Modification du mot de passe effectuee avec succes, veuillez vous reconnecter', extra_tags="alert alert-success")
                return redirect("/connect")
    else:
        username_form = UsernameUpdateForm(instance=request.user)
        email_form = EmailUpdateForm(instance=request.user)
        password_form = PasswordUpdateForm()
        return render(request, template_name, {'username_form': username_form, 'email_form': email_form, 'password_form': password_form})