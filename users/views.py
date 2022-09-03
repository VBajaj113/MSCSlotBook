from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import *
from sports.models import BookRequest, Sport
from django.contrib import messages
from PIL import Image


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.is_staff = False
            user.username = form.cleaned_data.get('username')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.set_password(password)
            user.save()

            name = user.username

            messages.success(request, f'Account created for {name}! Please LogIn to continue.')
            return redirect('login')

    else:
        form = UserForm()

    return render(request, "users/register.html", {'form':form, 'title':'Registration'})


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        
        if form.is_valid():
            user = form.save(commit=False)
            new_password = form.cleaned_data.get('new_password')
            old_password = form.cleaned_data.get('old_password')

            if user.check_password(old_password):
                user.set_password(new_password)
            else:
                messages.error(request, f'Your password was incorrect!')
                return redirect('profile')
            
            try:
                user.avatar = request.FILES['avatar']
                user.save()
                img = Image.open(user.avatar.path)
                img.thumbnail((300,300))
                img.save(user.avatar.path)
            except:
                user.save()

            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        form = UserProfileForm(instance=request.user)

    req_lis=[i for i in BookRequest.objects.all() if i.user == request.user]

    context = {
        'form':form,
        'title':'Profile',
        'req_lis':req_lis,
    }
    return render(request, 'users/profile.html', context)


@login_required
def homepage(request):
    sports = [i for i in Sport.objects.all()]
    return render(request, 'users/home.html', {'sports':sports})


def about(request):
    return render(request, 'users/about.html')
