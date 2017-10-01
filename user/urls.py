from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='user.index'),
    url(r'^registrering/', views.registration, name='user.registration')
]
