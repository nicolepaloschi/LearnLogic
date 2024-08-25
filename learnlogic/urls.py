from django.urls import path
from .aluno_views import AlunoView
from .instrutor_views import InstrutorView
from .disciplina_views import DisciplinaView

urlpatterns = [
    # Alunos
    path('alunos/', AlunoView.as_view(), name='aluno-list-create'), # Para POST e GET em lista
    path('alunos/<int:pk>/', AlunoView.as_view(), name='aluno-detail'), # Para GET, PUT e DELETE em detalhe

    # Instrutores
    path('instrutores/', InstrutorView.as_view()),
    path('instrutores/<int:pk>/', InstrutorView.as_view()),

    # Disciplinas
    path('disciplinas/', DisciplinaView.as_view()),
    path('disciplinas/<int:pk>/', DisciplinaView.as_view())
]