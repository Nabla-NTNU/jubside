"""jubside URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    url(r'^$', views.index, name='jubside.frontpage'),
    url(r'^user/', include('user.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^arrangement/', include('events.urls')),
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'img/favicon.ico', permanent=True)),
    url(r'^markdown/', include('django_markdown.urls')),
    #url(r'^calendar/', include('happenings.urls', namespace='calendar')),

]

if settings.DEBUG:
    urlpatterns += [
         url(r'^500.html/$', TemplateView.as_view(template_name='500.html')),
         url(r'^404.html/$', TemplateView.as_view(template_name='404.html')),
    ]