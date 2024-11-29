from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Aluno, Instrutor, Disciplina


class AlunoSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    password = serializers.CharField(write_only=True, source='user.password', required=True, style={'input_type': 'password'})

    class Meta:
        model = Aluno
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'data_nascimento', 'CPF']

    def create(self, validated_data):
        # Extrai os campos do User diretamente do validated_data
        user_data = {
            'username': validated_data.pop('username'),
            'email': validated_data.pop('email'),
            'first_name': validated_data.pop('first_name'),
            'last_name': validated_data.pop('last_name'),
            'password': validated_data.pop('password'),
        }
        # Cria um usuário com os dados
        user = User.objects.create_user(
            username = user_data['username'],
            email = user_data['email'],
            first_name = user_data['first_name'],
            last_name = user_data['last_name'],
            password =user_data['password']
        )

        #Cria um aluno vinculado ao usuário
        aluno = Aluno.objects.create(user=user, **validated_data)

        return aluno


class InstrutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrutor
        fields = '__all__'


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

#Classe User Padrão do Django para autenticação 
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # Cria o usuário com o método `create_user` para garantir o hash da senha
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user


