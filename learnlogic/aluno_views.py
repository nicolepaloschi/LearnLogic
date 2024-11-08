from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.exceptions import APIException
from django_filters import rest_framework as filters

from .models import Aluno
from .serializers import AlunoSerializer

class AlunoView(APIView):
    def post(self, request):
        try:
            serializer = AlunoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {'message': 'Registro de aluno adicionado com sucesso!', 'data': serializer.data},
                    status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except APIException as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, pk=None):
        if pk is None:
            alunos = Aluno.objects.all()
            serializer = AlunoSerializer(alunos, many=True)
            return Response(serializer.data)
        else:
            try:
                aluno = Aluno.objects.get(pk=pk)
                serializer = AlunoSerializer(aluno)
                return Response(serializer.data)
            except Aluno.DoesNotExist:
                return Response({'error':'Registro de aluno não encontrado!'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            aluno = Aluno.objects.get(pk=pk)
        except Aluno.DoesNotExist:
            return Response({'error':'Registro de aluno não encontrado!'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AlunoSerializer(aluno, data=request.data, partial=True) # partial=True permite atualizações parciais
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Registro de aluno atualizado com sucesso!', 'data': serializer.data}
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            aluno = Aluno.objects.get(pk=pk)
            aluno.delete()
            return Response(
                {'message': 'Registro de aluno excluído com sucesso'},
                status=status.HTTP_204_NO_CONTENT
            )
        except Aluno.DoesNotExist:
            return Response({'error': 'Aluno não encontrado'}, status=status.HTTP_404_NOT_FOUND)

class AlunoFilter(filters.FilterSet):
    aluno = filters.CharFilter(field_name="aluno__nome", lookup_expr='icontains')

class AlunoListView(generics.ListAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    # filter_backend = (filters.DjangoFilterBackend)
    filter_class = AlunoFilter