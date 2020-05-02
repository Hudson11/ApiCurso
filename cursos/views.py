from .models import Curso, Avaliacao
from .serializers import CursoSerializers, AvaliacaoSerializers

from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import permissions

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from .permissions import EhSuperUser

'''
 API VERSION 1
'''

#ListCreatedAPIView -> GET / POST
class CursosAPIView (generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializers

#RetrieveUpdateDestroyAPIView PUT / DELETE / GETByID
class CursoAPIView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializers

class AvaliacoesAPIView (generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializers

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()

class AvaliacaoAPIView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializers

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('curso_pk')
                                        , pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.kwargs.get('avaliacao_pk'))

'''
API VERSION 2
'''
class CursoViewSets(viewsets.ModelViewSet):
    permission_classes = (
        EhSuperUser,
        permissions.DjangoModelPermissions
    )
    queryset = Curso.objects.all()
    serializer_class = CursoSerializers

    # recurso /cursos/<curso_pk>/avaliacoes
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        self.pagination_class.page_size = 1
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializers(page, many=True)
            return self.get_paginated_response(serializer.data)

        #curso = self.get_object()
        serializer = AvaliacaoSerializers(avaliacoes, many=True)
        return Response(serializer.data)

'''
class AvaliacaoViewSets(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializers
'''

class AvaliacaoViewSets(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet
    ):

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializers
