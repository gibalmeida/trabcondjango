from django.contrib import admin

from .models import Departamento, Vaga, Candidatura

admin.site.register(Departamento)
admin.site.register(Vaga)
admin.site.register(Candidatura)
