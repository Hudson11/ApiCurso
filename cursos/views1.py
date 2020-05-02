from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Curso, Avaliacao
from .serializers import CursoSerializers, AvaliacaoSerializers

class CursoAPIView(APIView):
    '''
    API DE ENSINO UDEMY
    '''

    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializers(cursos, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AvaliacaoAPIView(APIView):
    '''
    API DE AVALIAÇÕES
    '''

    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializers(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
