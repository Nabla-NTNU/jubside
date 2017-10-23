from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistrationForm
from django.core.exceptions import PermissionDenied
from . models import User


# Register user
def registration(request):
    if request.user.is_authenticated:
        return redirect('user.profile')
    else:
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(form.cleaned_data['email'],
                                                form.cleaned_data['email'],
                                                form.cleaned_data['password'],
                                                first_name=form.cleaned_data['first_name'],
                                                last_name=form.cleaned_data['last_name'],
                                                starting_year=form.cleaned_data['starting_year'],
                                                is_active = False,
                                                account_verified = False,
                                                is_awaiting_approval = True
                                                )
                user.save()

                return redirect('user.registration')
        else:
            form = RegistrationForm()

        return render(request, 'user_registration.html', {'form': form})

# Recover user password
def recover(request):
    if request.user.is_authenticated:
        return redirect('user.profile')
    else:
        return render(request, 'user_registration.html')

# Displays user profile
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'user_profile.html')
    else:
        raise PermissionDenied

# Displays user settings
def settings(request):
    if request.user.is_authenticated:
        return render(request, 'user_settings.html')
    else:
        raise PermissionDenied

# Lists all events you have signed up on
def events(request):
    if request.user.is_authenticated:
        return render(request, 'user_events.html')
    else:
        raise PermissionDenied

# Lists all users according to different statuses
def registerapplicants(request):
    if request.user.is_authenticated and request.user.has_perm('user.can_view_users'):

        if request.GET.get('list') == 'accepted':

            # get all accepted users in user list
            user_list = User.objects.filter(is_awaiting_approval=False, is_staff=False, is_active=True)
            user_title = 'Godkjente brukere'

        elif request.GET.get('list') == 'declined':

            # get all declined users in user list
            user_list = User.objects.filter(is_awaiting_approval=False, is_staff=False, is_active=False)
            user_title = 'Avslåtte brukere'

        else:

            # get all users awaiting checkup
            user_list = User.objects.filter(is_awaiting_approval=True, is_staff=False)
            user_title = 'Brukere som avventer godkjenning'

        return render(request, 'user_registerapplicants.html', {'user_list': user_list, 'user_title': user_title})
    else:
        raise PermissionDenied

# Change the user status for registration
def changeapplicants(request, action, userid):
    if request.user.is_authenticated and request.user.has_perm('user.can_change_users'):

        if action == 'accept':

            # update user to accepted, and change status to has been checked
            user = User.objects.get(id=userid, is_staff=False)
            user.is_awaiting_approval = False
            user.is_active = True
            user.save(update_fields=["is_awaiting_approval", "is_active"])

            # redirect to register applicants with msg=1 (meaning approved)
            return redirect(reverse('user.registerapplicants') + '?msg=1')

        elif action == 'decline':

            # update user to declined, and change status to has been checked
            user = User.objects.get(id=userid, is_staff=False)
            user.is_awaiting_approval = False
            user.is_active = False
            user.save(update_fields=["is_awaiting_approval", "is_active"])

            # redirect to register applicants with msg = 2 (meaning disapproved)
            return redirect(reverse('user.registerapplicants') + '?msg=2')

        elif action == 'delete':

            # delete user
            user = User.objects.get(id=userid, is_staff=False)
            user.delete()

            # redirect to register applicants with msg = 3 (meaning deleted)
            return redirect(reverse('user.registerapplicants') + '?msg=3')

        else:
            raise PermissionDenied
    else:
        raise PermissionDenied