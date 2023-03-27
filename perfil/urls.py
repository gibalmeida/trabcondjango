from django.urls import path

from . import views

app_name = 'perfil'

urlpatterns = [
    path('new/', views.CreatePersonView.as_view(),name='perfil.new'),
    path('edit/', views.UpdatePersonView.as_view(),name='perfil.edit')
]
