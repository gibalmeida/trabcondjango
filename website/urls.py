from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'website'
urlpatterns = [
    path('',views.home, name= 'home'),
    path('quem_somos',views.quemsomos, name= 'quemsomos')
]