from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException

from .models import Instrutor
from .serializers import InstrutorSerializer

class InstrutorView(APIView):
    def post(self, request):
        try:
            serializer = InstrutorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except APIException as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, pk=None):
        if pk is None:
            instrutores = Instrutor.objects.all()
            serializer = InstrutorSerializer(instrutores, many=True)
            return Response(serializer.data)
        else:
            try:
                instrutores = Instrutor.objects.get(pk=pk)
                serializer = InstrutorSerializer(instrutores)
                return Response(serializer.data)
            except Instrutor.DoesNotExist:
                return Response({'error':'Instrutor não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            instrutor = Instrutor.objects.get(pk=pk)
        except Instrutor.DoesNotExist:
            return Response({'error':'Instrutor não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = InstrutorSerializer(instrutor, data=request.data, partial=True) # partial=True permite atualizações parciais
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            instrutor = Instrutor.objects.get(pk=pk)
            instrutor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Instrutor.DoesNotExist:
            return Response({'error': 'Instrutor não encontrado'}, status=status.HTTP_404_NOT_FOUND)