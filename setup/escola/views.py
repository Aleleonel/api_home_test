from rest_framework import viewsets
from escola.models import Aluno, Curso
from escola.serializer import AlunoSerializer, CursoSerializer, Matricula, MatriculaSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Exibe todos os Cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando todas as matrícula"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
