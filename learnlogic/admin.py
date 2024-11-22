from django.contrib import admin
from .models import Aluno, Instrutor, Material, Resumo

# Register your models here.
#adicionei os models para serem visualizados no django admin
admin.site.register(Aluno)
admin.site.register(Instrutor)
admin.site.register(Material)
admin.site.register(Resumo)
