from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    AvaliacaoAPIView,
    AvaliacoesAPIView,
    CursoAPIView,
    CursosAPIView,
    CursoViewSets,
    AvaliacaoViewSets
)

router = SimpleRouter()
router.register('cursos', CursoViewSets)
router.register('avaliacoes', AvaliacaoViewSets)

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='cursos/avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='cursos/avaliacao'),

    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),

]