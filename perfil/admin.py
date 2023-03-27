from django.contrib import admin

from .models import Pessoa, Emprego, Formacao

admin.site.register(Pessoa)
admin.site.register(Emprego)
admin.site.register(Formacao)