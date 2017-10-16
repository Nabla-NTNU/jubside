from django.shortcuts import render, redirect
from .forms import RegistrationRequest
from django.core.exceptions import PermissionDenied

def index(request):
    return render(request, 'registration.html', {})

def registration(request):
    if request.user.is_authenticated:
        return redirect('user.profile')
    else:
        if request.method == "POST":
            form = RegistrationRequest(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.username = post.email
                post.is_active = False
                post.is_awaiting_approval = True

                post.save()
                return redirect('user.registration', pk=post.pk)
        else:
            form = RegistrationRequest()

        return render(request, 'registration.html', {'form': form})

def recover(request):
    if request.user.is_authenticated:
        return redirect('user.profile')
    else:
        return render(request, 'registration.html')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        raise PermissionDenied

def settings(request):
    if request.user.is_authenticated:
        return render(request, 'settings.html')
    else:
        raise PermissionDenied

def events(request):
    if request.user.is_authenticated:
        return render(request, 'events.html')
    else:
        raise PermissionDenied