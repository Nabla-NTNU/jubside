from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationRequest
from django.views.generic import TemplateView

def registration(request):
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

    return render(request, 'registration_form.html', {'form': form})


def index(request):
    return HttpResponse("Hello, world. You're at the user index.")