from django.urls import path
from .aluno_views import AlunoView
from .instrutor_views import InstrutorView
from .disciplina_views import DisciplinaView
from .user_view import UserRegisterAPIView 
from .render_view import first_page, dashboard_view

urlpatterns = [
    #render pages
    path('firstpage/', first_page, name='first_page'),
    path('dashboard/', dashboard_view, name='dashboard'),

    # Alunos
    path('alunos/', AlunoView.as_view(), name='aluno-list-create'), # Para POST e GET em lista
    path('alunos/<int:pk>/', AlunoView.as_view(), name='aluno-detail'), # Para GET, PUT e DELETE em detalhe

    # Instrutores
    path('instrutores/', InstrutorView.as_view(), name='instrutores'),
    path('instrutores/<int:pk>/', InstrutorView.as_view()),

    # Disciplinas
    path('disciplinas/', DisciplinaView.as_view(), name='disciplina'),
    path('disciplinas/<int:pk>/', DisciplinaView.as_view()),

    #url para registro de usuário
    path('register/', UserRegisterAPIView.as_view(), name='user-register')

]