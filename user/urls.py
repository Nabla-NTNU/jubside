from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^logg-inn/$', auth_views.login, {'template_name': 'user_login.html', 'redirect_authenticated_user': True}, name='user.login'),
    url(r'^logg-ut/$', auth_views.logout, {'next_page': 'user.login'}, name='user.logout'),
    url(r'^registrer-meg/$', views.registration, name='user.registration'),
    url(r'^glemt-passord/$', views.recover, name='user.recover'),
    url(r'^min-profil/$', views.profile, name='user.profile'),
    url(r'^min-profil/innstillinger/$', views.settings, name='user.settings'),
    url(r'^min-profil/arrangementer/$', views.events, name='user.events'),
    url(r'^min-profil/brukere/$', views.registerapplicants, name='user.registerapplicants'),
    url(r'^min-profil/brukere/(?P<action>accept|decline|delete)/(?P<userid>[0-9]+)/', views.changeapplicants, name='user.changeapplicants')
]