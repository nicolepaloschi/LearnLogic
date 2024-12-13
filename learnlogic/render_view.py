from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from models import Instrutor, Aluno, Disciplina

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def first_page(request):
    return render(request, 'index.html')

def home_view(request):
    return render(request, 'home.html')
