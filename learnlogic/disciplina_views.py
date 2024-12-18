from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics

from .models import Disciplina
from .serializers import DisciplinaSerializer

class DisciplinaView(APIView):
    def post(self, request):
        try:
            serializer = DisciplinaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except APIException as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, pk=None):
        if pk is None:
            disciplinas = Disciplina.objects.all()
            serializer = DisciplinaSerializer(disciplinas, many=True)
            return Response(serializer.data)
        else:
            try:
                disciplinas = Disciplina.objects.get(pk=pk)
                serializer = DisciplinaSerializer(disciplinas)
                return Response(serializer.data)
            except Disciplina.DoesNotExist:
                return Response({'error':'Disciplina não encontrada'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            disciplina = Disciplina.objects.get(pk=pk)
        except Disciplina.DoesNotExist:
            return Response({'error':'Disciplina não encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DisciplinaSerializer(disciplina, data=request.data, partial=True) # partial=True permite atualizações parciais
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            disciplina = Disciplina.objects.get(pk=pk)
            disciplina.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Disciplina.DoesNotExist:
            return Response({'error': 'Disciplina não encontrada'}, status=status.HTTP_404_NOT_FOUND)



class DisciplinaListView(generics.ListAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    #filter_backends = (filters.DjangoFilterBackend,)
    #filter_class = DisciplinaFilter
    permission_classes =[IsAuthenticated] #garante que o usuário está autenticado

    def get_queryset(self):
        """
        Filtra as disciplinas para retornar apenas as relacionadas ao usuário logado.
        """
        usuario_logado= self.request.user


        # Considerando que o modelo Disciplina tem uma relação com Professor, que por sua vez se relaciona com User
        return Disciplina.objects.filter(instrutor__user=usuario_logado)