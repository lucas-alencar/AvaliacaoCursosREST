from django.urls import path
from .views import CursoAPIView, CursosAPIView, AvaliacaoAPIView, AvaliacoesAPIView

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('avaliacoes/',AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:pk>',AvaliacaoAPIView.as_view(), name='avaliacao'),
    path('cursos/<int:pk>',CursoAPIView.as_view(), name='curso')
]