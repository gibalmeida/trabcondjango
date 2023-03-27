from django.urls import path

from . import views

app_name = "vagas"

urlpatterns = [
    path('',views.index,name= 'index'),
    path('candidatarse/<int:vaga_id>/',views.candidatarse,name='candidatarse')
]