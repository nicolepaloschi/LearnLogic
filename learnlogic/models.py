from django.db import models
from django.contrib.auth.models import User

"""
    Objetivos da aula: ter uma própria classe User do Django
    Podemos adidiconar informações para esse usuário, assim temos duas opções, usar herança ou o relacionamento por chave estrangeira
"""

class Aluno(models.Model):
    #adicionando chave estrangeira de usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='aluno_profile')
    CPF = models.CharField(max_length=11, null=False)
    data_nascimento = models.DateField(null=False)

    # --> Retirar da tabela, pois já existe em User
    # nome = models.CharField(max_length=200, null=False) 
    # email = models.EmailField(max_length=254, null=False)
    # senha = models.CharField(max_length=64, null=False)

    
    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Certificacao(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    instituicao = models.CharField(max_length=200)
    data_emissao = models.DateField(null=False)

    def __str__(self):
        return self.titulo

class Instrutor(models.Model): # a mesma coisa será aplicada aqui
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='instrutor_profile')
    CPF = models.CharField(max_length=11)
    data_nascimento = models.DateField(null=False)
    id_certificacao = models.ForeignKey(Certificacao, on_delete=models.CASCADE)

    # --> Retirar da tabela, pois já existe em User
    # nome = models.CharField(max_length=200, null=False) 
    # email = models.EmailField(max_length=254, null=False)
    # senha = models.CharField(max_length=64, null=False)
    
    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Material(models.Model):
    instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=300, null=False)
    autor = models.CharField(max_length=200, null=False)
    tipo = models.CharField(max_length=80)
    descricao = models.CharField(max_length=1500)
    data_publicacao = models.DateField(null=False)

    class Meta: 
        constraints = [
            models.UniqueConstraint(fields=['autor','titulo'], name='unique_autor_titulo')
        ]

    def __str__(self):
        return self.titulo
    
class Disciplina(models.Model):
    nome = models.CharField(max_length=200, null=False, unique=True)

    def __str__(self):
        return self.nome
    
class DisciplinaMaterial(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('disciplina', 'material')

    def __str__(self):
        return f'{self.disciplina.nome} - {self.material.titulo}'
    
class DisciplinaInstrutor(models.Model):
    instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('instrutor', 'disciplina')

    def __str__(self):
        return f'{self.instrutor.nome} - {self.disciplina.nome}'
    
class Resumo(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    titulo = models.CharField(max_length=100, default='Título do Resumo')
    conteudo = models.CharField(max_length=8000, null=False)

    def __str__(self):
        return self.titulo


class DisciplinaResumo(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    resumo = models.ForeignKey(Resumo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('disciplina','resumo')
        constraints = [
            models.UniqueConstraint(fields=['disciplina', 'resumo'], name='unique_disciplina_resumo')
        ]

    def __str__(self):
        return f'{self.disciplina.nome} - {self.resumo.titulo}'