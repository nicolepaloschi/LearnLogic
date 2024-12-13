from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Instrutor, Aluno, Disciplina, DisciplinaMaterial

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def first_page(request):
    return render(request, 'index.html')


def dashboard_view(request):
    disciplinas = DisciplinaMaterial.objects.all()  # Recupera todas as atividades
    return render(request, 'dashboard.html', {'disciplina': disciplinas})
